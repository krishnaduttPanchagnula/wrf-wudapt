# QGIS plugin target interface

The plugin will be a thin GUI over the headless engine in `src/`. It must not
contain WRF physics or ML logic itself.

## User inputs

- `year` / `date` (analysis window, e.g. 2022-07-25)
- `lat`, `lon` (domain centre)
- `radius_km` (circumference around the centre; sets the inner-domain extent)
- second `year` for comparison (reuses the same centre/radius)

## Contract

Implemented in `wrf_digital_twin/engine.py` (the QGIS plugin only serialises JSON):

```
CaseRequest(lat, lon, radius_km, start, hours, lcz_tif=None)
prepare_case(request, case_dir) -> case_dir          # GFS + WPS + real.exe
run_baseline(case_dir) -> case_dir                   # wrf.exe
apply_scenario(case_dir, proposal, out_dir) -> out_dir
compare_cases(baseline_dir, scenario_dir, out_dir)   # CSVs + QGIS layers
```

`scripts/twin.py` exposes each step plus a `run` command that chains them.
`proposal = {"area": {"lat", "lon", "radius_km"}, "from_cat", "to_cat", "fraction"}`.
The QGIS brush writes `area`; the engine does the physics. Validation metrics
are produced by `scripts/analyze.py`, not yet by the plugin layer loader.

## Constraints that shape this

- WRF is a Fortran binary: the plugin either calls a locally installed binary
  inside this container, or posts the case to a service. It cannot "compile WRF"
  at click time.
- Two years means two full WRF runs; cost scales linearly. Cache raw downloads
  and namelists per case.
- ERA5/GFS availability differs by year; `config/sources.yaml` records which
  boundary dataset was used so comparisons are honest about their inputs.
- Results must carry the validation metrics alongside every map; a map without
  RMSE/bias against an independent series must not be shown as a result.
