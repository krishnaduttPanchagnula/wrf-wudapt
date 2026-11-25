# Weather Digital Twin (wrf-wudapt)

Imagine you can ask: **"If we replace the concrete in this part of the city with
grass, how much will the air temperature change?"** This project answers that
question by running a real weather model twice: once for the city as it is, and
once with your proposed change. It then gives you maps and tables of the
difference, so planners and GIS analysts can compare options before building
anything.

It is a research tool, not a crystal ball. Results depend on the date, weather
and the changes you choose, and every run takes time (about 1–2 hours for an
18-hour simulation on a normal laptop).

## Quick start (no programming needed)

You need a Linux computer with **Podman** installed and this project folder
checked out. The weather model itself is already prepared inside a container.

1. Install the desktop app:
   ```bash
   pip install wrf-digital-twin
   ```
2. Start it with `wrf-twin-gui` (or run `python -m wrf_digital_twin.gui` from
   this folder).
3. Type a latitude, longitude, radius in kilometres, a UTC start date/time and
   how many hours to simulate (must be 6, 12, 18...).
4. Click **1. Baseline** to create the "current city" simulation.
5. Choose which land-use class to replace (13 = built-up area) and what to put
   in its place (10 = grassland), then click **2. Proposal + compare**.
6. The app writes maps and CSV tables into the output folder. Open
   `output/results/REPORT.md` for the numbers, or
   `output/results/base_proposal_difference.html` for a base / proposal /
   difference table hour by hour.

If you use **QGIS**, install the plugin from `qgis_plugin/` instead: it gives
you a brush to draw the proposal area directly on the map. See
`qgis_plugin/README.md`.

A `pip`-installed app still needs this project folder (with the prepared WRF
container and data). Set **Project folder** in the app to that location, or set
the environment variable `WRF_TWIN_ROOT`.

**What you can change today:** the share of built-up land in a circular area
(land use class 13 → 10 by default). Other variables need a new intervention in
the engine.

**Please remember:** the weather data is public GFS archive data from 2021
onwards; the LCZ map covers Europe only; each proposal is a full new weather
simulation; and the accuracy check uses ERA5 reanalysis, not a real weather
station. Keep the report next to any map you share.

## What the desktop app looks like

`wrf-twin-gui` opens a small window (icon: ![app icon](wrf_digital_twin/icons/app.png)).
The mockup below shows the layout — it is a guide, not a screenshot:

