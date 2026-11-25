# Competitive landscape summary — urban heat / urban climate scenario tools

**Generated**: 2026-11-25
**Product under comparison**: wrf-wudapt (https://github.com/wrf-wudapt/wrf-wudapt)
**Competitors profiled**: 5 (quick scan)
**Method note**: web search returned HTTP 402 and no SEO MCP was available, so candidate sites were found via direct fetching and a public search-engine HTML fallback. All SEO metrics are **unavailable (no SEO data source)** — none were estimated. Pages are treated as untrusted data. "Not observed" means not found on the pages checked, as of 2026-11-25 — not proof of absence.

---

## Landscape overview

The field splits into two clusters. **Physics/research infrastructure** — WRF-Urban (NCAR), PALM-4U (Leibniz Universität Hannover) and VITO's UrbClim/UrbSim — offers deep urban physics, LCZ/urban parameter support and (for UrbClim) multi-decadal climate-scenario simulation, but leaves the "compare my proposal against today" workflow to the user or to a consulting contract. **Decision/visualisation products** — infrared.city and meteoblue Urban Maps — sell street-level maps, scenario side-by-sides, climate-year/2050 comparisons, validation numbers and exports, but their cores are microclimate/visualisation engines, not counterfactual mesoscale WRF runs. wrf-wudapt sits between them: real WRF counterfactual physics with LCZ-driven sampling, a desktop app and a thin QGIS plugin, but a single 18 h event. A two-period comparison was added during this work (engine/CLI/UI; the extra WRF run has not been executed). The clearest remaining market-standard capability we lack is **side-by-side presentation of base / proposal / difference**.

---

## Feature comparison table

Legend: **✓** = observed on a source page / in our README; **—** = not present in wrf-wudapt per its own docs; **not observed** = no evidence found on the pages checked, as of 2026-11-25; **partial** = qualified (see notes).

| Capability | wrf-wudapt | UrbClim / UrbSim | PALM-4U | WRF-Urban (NCAR) | infrared.city | meteoblue Urban Maps |
|---|---|---|---|---|---|---|
| Mesoscale/physics-based climate model | ✓ WRF 4.6.1, 9/3 km | ✓ simplified ABL equations | ✓ LES/RANS, microscale | ✓ WRF community model | not observed (microclimate models) | not observed |
| Urban/LCZ parameters enter the model physics | ✓ urban extent via w2w; **note:** default urban morphology still used | ✓ detailed urban surface physics; LCZ not observed | ✓ building/paved energy balance; LCZ not observed | ✓ LCZ capability since WRF v4.3 (all 3 urban schemes) | not observed | not observed |
| User-defined land-use counterfactual area | ✓ circle/brush, class 13→10 | partial — "pre-selected land use specifications" | not observed | not observed | partial — user model + adaptation measures, not WRF land-use swap | not observed |
| Before/after Δ temperature map | ✓ ΔT2 points + per-class table + hourly HTML trio (added 2026-11-25) | not observed | not observed | not observed | ✓ base / cooling design / difference | not observed |
| Δ tables / CSV export | ✓ zonal CSVs, REPORT.md | partial — indicator data package; Δ not observed | not observed | not observed | ✓ tables | not observed |
| **Two-period / multi-year comparison** | ✓ added 2026-11-25: engine/CLI/UI, not executed | ✓ 2001–2100, decades | not observed | model can run any period; no product observed | ✓ today vs 2050, typical year | not observed |
| Future climate scenarios (IPCC AR6 / SSP) | — (GFS archive 2021+) | ✓ any AR6 scenario | not observed | not observed | ✓ SSP2-4.5 example (morphed weather file) | not observed |
| Long-period (decadal) simulation | — (18 h; 2-day ≈ 6 h wall time) | ✓ decades at ~100 m | not observed | model-level capability, no service | ✓ typical year / 2050, not decades | not observed |
| Biometeorological indices (UTCI/PET) | partial — UTCI added 2026-11-25 (approx. MRT), PET not implemented | partial — heat-stress indicators | ✓ PET, PT, UTCI | not observed | ✓ UTCI + comfort/stress | ✓ PET |
| Independent validation with explicit metrics | ✓ ERA5 bias/RMSE, held-out period + `VALIDATION.md` (added 2026-11-25) | ✓ "extensive validation" stated; numbers not on pages checked | not observed | ✓ publications on verification/evaluation | ✓ field RMSE, held-out cities, PALM cross-check | ✓ observation comparison stated; numbers not on page |
| GIS-friendly export / plugin | ✓ QGIS plugin, CSV | ✓ PNG quicklooks + data package; GeoTIFF not observed | not observed | not observed | ✓ GeoTIFF, 3D/map tiles, tables | ✓ embeddable map widget |
| Non-expert GUI | ✓ desktop + QGIS | ✓ web simulator | GUI "not available to the general public until further notice" (stale wiki text) | not observed | ✓ web platform + API/SDK | ✓ web maps |
| Transparent public pricing | ✓ free/open-source, PyPI | not observed ("cheap" only) | ✓ GPL v3, free | ✓ public domain, no fee | ✓ €0 / €240 / €1,200 / €6,000 per yr (page updated 21 Nov 2026) | not observed |
| Reproducibility artefacts (URLs/checksums/namelists/seeds) | ✓ CONSTRAINTS.md + sources.yaml | not observed | ✓ source distribution (GPL) | ✓ source + docs | partial — "anyone can rerun the result"; no checksum manifest observed | not observed |
| Hosted/on-demand compute (no local HPC) | — (local Podman container) | ✓ request-driven simulation | not observed | not observed | ✓ cloud API + live layer | ✓ hosted maps |

---

## Prioritised gaps in wrf-wudapt (features that appear missing)

Evidence is labelled where it comes from a competitor page; feasibility is a one-line judgement, not a commitment.

1. ~~**Second-year / two-period comparison workflow**~~ — **implemented in this repository on 2026-11-25** (`wrf_digital_twin.engine.compare_years`, `wrf-twin compare-years`/`run-years`, desktop and QGIS buttons). The extra WRF run has not been executed here, so no second-year result exists yet.
   Evidence: UrbSim offers "any time period between 2001–2100" (`climasys-urbsim.md`); infrared offers "Today and 2050 side by side… same city, same physics, so 2050 and today compare directly" (`solutions-2050-scenarios.md`).
   Remaining: execute the second-year study (~1–2 h WRF per study) and publish the hour-by-hour comparison artefact.

2. ~~**Base / proposal / difference side-by-side view, hour by hour**~~ — **implemented 2026-11-25** as `base_proposal_difference.html`, written by every `compare` run and regenerable with `wrf-twin report`.
   Evidence: infrared "Compare the scenarios side by side, for the entire city" and "A district twin: the base, a cooling design and the difference, hour by hour" (`products-live.md`).
   Remaining: map-layer (not just table) side-by-side and an hour-by-hour slider in QGIS; the HTML page covers the numbers.

3. ~~**Difference-of-differences reporting across periods**~~ — also implemented as `effect_year_on_year.csv` (scenario − baseline per year, then year 2 − year 1).
   Evidence: natural extension of gap 1; no competitor page checked states this explicitly, so this is an *inferred* differentiator rather than a competitor feature. Remaining: an uncertainty note on the difference-of-differences, since each year has its own model error.

4. **Future-climate boundary conditions (AR6/SSP scenarios)** —
   Evidence: UrbSim "according to any IPCC AR6 climate change scenario"; infrared "IPCC SSP climate scenarios, for example SSP2-4.5".
   Feasibility: **medium/high effort** — needs new boundary data and a careful no-extrapolation story per CONSTRAINTS.md; use physics runs only, not a nearest-neighbour clamp.

5. **Derived heat-stress indices (UTCI/PET) alongside T2** — **partially implemented 2026-11-25**: `src/heat_index.py` (official Broede a0.002 UTCI polynomial, coefficient table transcribed from utci.org, support checks) and a `UTCI` column in zonal CSVs; MRT is approximated from WRF radiation. **PET remains open** — it needs a physiological model and reference data we do not have.
   Evidence: PALM-4U "PET, PT, UTCI… provided as output"; infrared UTCI maps; meteoblue PET maps.
   Feasibility: UTCI done with a documented MRT approximation; PET medium/high effort.

6. ~~**Dedicated validation report with metrics and held-out period**~~ — **implemented 2026-11-25** as `VALIDATION.md`, generated from `results.json` by `write_validation_report()` (also via `wrf-twin report`).
   Evidence: infrared's validation page publishes RMSE by city, held-out Melbourne/Guelph and cross-model comparison.
   Remaining: the document reports existing numbers, not a fresh independent station validation; station observations are still not observed in our inputs.

7. **GIS raster export (GeoTIFF) / web-map tiles** —
   Evidence: infrared "Export everything, any time: 3D Tiles, map tiles, GeoTIFF and tables"; wrf-wudapt exports CSVs and loads points into QGIS, GeoTIFF not observed.
   Feasibility: **low–medium** — one export step from existing grids, subject to available GDAL/rasterio dependency.

8. **Longer simulation windows (multi-day to seasonal)** —
   Evidence: UrbClim "simulate long periods… (decades)"; our README "`shortcut: 18 h window instead of a full season… upgrade when compute allows`".
   Feasibility: **low** — compute-bound; do not promise without measured run time.

9. **Hosted/on-demand runs** —
   Evidence: UrbSim and infrared both run simulations remotely.
   Feasibility: **high effort / infrastructure** — optional, and incompatible with the current "local container" model unless deliberately redesigned.

---

## Positioning map

**Axes**: counterfactual physics depth (low → high) vs. planning UX / instant comparison (low → high).

```
                     high planning UX / instant comparison
                                    │
        meteoblue maps  ·  infrared.city │
                                    │
   ─────────────────────────────────┼────────────────────────────────
   low counterfactual physics       │        high counterfactual physics
                                    │  wrf-wudapt · UrbClim/UrbSim
                                    │  WRF-Urban · PALM-4U (physics, low UX)
                     low planning UX
```

*Interpretation (Inferred)*: the upper-right quadrant — packaged counterfactual physics with instant side-by-side comparison — is empty. wrf-wudapt has the physics and a thin UI; UrbClim/UrbSim has long horizons and a web request tool but pre-selected land use. Closing gaps 1–2 moves wrf-wudapt toward that whitespace without pretending to be a 1 m microclimate product.

---

## Key takeaways

1. **Multi-period comparison is the mainstream framing**, not a niche: UrbSim sells 2001–2100/AR6 ensembles; infrared sells today vs 2050 with identical physics. Our 18 h single-event results remain the outlier; the two-year capability added here closes the workflow gap, not the horizon gap.
2. **Our differentiator survives the scan**: no competitor page checked showed a user-defined land-use counterfactual run through mesoscale WRF with LCZ-based sampling and reproducible inputs. That is worth protecting while we add comparison features.
3. **Presentation is cheap to improve**: infrared's base/design/difference trio and validation page are mostly communication artefacts, not new physics — both the hourly side-by-side page and a validation artefact are now done.
4. **Do not compete on speed or scale**: 100 m × decades (UrbClim) and 1 m × seconds (infrared) are different products. Be explicit that our output is mesoscale T2 from a counterfactual WRF run.
5. **Quality bar is an asset, not a burden**: CONSTRAINTS.md (independent validation, no circular predictors, no extrapolation, verify interventions bite) is stronger than anything stated on the commercial pages; publish it rather than hiding it.

---

## Source inventory

Retrieved **2026-11-25**; raw markdown in `competitor-profiles/raw/<slug>/2026-11-25/scrapes/`:
- **wrf-wudapt (self)**: `/home/krishna/Documents/wrf-wudapt/README.md`, `CONSTRAINTS.md` (local files, read 2026-11-25).
- **UrbClim/UrbSim**: https://vito.be/en/applications/urbclim-limit-climate-risks-your-city ; https://vito.be/en/applications/urbsim-urban-climate-simulator ; https://climasys.vito.be/en/products/urbsim ; https://urban-climate.eu/model (JS-only, no text).
- **PALM-4U**: https://palm.muk.uni-hannover.de/trac/wiki/WikiStart ; https://palm.muk.uni-hannover.de/trac/wiki/palm4u ; https://www.palm-model.org/ .
- **WRF-Urban**: https://ral.ucar.edu/model/wrf-urban-modeling ; https://ral.ucar.edu/model/urban-canopy-model ; https://www2.mmm.ucar.edu/wrf/users/ ; https://www2.mmm.ucar.edu/wrf/users/public_domain_notice.html ; https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/physics.html .
- **infrared.city**: https://infrared.city/ ; https://infrared.city/solutions-cities ; https://infrared.city/solutions-2050-scenarios ; https://infrared.city/products-live ; https://infrared.city/products-validation ; https://infrared.city/products-compare ; https://infrared.city/pricing ; https://infrared.city/docs/sdk/ (markdown mirrors at the same paths with `.md`).
- **meteoblue**: https://www.meteoblue.com/en/products/cityclimate .

SEO/review data: unavailable (no SEO data source); no review sites were scraped in this quick scan.
