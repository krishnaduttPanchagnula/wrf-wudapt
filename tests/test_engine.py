"""Fast, WRF-free checks for the installable engine."""
import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from wrf_digital_twin.engine import (CaseRequest, build_namelists, compare_years,
                                     study_name, warm_case, write_comparison_report,
                                     write_validation_report)


class TestRequest(unittest.TestCase):
    def test_grid_centred_and_sized(self):
        self.assertEqual(CaseRequest(45.5, 9.1, 25, "2022-07-25T00:00:00Z", 6).grid_n, 31)
        self.assertEqual(CaseRequest(45.5, 9.1, 100, "2022-07-25T00:00:00Z", 6).grid_n, 73)

    def test_gfs_window_must_be_6_hourly(self):
        for hours in (1, 5, 7):
            with self.assertRaises(ValueError):
                CaseRequest(45.5, 9.1, 25, "2022-07-25T00:00:00Z", hours)

    def test_namelists_follow_request(self):
        req = CaseRequest(45.4937, 9.16646, 25, "2022-07-25T00:00:00Z", 6)
        with tempfile.TemporaryDirectory() as tmp:
            case = Path(tmp)
            build_namelists(req, case)
            wps = (case / "namelist.wps").read_text()
            wrf = (case / "namelist.input").read_text()
            self.assertIn("ref_lat = 45.493700", wps)
            self.assertIn("ref_lon = 9.166460", wps)
            self.assertIn("e_we = 31, 31,", wps)
            self.assertIn("end_date   = '2022-07-25_06:00:00'", wps)
            self.assertIn("start_day = 25, 25,", wrf)
            self.assertIn("end_hour = 6, 6,", wrf)
            self.assertIn("i_parent_start = 1, 11,", wrf)

    def test_study_name_is_stable(self):
        req = CaseRequest(45.4937, 9.16646, 25, "2023-07-25T00:00:00Z", 6)
        self.assertEqual(study_name(req), "twin_45.4937_9.1665_20230725T00")

    def test_multi_day_window_is_supported(self):
        req = CaseRequest(45.4937, 9.16646, 25, "2022-07-25T00:00:00Z", 72)
        with tempfile.TemporaryDirectory() as tmp:
            build_namelists(req, Path(tmp))
            wps = (Path(tmp) / "namelist.wps").read_text()
            self.assertIn("end_date   = '2022-07-28_00:00:00'", wps)
            self.assertIn("end_day = 28, 28,", (Path(tmp) / "namelist.input").read_text())