```
┌──────────────────────────────────────────────────────────┐
│  Weather Digital Twin 0.1.0                    _  □  ×  │
├──────────────────────────────────────────────────────────┤
│  Project folder        [/home/you/wrf-wudapt]  [Browse]  │
│  Latitude              [45.4937         ]                │
│  Longitude             [9.16646         ]                │
│  Radius (km)           [25              ]                │
│  Start (UTC)           [2022-07-25T00:00:00Z]            │
│  Second start (UTC)    [2023-07-25T00:00:00Z]            │
│  Hours (multiple of 6) [6               ]                │
│  Replace land-use class [13 (built-up)  ]                │
│  With land-use class    [10 (grassland) ]                │
│  Fraction replaced      [0.8            ]                │
│  Output folder          [output         ]    [Browse]    │
│                                                          │
│  [ Run full study ] [ 1. Baseline ] [ 2. Proposal+compare ]│
│  [ 3. Compare years ]                                     │
│                                                          │
│  Engine output                                           │
│  ┌────────────────────────────────────────────────────┐  │
│  │ $ python -m wrf_digital_twin.cli prepare ...       │  │
│  │ prepared /home/you/wrf-wudapt/output/baseline      │  │
│  │ --- done ---                                        │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

The log pane fills while the weather model runs; buttons are disabled until it
finishes. Results are written to the output folder, not displayed inside the
window — open `output/results/REPORT.md` for the numbers and load the CSVs into
QGIS or a spreadsheet.

## What the QGIS plugin looks like

The plugin adds a toolbar button (icon: ![plugin icon](qgis_plugin/digital_twin/icon.png))
called **Weather Digital Twin**. Clicking it opens a panel with the same fields
as the desktop app, plus a **Brush: pick area on map** button:

```
┌──────────────────────── QGIS ────────────────────────────┐
│ [🌐 Weather Digital Twin]  [other tools...]             │
├───────────────┬──────────────────────────────────────────┤
│ Layers        │  Map canvas                              │
│ • ΔT2 points  │      ╭──────────╮                        │
│ • ΔT2 by class│      │  ● MILAN │  ← red circle =        │
│ • LCZ map     │      ╰──────────╯    selected proposal   │
│               │                                          │
│  ┌──────────────────────────────────────────┐            │
│  │ Weather Digital Twin                    │            │
│  │ Latitude  [45.4937] Longitude [9.16646] │            │
│  │ Radius    [10 km]  Start [2022-07-25Z]  │            │
│  │ Second year [2023-07-25Z]               │            │
│  │ From class [13] → To [10] Fraction [0.8]│            │
│  │ [Brush: pick area on map]               │            │
│  │ [1. Generate baseline] [2. Apply+compare]│           │
│  │ [3. Compare years]                      │            │
│  │ [4. Load results into QGIS]             │            │
│  └──────────────────────────────────────────┘            │
└───────────────┴──────────────────────────────────────────┘
```

After step 3, the `ΔT2 per grid cell` layer appears on the map (negative values
= cooling) and the `ΔT2 by land-use class` table can be opened from the Layers
panel. The brush circle is drawn from the radius field; clicking elsewhere on
the map moves the proposal centre.

## Technical details

This is a rebuild of *Urban Climate Modelling Using WRF and WUDAPT Model: A
Case of Milan* (Panchagnula Krishna Dutt, Politecnico di Milano, 2020), fixing
the validity problems found in Chapter 4. Everything runs inside a Podman
container; the project directory is bind-mounted at `/work`.

## Case definition (changed from the thesis)

- Thesis: 31 Jul – 1 Aug 2020, NCEP FNL 0.25°.
- Here: **25 Jul 2022, 00–18 UTC** (6 h spin-up, 12 h analysis). Reason: FNL 2020
  is no longer publicly downloadable without a UCAR/GDEX account; GFS 0.25°
  `f000` files for 2022 are public on AWS S3 and contain soil fields (`.anl`
  files do not).
- `shortcut: 18 h window instead of a full season; upgrade when compute allows.
  A two-day run here takes ~6 h of wall time at 3 km with BEP.`
- Domain centre: 45.4937 N, 9.16646 E (Milan). Nested 9 km / 3 km.

## What changes from the thesis

| Thesis (Ch. 4) | Here |
|---|---|
| WRF with default land use; BEP selected but no urban parameters | LCZ-derived urban extent injected into `geo_em` via `w2w` (BEP active) |
| LCZ map used only as a post-hoc averaging mask | LCZ drives the urban extent in WRF *and* the sampling |
| — | `shortcut: WRF's 41-category LCZ mode needs a source rebuild (`NLUS=61`) and a custom `VEGPARM.TBL`; until then WRF uses default urban morphology. Logged as "USING DEFAULT URBAN MORPHOLOGY" in `wrf.log`.` |
| "Ground truth" = interpolated Dati Lombardia grid | Independent ERA5 point series (GFS vs ERA5 are different analyses); bias/RMSE reported |
| Predictors chosen by >80% correlation with the same output | Features chosen physically; circular variables excluded |
| One run, then ±20/30% LAI into a regression → "cooling" | Counterfactual WRF runs with perturbed land surface |
| "82% accuracy", undefined | RMSE/MAE/R² on LCZ-blocked folds; prediction intervals |
| Gaussian-kernel equation labelled KNN, mis-typed | Explicit, tested model with monotonic constraints and support checks |

## Plugin interface (framework built; see `qgis_plugin/`)

A QGIS plugin will let a user enter a date/year, a lat/lon and a radius, run the
whole engine, and **compare two years**. The engine therefore stays headless
and importable: `src/` functions take plain config/arrays and return tables.
A plugin is a thin front-end that orchestrates WRF locally or against a service;
it cannot run WRF itself.

## Layout

```
Containerfile, run.sh   container image + build/shell/run helpers
config/sources.yaml     verified URLs, checksums to be filled, licenses, caveats
config/namelist.*       corrected WPS/WRF settings
src/acquire.py          no-credential downloads + sha256 manifest
src/emulator.py         physics-constrained ML with LCZ-blocked validation
src/lcz.py, src/wrfio.py, src/pipeline.py   remaining pipeline (in progress)
tests/                  self-checks
data/raw|interim|processed, output/
```

## Workflow

```bash
./run.sh build                       # build image (once)
./run.sh run 'python src/acquire.py' # download LCZ, geography, GFS, validation data
./run.sh shell                       # interactive work inside container
```

## Weather digital-twin framework

`wrf_digital_twin/engine.py` turns a `(lat, lon, radius, date/time)` request into a WRF
case and a land-use proposal into a counterfactual run. `scripts/twin.py` is its
CLI; `qgis_plugin/digital_twin/` is a thin QGIS front-end (brush area selection,
request/proposal forms, result layers). See `qgis_plugin/README.md`.

```bash
./run.sh run 'python scripts/twin.py run /work/config/twin_request.example.json \
  /work/config/twin_proposal.example.json'
```

**Second-year comparison.** Run the same centre, radius and proposal with a
second start date, then compare the two result sets. This costs another full
WRF run, so the comparison can be done later from cached results:

```bash
./run.sh run 'python scripts/twin.py run-years \
  /work/config/twin_request.example.json /work/config/twin_request_2.example.json \
  /work/config/twin_proposal.example.json'

# after running the second year on its own instead:
./run.sh run 'python scripts/twin.py compare-years \
  /work/output/twin_45.4937_9.1665_20220725T00/results \
  /work/output/twin_45.4937_9.1665_20230725T00/results \
  --out /work/output/years'
```

