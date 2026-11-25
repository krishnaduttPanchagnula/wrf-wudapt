# QGIS plugin target interface

The plugin will be a thin GUI over the headless engine in `src/`. It must not
contain WRF physics or ML logic itself.

## User inputs

- `year` / `date` (analysis window, e.g. 2022-07-25)
- `lat`, `lon` (domain centre)
- `radius_km` (circumference around the centre; sets the inner-domain extent)
- second `year` for comparison (reuses the same centre/radius and proposal)

## Contract

Implemented in `wrf_digital_twin/engine.py` (the QGIS plugin only serialises JSON):

```
CaseRequest(lat, lon, radius_km, start, hours, lcz_tif=None)
prepare_case(request, case_dir) -> case_dir          # GFS + WPS + real.exe
run_baseline(case_dir) -> case_dir                   # wrf.exe
apply_scenario(case_dir, proposal, out_dir) -> out_dir
compare_cases(baseline_dir, scenario_dir, out_dir)   # CSVs + QGIS layers
run_study(request, proposal, root) -> study_dir      # the four steps above
compare_years(first_results, second_results, out_dir) # LCZ/hour tables + years.json
write_comparison_report(results_dir, out_dir=None) -> html_path
write_validation_report(results_dir, out_dir=None) -> md_path
warm_case(case_dir, out_dir, delta_t_k) -> out_dir      # PGW initial/boundary T offset
apply_future_climate(case_dir, scenario, out_dir) -> out_dir
```

`study_dir = root / twin_<lat>_<lon>_<start>`; its `results/` is what
`compare_years` takes. Years are aligned on month-day and hour. The baseline
T2 difference is always exported; `effect_year_on_year.csv` is exported only
when both years have a counterfactual, and compares scenario − baseline per
year so weather differences are not read as intervention effects.

`scripts/twin.py` exposes each step, a `run` command that chains them,
`run-years` (two requests + one proposal), `compare-years` (two existing
result sets, no WRF), `future` (PGW-warmed case from a supplied `delta_T_K`)
and `report` (re-render the side-by-side page, `VALIDATION.md` and GeoTIFF).
`compare-years` makes a second-year analysis possible when only one extra
study can be afforded. `compare` writes `base_proposal_difference.html` with
base / proposal / ΔT2 per LCZ and hour, plus validation metrics from
`results.json` when present, and `delta_t2.tif` (EPSG:4326). The PGW offset is
applied to initial and boundary temperature fields and checked for effect;
no CMIP6 data is bundled. `zonal_stats` adds a `UTCI` column from
`src/heat_index.py` (official polynomial, support-checked; MRT approximated
from WRF radiation). PET is out of scope without a physiological model.
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
