# Weather Digital Twin — QGIS plugin

Thin GUI over the headless engine in `wrf_digital_twin/engine.py`. The plugin contains
no WRF physics: it writes a request/proposal JSON, calls the engine through the
existing Podman container, and loads the result layers into QGIS.

## Install

Copy `digital_twin/` into your QGIS Python plugins directory, e.g.
`~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/digital_twin/`, then
enable **Weather Digital Twin** in *Plugins → Manage and Install Plugins*.
QGIS 3.22+ with PyQt5 is assumed. `PySide2` is also accepted.

The engine requires the project checkout with `./run.sh` working (Podman image
already built). Set **Project root** in the dialog to that directory.

## Use

1. Enter centre latitude/longitude, radius, UTC start time and run length.
   Click **Brush: pick area on map** and click the map to move the centre; the
   red circle shows the proposal extent (radius from the dialog).
2. **Generate baseline case + run** — downloads 6-hourly GFS `f000` files for
   the window, builds WPS/WRF namelists, runs geogrid/w2w/ungrib/metgrid/real
   and WRF. Progress appears in the log pane.
3. Choose the land-use class to replace (default 13 = urban) and the class to
   convert to (default 10 = grassland), plus the fraction replaced.
   **Apply proposal + compare** re-runs WRF from the perturbed initial state
   and writes the comparison tables.
4. Enter a **Second start** date and click **Compare years** to run the same
   proposal in the second year and write `output/years/`. This costs one more
   full WRF run; you can run the second year later and only then compare.
5. **Load results into QGIS** adds three side-by-side layers — base T2,
   proposal T2 and ΔT2 per grid cell — plus `delta_by_landuse.csv`. The same results folder also
   contains `base_proposal_difference.html`: base, proposal and ΔT2 side by
   side for each LCZ and hour, with validation metrics when available, and
   `VALIDATION.md` with the full/held-out scores and provenance.

Outputs are under `<project root>/output/twin_<lat>_<lon>_<date>/` when using
the CLI `run` command, or `output/twin_baseline`, `output/twin_scenario` and
`output/twin_results` when using the plugin buttons.

## Headless CLI (same engine)

```bash
./run.sh run 'python scripts/twin.py run /work/request.json /work/proposal.json'
```

`request.json`: `{"lat":45.4937,"lon":9.16646,"radius_km":50,
"start":"2022-07-25T00:00:00Z","hours":18}`

`proposal.json`: `{"area":{"lat":45.4937,"lon":9.16646,"radius_km":10},
"from_cat":13,"to_cat":10,"fraction":0.8}`

`python scripts/twin.py --help` lists the individual `prepare`, `baseline`,
`scenario` and `compare` steps, plus `run-years` (two requests) and
`compare-years` (two existing results dirs, no WRF). The latter writes
`baseline_year_on_year.csv`, optionally `effect_year_on_year.csv` (change in
cooling, not just weather) and `years.json` with both start dates.

## Limits (current framework)

- GFS f000 is public from 2021-01-01; earlier dates need credentials (see
  `config/sources.yaml`). Global low-resolution geography is used; the LCZ map
  currently covers Europe only, so elsewhere the classes are MODIS land use.
- Only `LANDUSEF` (land-use fractions) is editable. Other variables need a new
  intervention in `wrf_digital_twin.engine.apply_scenario` plus a fresh WRF run.
- Each proposal costs one full WRF run (~1–2 h for 18 h at 3 km). The plugin
  calls the engine locally; a remote service would need the same JSON contract.
- Validation metrics are NOT yet attached to the plugin layers. Load the
  experiment's `output/results/REPORT.md` alongside any map; a map without
  bias/RMSE against an independent series is not a result (see `CONSTRAINTS.md`).