`base_proposal_difference.html` is written by every `compare` run (and can be
regenerated with `wrf-twin report <results-dir>`). It shows base, proposal and
difference side by side for each LCZ and hour; validation metrics are embedded
when `results.json` has them, otherwise the page says so instead of presenting
an unchecked result. The same run writes `VALIDATION.md`: bias/MAE/RMSE for the
full and held-out windows, emulator skill and provenance hashes, or an explicit
"not validated" note when `results.json` is absent. It also exports
`delta_t2.tif` (EPSG:4326) for QGIS or any GIS that reads GeoTIFF. Zonal CSVs
also carry `UTCI` (degrees C) beside T2, computed from the official
Broede a0.002 polynomial with its wind/radiation support limits enforced;
mean radiant temperature is estimated from WRF radiation fluxes, so treat it
as an approximation, not a globe-thermometer measurement. PET is not
implemented: it needs a separate physiological model and reference data.

`output/years/baseline_year_on_year.csv` is the weather difference between
years (LCZ × calendar day × hour). `effect_year_on_year.csv`, written when both
years have a counterfactual, is the *change in cooling effect* (scenario −
baseline) — that is the number to use for a claim about the proposal, not the
baseline difference. `years.json` records both start dates. The desktop app
and QGIS plugin have a **Compare years** button for the same workflow.

**Longer windows.** `hours` can be any multiple of 6, so 72 (three days) or
168 (a week) works with the same engine; `config/twin_request_multiday.example.json`
is a 72 h example. Cost and GFS downloads grow with the window — the 18 h case
is the tested default, not a hard limit.

**Future climate (supplied scenario).** With a CMIP6-derived temperature offset
you can run a warmed case through the same WRF physics:
`wrf-twin future <case> config/future_ssp245.example.json --out <dir>`, then
`wrf-twin compare <case> <dir> --out <results>`. This is a pseudo-global-warming
perturbation of WRF's initial and boundary temperature fields; the offset and
its source/retrieval date must be filled in by the user — no CMIP6 data is
bundled, and a plain temperature offset is not a full AR6 ensemble.

Hours must be a multiple of 6 (GFS boundary data is 6-hourly). Each proposal
costs one full WRF run; the engine reuses the shared `src/WPS` and `src/WRF/run`
directories, so a running experiment should be finished before starting a twin
case. Only `LANDUSEF` is editable today; other variables need a new intervention
in `apply_scenario`. Validation metrics are not yet attached to QGIS layers.

## Installing and releasing the app

```bash
pip install wrf-digital-twin     # from PyPI
wrf-twin-gui                     # desktop app
wrf-twin --help                  # command line
```

To publish: push a tag such as `v0.1.0`. `.github/workflows/release.yml`
creates the GitHub release, and `.github/workflows/publish.yml` then builds the
wheel/sdist and publishes it to PyPI with trusted publishing (no API token
stored). `.github/workflows/test.yml` runs engine checks on Python 3.10–3.12.

Before the first tag, configure a trusted publisher on PyPI for this repository
(owner `krishnaduttPanchagnula`, repo `wrf-wudapt`, workflow `publish.yml`).

## Status

- [x] Container image (Podman), WRF v4.6.1 + WPS v4.6.0 compiled, w2w working
- [x] Data acquisition: LCZ, geography, 16 × GFS f000 (soil-bearing), ERA5 validation
- [x] LCZ-derived urban extent injected via w2w; corrected WPS/WRF namelists
- [x] Full 18 h baseline WRF run, 19 hourly frames, classic NetCDF output
- [x] Counterfactual WRF run (80% urban land use → grassland in LCZ 1–10), LCZ-wise differencing
- [x] Emulator with LCZ- and time-blocked validation, prediction intervals, support checks
- [x] Digital-twin engine, desktop app, QGIS plugin and icons (GUI smoke-tested; QGIS UI untested here)
- [x] PyPI/GitHub release workflows
- [x] Hourly base / proposal / difference HTML report + `VALIDATION.md` artefact
- [x] Second-year comparison — engine, CLI, desktop app and QGIS button; second-year WRF run not executed here (compute/time)

Results: `output/results/REPORT.md`, `results.json`, `zonal_*.csv`, `compare_lu80.csv`.
ERA5 point validation: bias -2.46 K, RMSE 3.12 K (n=19; held-out 12–18Z RMSE 3.44 K).
Built LCZ response to the land-use intervention: mean ΔT2 -0.093 K (5 of 6 classes cool).

Finding: perturbing `LAI` in `wrfinput` had **zero** effect on T2 — Noah recomputes
LAI from land cover. The effective intervention is `LANDUSEF`, which WRF actually uses.

See `CONSTRAINTS.md` for the quality bar that must not be lowered.