class TestYearComparison(unittest.TestCase):
    @staticmethod
    def study(root, name, base_t, scenario_t, start):
        results = root / name / "results"
        results.mkdir(parents=True)
        case = root / name / "baseline"
        case.mkdir(parents=True)
        (case / "request.json").write_text(json.dumps({"start": start}))
        times = pd.date_range("2022-07-25", periods=6, freq="h", tz="UTC")
        for label, temp in (("baseline", base_t), ("scenario", scenario_t)):
            pd.DataFrame({"time": times, "domain": [2] * 6, "LCZ": [1, 2] * 3,
                          "T2": [temp] * 6}).to_csv(
                results / f"zonal_{label}.csv", index=False)
        return results

    def test_compares_effects_not_just_temperature(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = self.study(root, "y1", 300.0, 299.5, "2022-07-25T00:00:00Z")
            b = self.study(root, "y2", 302.0, 301.0, "2023-07-25T00:00:00Z")
            out = compare_years(a, b, root / "years")

            baseline = pd.read_csv(out / "baseline_year_on_year.csv")
            effects = pd.read_csv(out / "effect_year_on_year.csv")
            summary = json.loads((out / "years.json").read_text())
            self.assertEqual(len(baseline), 6)
            self.assertTrue((baseline["second_minus_first_K"] == 2.0).all())
            self.assertEqual(len(effects), 6)
            self.assertTrue((effects["first_effect_K"] == -0.5).all())
            self.assertTrue((effects["second_effect_K"] == -1.0).all())
            self.assertTrue((effects["second_minus_first_K"] == -0.5).all())
            self.assertEqual(summary["first_start"], "2022-07-25T00:00:00Z")
            self.assertEqual(summary["second_start"], "2023-07-25T00:00:00Z")
            self.assertAlmostEqual(summary["effect_change_mean_K"], -0.5)

    def test_side_by_side_report_shows_three_columns_and_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            results = TestYearComparison.study(root, "y1", 300.0, 299.5,
                                               "2022-07-25T00:00:00Z")
            page = write_comparison_report(results)
            text = page.read_text()
            for heading in ("Base (K)", "Proposal (K)", "Difference (K)"):
                self.assertIn(heading, text)
            self.assertIn("299.5", text)
            self.assertIn("-0.5", text)
            self.assertIn("No validation metrics found", text)

            (results / "results.json").write_text(json.dumps({"validation": {
                "source": "ERA5 test", "full": {"n": 2, "bias": -1.0, "rmse": 2.0},
                "held_out_12_18Z": {"rmse": 3.0}}}))
            text = write_comparison_report(results).read_text()
            self.assertIn("ERA5 test", text)
            self.assertIn("held-out RMSE 3.0 K", text)
            self.assertNotIn("No validation metrics found", text)

    def test_warm_case_changes_initial_and_boundary_fields(self):
        from netCDF4 import Dataset

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case = root / "case"
            case.mkdir()
            (case / "namelist.input").write_text("")
            fields = (("wrfinput_d01", "T"), ("wrfinput_d02", "T"),
                      ("wrfbdy_d01", "T_BXS"))
            for name, var in fields:
                with Dataset(case / name, "w") as ds:
                    ds.createDimension("Time", 1)
                    ds.createVariable(var, "f4", ("Time",))[:] = [280.0]
            out = warm_case(case, root / "warm", 2.0)
            for name, var in fields:
                with Dataset(out / name) as ds:
                    self.assertAlmostEqual(float(ds.variables[var][:].mean()), 282.0)

    def test_geotiff_export_from_delta_points(self):
        import rasterio

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            results = TestYearComparison.study(root, "y1", 300.0, 299.5,
                                               "2022-07-25T00:00:00Z")
            pd.DataFrame({"lat": [45.0, 45.0, 45.1, 45.1],
                          "lon": [9.0, 9.1, 9.0, 9.1],
                          "delta_T2_K": [-0.5, -0.4, -0.3, -0.2]}).to_csv(
                results / "delta_t2_points.csv", index=False)
            out = write_comparison_report(results)
            with rasterio.open(out.parent / "delta_t2.tif") as ds:
                self.assertEqual((ds.width, ds.height), (2, 2))
                self.assertEqual(ds.crs.to_epsg(), 4326)
                self.assertAlmostEqual(float(ds.read(1)[0, 0]), -0.5, places=5)

    def test_validation_report_uses_only_recorded_metrics(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            results = TestYearComparison.study(root, "y1", 300.0, 299.5,
                                               "2022-07-25T00:00:00Z")
            doc = write_validation_report(results)
            self.assertIn("No validation metrics found", doc.read_text())

            (results / "results.json").write_text(json.dumps({"validation": {
                "source": "ERA5 test", "full": {"n": 2, "bias": -1.0, "mae": 0.5,
                                               "rmse": 2.0},
                "held_out_12_18Z": {"n": 1, "bias": -2.0, "mae": 0.7, "rmse": 3.0}}}))
            text = write_validation_report(results).read_text()
            self.assertIn("ERA5 test", text)
            self.assertIn("| Full | 2 | -1.000 | 0.500 | 2.000 |", text)
            self.assertIn("Held out 12–18Z", text)

    def test_baseline_only_studies_still_compare(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = self.study(root, "y1", 300.0, 299.5, "2022-07-25T00:00:00Z")
            b = self.study(root, "y2", 302.0, 301.0, "2023-07-25T00:00:00Z")
            for results in (a, b):
                (results / "zonal_scenario.csv").unlink()
            out = compare_years(a, b, root / "years")
            self.assertFalse((out / "effect_year_on_year.csv").exists())
            self.assertNotIn("effect_pairs", json.loads((out / "years.json").read_text()))


if __name__ == "__main__":
    unittest.main()
