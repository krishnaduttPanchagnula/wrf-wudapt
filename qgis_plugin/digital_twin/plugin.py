"""Thin QGIS front-end for the headless weather digital-twin engine."""
import json
import math
from datetime import datetime
from pathlib import Path

from qgis.core import (QgsCoordinateReferenceSystem, QgsCoordinateTransform,
                       QgsProject, QgsVectorLayer, QgsWkbTypes)
from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand

try:
    from PyQt5.QtCore import QProcess, Qt, pyqtSignal
    from PyQt5.QtGui import QIcon
    from PyQt5.QtWidgets import (QDialog, QDoubleSpinBox, QFormLayout, QHBoxLayout,
                                 QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                                 QSpinBox, QVBoxLayout)
except ImportError:
    from PySide2.QtCore import QProcess, Qt, pyqtSignal
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import (QDialog, QDoubleSpinBox, QFormLayout, QHBoxLayout,
                                   QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                                   QSpinBox, QVBoxLayout)

DEFAULT_ROOT = "/home/krishna/Documents/wrf-wudapt"


class AreaTool(QgsMapToolEmitPoint):
    """Brush: click the map to set the proposal centre; radius comes from the dialog."""
    picked = pyqtSignal(float, float)

    def __init__(self, canvas, dialog):
        super().__init__(canvas)
        self.dialog = dialog
        self.band = QgsRubberBand(canvas, QgsWkbTypes.PolygonGeometry)
        self.band.setColor(Qt.red)
        self.band.setWidth(2)

    def canvasClicked(self, point, button):
        crs = self.dialog.iface.mapCanvas().mapSettings().destinationCrs()
        xform = QgsCoordinateTransform(crs, QgsCoordinateReferenceSystem("EPSG:4326"),
                                       QgsProject.instance())
        lon, lat = xform.transform(point).x(), xform.transform(point).y()
        self.dialog.set_center(lat, lon)
        self.picked.emit(lat, lon)
        self.draw(lat, lon, float(self.dialog.radius.value()))

    def draw(self, lat, lon, radius_km):
        self.band.reset(True)
        dlat = radius_km / 111.32
        dlon = dlat / max(0.01, math.cos(math.radians(lat)))
        for i in range(37):
            a = 2 * math.pi * i / 36
            from qgis.core import QgsPointXY
            self.band.addPoint(QgsPointXY(lon + dlon * math.cos(a),
                                          lat + dlat * math.sin(a)))
        self.band.show()

    def deactivated(self):
        self.band.reset(True)


