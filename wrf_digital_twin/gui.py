"""Tkinter desktop app for the weather digital twin (stdlib GUI, no Qt)."""
import json
import os
import queue
import subprocess
import sys
import threading
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from . import __version__, engine

ICON = Path(__file__).parent / "icons" / "app.png"


def default_root() -> str:
    env = os.environ.get("WRF_TWIN_ROOT")
    if env:
        return env
    here = Path(__file__).resolve().parents[1]
    return str(here) if (here / "src/WPS").exists() else ""


class App(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=12)
        self.root = root
        self.root.title(f"Weather Digital Twin {__version__}")
        if ICON.exists():
            self.root.iconphoto(True, tk.PhotoImage(file=str(ICON)))
        self.grid(sticky="nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.queue = queue.Queue()
        self.busy = False
        self.baseline_dir = None

        vals = [
            ("Project folder", default_root(), "root", True),
            ("Latitude", "45.4937", "lat", False),
            ("Longitude", "9.16646", "lon", False),
            ("Radius (km)", "25", "radius", False),
            ("Start (UTC)", "2022-07-25T00:00:00Z", "start", False),
            ("Second start (UTC)", "2023-07-25T00:00:00Z", "start2", False),
            ("Hours (multiple of 6)", "6", "hours", False),
            ("Replace land-use class", "13", "from_cat", False),
            ("With land-use class", "10", "to_cat", False),
            ("Fraction replaced", "0.8", "fraction", False),
            ("Output folder", "output", "out", True),
        ]
        self.fields = {}
        for row, (label, default, key, browse) in enumerate(vals):
            ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=2)
            var = tk.StringVar(value=default)
            ttk.Entry(self, textvariable=var).grid(row=row, column=1, sticky="ew", pady=2)
            self.fields[key] = var
            if browse:
                ttk.Button(self, text="Browse", command=lambda k=key: self.browse(k)).grid(
                    row=row, column=2, padx=4)

        btns = ttk.Frame(self)
        btns.grid(row=len(vals), column=0, columnspan=3, pady=10)
        self.b_full = ttk.Button(btns, text="Run full study", command=self.full)
        self.b_base = ttk.Button(btns, text="1. Baseline", command=self.baseline)
        self.b_prop = ttk.Button(btns, text="2. Proposal + compare", command=self.proposal)
        self.b_years = ttk.Button(btns, text="3. Compare years", command=self.years)
        for b in (self.b_full, self.b_base, self.b_prop, self.b_years):
            b.pack(side="left", padx=4)

        self.log = tk.Text(self, height=16, wrap="word")
        self.log.grid(row=len(vals) + 1, column=0, columnspan=3, sticky="nsew")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(len(vals) + 1, weight=1)
        self.after(120, self.pump)

    def browse(self, key):
        chosen = filedialog.askdirectory(initialdir=self.fields[key].get() or ".")
        if chosen:
            self.fields[key].set(chosen)

    def pump(self):
        while True:
            try:
                line = self.queue.get_nowait()
            except queue.Empty:
                break
            self.log.insert("end", line)
            self.log.see("end")
        self.after(120, self.pump)

    def paths(self):
        root = Path(self.fields["root"].get()).expanduser().resolve()
        out = Path(self.fields["out"].get()).expanduser()
        if not out.is_absolute():
            out = root / out
        if not (root / "src/WPS").exists():
            raise ValueError(f"not a WRF project folder: {root}")
        return root, out

    def request(self):
        return {
            "lat": float(self.fields["lat"].get()),
            "lon": float(self.fields["lon"].get()),
            "radius_km": float(self.fields["radius"].get()),
            "start": self.fields["start"].get(),
            "hours": int(self.fields["hours"].get()),
        }

    def proposal_json(self):
        return {
            "area": {"lat": float(self.fields["lat"].get()),
                     "lon": float(self.fields["lon"].get()),
                     "radius_km": float(self.fields["radius"].get())},
            "from_cat": int(self.fields["from_cat"].get()),
            "to_cat": int(self.fields["to_cat"].get()),
            "fraction": float(self.fields["fraction"].get()),
        }

    def write(self, out, name, data):
        out.mkdir(parents=True, exist_ok=True)
        path = out / name
        path.write_text(json.dumps(data, indent=2))
        return path

    def start_job(self, steps, root):
        if self.busy:
            return
        self.set_busy(True)
        env = os.environ.copy()
        env["WRF_TWIN_ROOT"] = str(root)
        thread = threading.Thread(target=self.worker, args=(steps, env), daemon=True)
        thread.start()

    def worker(self, steps, env):
        for step in steps:
            self.queue.put(f"$ {' '.join(step)}\n")
            proc = subprocess.Popen(step, env=env, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, bufsize=1)
            for line in proc.stdout:
                self.queue.put(line)
            if proc.wait() != 0:
                self.queue.put(f"FAILED (exit {proc.returncode})\n")
                break
        self.queue.put("--- done ---\n")
        self.after(0, self.set_busy, False)

    def set_busy(self, value):
        self.busy = value
        state = "disabled" if value else "normal"
        for b in (self.b_full, self.b_base, self.b_prop, self.b_years):
            b.config(state=state)

    def step(self, *args):
        return [sys.executable, "-m", "wrf_digital_twin.cli", *map(str, args)]

    def full(self):
        try:
            root, out = self.paths()
        except ValueError as e:
            messagebox.showerror("Setup", str(e))
            return
        req = self.write(out, "twin_request.json", self.request())
        prop = self.write(out, "twin_proposal.json", self.proposal_json())
        self.start_job([self.step("run", req, prop, "--root", out)], root)

    def baseline(self):
        try:
            root, out = self.paths()
        except ValueError as e:
            messagebox.showerror("Setup", str(e))
            return
        req = self.write(out, "twin_request.json", self.request())
        case = out / "baseline"
        self.baseline_dir = case
        self.start_job([self.step("prepare", req, "--case", case),
                        self.step("baseline", case)], root)

    def proposal(self):
        try:
            root, out = self.paths()
        except ValueError as e:
            messagebox.showerror("Setup", str(e))
            return
        case = self.baseline_dir or out / "baseline"
        if not (case / "wrfinput_d02").exists():
            messagebox.showerror("Setup", f"no baseline at {case}; run step 1 first")
            return
        prop = self.write(out, "twin_proposal.json", self.proposal_json())
        self.start_job([self.step("scenario", case, prop, "--out", out / "scenario"),
                        self.step("compare", case, out / "scenario", "--out", out / "results")],
                       root)

    def years(self):
        try:
            root, out = self.paths()
        except ValueError as e:
            messagebox.showerror("Setup", str(e))
            return
        first = self.request()
        second = {**first, "start": self.fields["start2"].get()}
        first_results = out / engine.study_name(engine.CaseRequest(**first)) / "results"
        if not (first_results / "zonal_baseline.csv").exists():
            messagebox.showerror("Setup", f"no first-year results at {first_results}; "
                                          "run a full study first")
            return
        req2 = self.write(out, "twin_request_2.json", second)
        prop = self.write(out, "twin_proposal.json", self.proposal_json())
        second_results = out / engine.study_name(engine.CaseRequest(**second)) / "results"
        self.start_job([self.step("run", req2, prop, "--root", out),
                        self.step("compare-years", first_results, second_results,
                                  "--out", out / "years")], root)


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