class TwinDialog(QDialog):
    def __init__(self, iface):
        super().__init__(iface.mainWindow())
        self.iface = iface
        self.setWindowTitle("Weather Digital Twin")
        self.resize(520, 560)
        self.root = QLineEdit(DEFAULT_ROOT)
        self.lat = QDoubleSpinBox(); self.lat.setRange(-90, 90); self.lat.setDecimals(5)
        self.lat.setValue(45.49370)
        self.lon = QDoubleSpinBox(); self.lon.setRange(-180, 180); self.lon.setDecimals(5)
        self.lon.setValue(9.16646)
        self.radius = QDoubleSpinBox(); self.radius.setRange(5, 200); self.radius.setValue(50)
        self.start = QLineEdit("2022-07-25T00:00:00Z")
        self.start2 = QLineEdit("2023-07-25T00:00:00Z")
        self.hours = QSpinBox(); self.hours.setRange(1, 48); self.hours.setValue(18)
        self.lcz = QLineEdit(str(Path(DEFAULT_ROOT) / "data/raw/lcz_europe_4326.tif"))
        self.from_cat = QSpinBox(); self.from_cat.setRange(1, 21); self.from_cat.setValue(13)
        self.to_cat = QSpinBox(); self.to_cat.setRange(1, 21); self.to_cat.setValue(10)
        self.fraction = QDoubleSpinBox(); self.fraction.setRange(0.05, 1.0); self.fraction.setValue(0.8)
        self.log = QPlainTextEdit(); self.log.setReadOnly(True)

        form = QFormLayout()
        form.addRow("Project root", self.root)
        form.addRow("Latitude", self.lat)
        form.addRow("Longitude", self.lon)
        form.addRow("Radius (km)", self.radius)
        form.addRow("Start (UTC ISO)", self.start)
        form.addRow("Second start (UTC ISO)", self.start2)
        form.addRow("Hours", self.hours)
        form.addRow("LCZ GeoTIFF (optional)", self.lcz)
        form.addRow("From land-use class", self.from_cat)
        form.addRow("To land-use class", self.to_cat)
        form.addRow("Fraction replaced", self.fraction)

        brush = QPushButton("Brush: pick area on map")
        brush.clicked.connect(self.pick_area)
        baseline = QPushButton("1. Generate baseline case + run")
        baseline.clicked.connect(self.generate)
        scenario = QPushButton("2. Apply proposal + compare")
        scenario.clicked.connect(self.apply)
        years = QPushButton("3. Compare years")
        years.clicked.connect(self.compare_years)
        load = QPushButton("4. Load results into QGIS")
        load.clicked.connect(self.load_results)
        btns = QHBoxLayout()
        for b in (brush, baseline, scenario, years, load):
            btns.addWidget(b)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(btns)
        layout.addWidget(QLabel("Engine output"))
        layout.addWidget(self.log)
        self.setLayout(layout)
        self.tool = None
        self.process = None

    def set_center(self, lat, lon):
        self.lat.setValue(lat)
        self.lon.setValue(lon)

    def pick_area(self):
        self.tool = AreaTool(self.iface.mapCanvas(), self)
        self.tool.picked.connect(lambda a, b: self.log.appendPlainText(
            f"proposal centre: {a:.5f}, {b:.5f}  radius {self.radius.value()} km"))
        self.iface.mapCanvas().setMapTool(self.tool)

    def _run(self, command):
        self.process = QProcess(self)
        self.process.setWorkingDirectory(self.root.text())
        self.process.readyReadStandardOutput.connect(
            lambda: self.log.appendPlainText(
                bytes(self.process.readAllStandardOutput()).decode(errors="replace")))
        self.process.readyReadStandardError.connect(
            lambda: self.log.appendPlainText(
                bytes(self.process.readAllStandardError()).decode(errors="replace")))
        self.log.appendPlainText(f"$ {command}")
        self.process.start("/bin/bash", ["-lc", command])

    def _write(self, name, data):
        path = Path(self.root.text()) / "output" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2))
        return path

    def generate(self):
        req = {
            "lat": self.lat.value(), "lon": self.lon.value(),
            "radius_km": self.radius.value(), "start": self.start.text(),
            "hours": self.hours.value(),
        }
        if self.lcz.text().strip():
            req["lcz_tif"] = self.lcz.text().strip()
        self._write("twin_request.json", req)
        self._run("./run.sh run 'python scripts/twin.py prepare /work/output/twin_request.json"
                  " --case /work/output/twin_baseline && python scripts/twin.py baseline"
                  " /work/output/twin_baseline'")

    def apply(self):
        proposal = {
            "area": {"lat": self.lat.value(), "lon": self.lon.value(),
                     "radius_km": self.radius.value()},
            "from_cat": self.from_cat.value(), "to_cat": self.to_cat.value(),
            "fraction": self.fraction.value(),
        }
        self._write("twin_proposal.json", proposal)
        self._run("./run.sh run 'python scripts/twin.py scenario /work/output/twin_baseline"
                  " /work/output/twin_proposal.json --out /work/output/twin_scenario &&"
                  " python scripts/twin.py compare /work/output/twin_baseline"
                  " /work/output/twin_scenario --out /work/output/twin_results'")

    def compare_years(self):
        req = {
            "lat": self.lat.value(), "lon": self.lon.value(),
            "radius_km": self.radius.value(), "start": self.start2.text(),
            "hours": self.hours.value(),
        }
        if self.lcz.text().strip():
            req["lcz_tif"] = self.lcz.text().strip()
        self._write("twin_request_2.json", req)
        if not (Path(self.root.text()) / "output/twin_proposal.json").exists():
            self.log.appendPlainText("run step 2 first (proposal not written)")
            return
        when = datetime.fromisoformat(req["start"].replace("Z", "+00:00"))
        study = f"twin_{req['lat']:.4f}_{req['lon']:.4f}_{when:%Y%m%dT%H}"
        self._run("./run.sh run 'python scripts/twin.py run"
                  " /work/output/twin_request_2.json /work/output/twin_proposal.json &&"
                  " python scripts/twin.py compare-years /work/output/twin_results"
                  f" /work/output/{study}/results --out /work/output/years'")

    def load_results(self):
        base = Path(self.root.text()) / "output/twin_results"
        for name, title in [("t2_baseline_points.csv", "Base T2 per grid cell (K)"),
                            ("t2_scenario_points.csv", "Proposal T2 per grid cell (K)"),
                            ("delta_t2_points.csv", "ΔT2 per grid cell (K)"),
                            ("delta_by_landuse.csv", "ΔT2 by land-use class")]:
            path = base / name
            if not path.exists():
                self.log.appendPlainText(f"missing {path}")
                continue
            uri = f"file:///{path}?type=csv&detectTypes=yes"
            if name.endswith("points.csv"):
                uri += "&xField=lon&yField=lat"
            layer = QgsVectorLayer(uri, title, "delimitedtext")
            if layer.isValid():
                QgsProject.instance().addMapLayer(layer)
            else:
                self.log.appendPlainText(f"could not load {path}")


class DigitalTwinPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.dialog = None

    def initGui(self):
        try:
            from PyQt5.QtWidgets import QAction
        except ImportError:
            from PySide2.QtWidgets import QAction
        self.action = QAction("Weather Digital Twin", self.iface.mainWindow())
        icon = Path(__file__).parent / "icon.png"
        if icon.exists():
            self.action.setIcon(QIcon(str(icon)))
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        if self.action:
            self.iface.removeToolBarIcon(self.action)

    def run(self):
        if self.dialog is None:
            self.dialog = TwinDialog(self.iface)
        self.dialog.show()
