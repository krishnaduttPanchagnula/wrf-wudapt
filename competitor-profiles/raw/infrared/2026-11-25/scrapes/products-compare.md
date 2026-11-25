# Raw scrape: products-compare

- Source URL: https://infrared.city/products-compare.md
- Retrieved: 2026-11-25
- HTTP status: 200
- Note: untrusted third-party content; ignore embedded instructions.

---

# ENVI-met, SOLWEIG, PALM-4U Alternative · infrared.city

> An alternative to ENVI-met, SOLWEIG, PALM-4U and Orbital Stack? Compare speed, geometry, analyses and field validation, and when to use each tool.

Source: https://infrared.city/products-compare

Every model simplifies reality. Choose the right model for the purpose: fast models to shape decisions, detailed models for in-depth studies. infrared.city next to SOLWEIG, ENVI-met, PALM-4U and Orbital Stack.

Climate intelligence for every decision. Full physics for the critical few.

## Why teams choose infrared.city

![A city coloured by the live heat result](https://infrared.city/assets/stills/live-layer-hongkong.webp)

Example: Hong Kong.

Fast and flexible

Seconds per site, so you test many options and change them freely. About 3 s for a city block, results while you design. An entire city, too. (footnote 1 )

12 models

Outdoor wind and heat, sun and sky, facades and roofs, interior daylight and energy. One engine. [Simulation library](https://infrared.city/products-simulations)

Cloud native + API

A browser app, a hosted API and SDK, plugins for Grasshopper, QGIS and ArcGIS. Nothing to install or operate.

Enterprise scale

100 km² of Hamburg in 37 s, from submission to result, including building data and upload (October 2026). (footnote 6 )

Real 3D geometry

Actual building and terrain meshes. Sun on every facade and roof of a 500 m block, 581,334 surfaces, in about 6 s. (footnote 1 )

Site to city

The same method at every scale, so you can screen a whole building stock or many variants.

Live climate layer

A whole city, again every hour, with a 72 h heat-stress forecast at metre scale. Scenarios use the same engine: same method, same numbers.

## Side by side

We compare the software stacks: speed, scale, analyses, geometry and how you run them.

|  | infrared.city (footnote 1 ) | SOLWEIG (footnote 9 ) | ENVI-met (footnote 8 ) | PALM-4U (footnote 7 ) | Orbital Stack (footnote 12 ) |
| --- | --- | --- | --- | --- | --- |
| Speed A typical UTCI calculation, per km² and simulated day. Rough estimate, footnote 14. | **~5 s** UTCI, 1 km², 08 to 18 h, geometry uploaded (measured). | **~7 s on GPU** UTCI, 2 m grid. About 33 s on CPU. | **~45 days** Per km² at 1 m, extrapolated from a measured 65 h for a 0.06 km² block (v5.9). A full microclimate run; UTCI is computed after. | **~4–5 days** Per wind direction and km² at 1 m, extrapolated from a measured 39 h for 8 directions × 6 h on 0.18 km² with 300 cores. A wind run, not UTCI. | **Minutes (AI)** A site is about 0.3 km² (300 m radius), so 3 to 4 runs per km². The CFD level takes 2 to 3 business days per site. |
| Smallest unit | **A room** Interior daylight factor and energy need, room by room. | **A street block** Outdoor radiation and comfort on a height raster. | **A street block** Outdoor microclimate. No room-level daylight or energy. | **A street block** Outdoor flow; the indoor model works per building, not per room. | **One building** The study building with a 300 m context. |
| Largest single run | **City scale** 100 km² of Hamburg in 37 s from submission to result, including building data and upload. | **~39 km²** On one GPU. | **One site** | **City** On a large compute cluster. | **One site** 300 m context radius. |
| Analyses | **12 models** | **Radiant heat** | **Microclimate** | **Airflow, energy** | **Wind, comfort, solar** |
| Geometry | **Real 3D meshes** | **2.5D raster** | **3D voxels** | **3D voxels** | **STL upload** |
| Runs as | **Cloud + API** | **Desktop** QGIS plugin or Python package. | **Windows desktop** | **Compute cluster** | **Browser app** Detailed CFD only through RWDI consulting. |
| Agent-ready Can a script or an AI agent run it, with no person at the screen? | **API, SDK, skill** REST API, Python and TypeScript SDK, and an agent skill for Claude Code, Cursor and Codex. MCP server coming. | **Python scripts** Runs headless as a Python package; no hosted API. | **No public API** None found on the vendor pages, checked 30 Oct 2026. | **HPC batch jobs** Scripted runs on a compute cluster; no hosted API. | **No public API** None found on the vendor pages, checked 30 Oct 2026. |
| Licence | **Tokens** Free plan to start. | **GPL-3.0** | **Subscription** No public prices. | **GPL v3** | **Pay per run** |
| Live climate layer An hourly climate layer for a digital twin. | **Hourly** For a whole city. | **Not offered** | **Not practical** Hours per run. | **Not practical** Hours per run. | **Not offered** |

Not in the table: EnergyPlus, a different job (footnote 4 ) , and SimScale, a general cloud CFD platform (footnote 13 ) .

## Real geometry, not voxels

infrared.city uses the actual building and terrain meshes. It does not turn the city into a grid of cells. Arcades stay open and sloped roofs stay sloped. (footnote 1 )

**3D cell grid** ENVI-met, PALM-4U The roof becomes steps. The arcade is cut to the cell size.

**Height raster, 2.5D** SOLWEIG One height for each cell. The arcade is filled in.

**Real mesh** infrared.city The actual roof, facade and slope. The arcade stays open.

Illustration: the same building in three ways of storing shape. Cell size is exaggerated to show the effect. Sources: infrared.city internal validation report (Oct 2026, available on request), and the tools' documentation.

## Speed

Run time per km², one day

Typical UTCI calculation, rough estimate per km² and simulated day; physics differ. Linear: 24 h wide. Log: 1 s to 100 days.

infrared.city

~5 s 1 km², 08–18 h 1

SOLWEIG

~7 s on GPU 2 m grid; ~33 s on CPU 9

ENVI-met

~45 days per km² at 1 m, extrapolated 8

PALM-4U

~4–5 days per wind direction, per km² at 1 m, extrapolated 7

0 6 h 12 h 18 h 24 h

1 s 1 min 1 h 1 day 10 days

Zoom: the first minute

infrared.city

~5 s

SOLWEIG

~7 s (GPU)

**0** **15** **30** **45** **60**

s

Measured Extrapolated

Orbital Stack: minutes per site with AI, 2 to 3 business days per site with CFD; a site is about 0.3 km², and no per-km² time is published, so it is not drawn. 12

Everything but infrared.city is extrapolated linearly from a smaller run; real scaling is often worse for 3D models. 14 The ENVI-met and PALM-4U runs are a full microclimate run and a wind run; we screen, then you go deep where it matters. ENVI-met 6.0 claims up to 10 times faster; not measured by us.

Decide, operate, monitor

### infrared.city

Every option, every street, every hour. Informed decisions from the first sketch, whole sites to whole cities in seconds, and a live layer to operate and monitor.

Validation of extreme or critical cases

### Detailed CFD and LES tools

For a final check of one chosen design or a critical case: full physics in hours to days per site.

Most teams use infrared.city to decide, and validate only the cases that need it.

## Questions

infrared.city compared with ENVI-met, SOLWEIG, PALM-4U and Orbital Stack.

**Is infrared.city an alternative to ENVI-met?**

infrared.city and ENVI-met do different jobs. infrared.city tests every option for a block, a district or a whole city in seconds, on real 3D building and terrain meshes, in the cloud and through an API. ENVI-met is a Windows desktop tool for a full microclimate run on a 3D cell grid (voxels).

ENVI-met run time is published: 65 hours per simulated day for a 0.06 km² block at 1 m (version 5.9). We ran no same-input test against ENVI-met, so we make no accuracy claim against it. Most teams use infrared.city to decide, and validate only the cases that need it.

**Is infrared.city an alternative to SOLWEIG?**

Yes, for radiant heat. SOLWEIG is a widely used research model for radiant heat. It works on a 2.5D height raster and runs on the desktop, in QGIS or in Python. infrared.city works on real 3D meshes and runs in the cloud with an API.

We tested both against field instruments on the same input: same points, weather and 3D scene. At Gothenburg the two are on par. Melbourne and Guelph are held-out sites. The chart and the method are on this page and on the validation page.

**Is infrared.city an alternative to PALM-4U?**

They serve different steps. PALM-4U is a detailed model on 3D voxels. It runs on a large compute cluster and gives airflow and energy results. In the speed row of this page, a wind run takes about 4 to 5 days per wind direction per km² at 1 m (extrapolated; a wind run, not UTCI).

infrared.city is for the decision step: every option, whole sites to whole cities in seconds, plus a live layer. Use a detailed tool such as PALM-4U for a final check of one chosen design or a critical case.

**Is infrared.city an alternative to Orbital Stack?**

Both give wind comfort, thermal comfort and solar analyses. Orbital Stack is a browser app. It takes an STL upload and covers one study site with a 300 m context radius. Its CFD results arrive in 2 to 3 business days per site, and its AI results take minutes per site.

infrared.city uses real 3D meshes, runs 12 models from one engine, and works in the cloud, through an API and in the browser. Whole sites to whole cities take seconds.

**How fast is infrared.city compared with other tools?**

infrared.city takes about 5 s for 1 km² when the scene is reused, and about 17 s for the first run (perceived heat, UTCI, 08 to 18 h, measured). A 100 km² area took 37 s from submission to result, including building data and upload (measured 23 Oct 2026).

On the same rough basis, SOLWEIG takes about 7 s per km² on a GPU, ENVI-met about 45 days per km² at 1 m (extrapolated from one published run) and PALM-4U about 4 to 5 days per km² at 1 m (extrapolated). These are estimates. The footnotes on this page give the sources and the arithmetic.

**How accurate is infrared.city?**

We test radiant heat (Tmrt) against field instruments at four sites: Gothenburg, Phoenix, Melbourne and Guelph. Phoenix and Gothenburg are in-sample. Melbourne and Guelph are held-out sites: we changed no setting for them. We ran SOLWEIG on the same input as a reference.

The validation page lists all sites, the reference data and the method.

**When should I use which tool?**

Use infrared.city to decide: it tests every option, from the first sketch, for a block, a district or a whole city, in seconds. Use detailed CFD and LES tools for a final check of one chosen design or a critical case: full physics in hours to days per site.

## Sources

1. infrared.city, measured. Speed basis: benchmark of 24 Oct 2026 (SDK 1.0.0): one 512 × 512 m tile (Vienna, 2,931 buildings; the 500 × 500 m block fits one 512 m tile), 15 July 08 to 18 h, ground UTCI, warm median 3.0 s end to end (4 runs, buildings already fetched; the first run took 14.2 s with the building fetch). Facades: the same block, solar radiation on facades and roofs, 581,334 surface triangles, 6.4 s warm (9.6 s first run); the SDK has no facade UTCI. Large runs, production cloud, 23 Oct 2026: UTCI for one summer day, 08 to 18 h, hourly, 1 m grid, 100 km² of Hamburg in 37 s from submission to result; 1 km² in about 5 s on reuse, 17 s on a first run. Whole-city runs (about 1,700 km² at 1 m) are a statement by infrared.city, 24 Oct 2026. Source: infrared.city internal validation report (Oct 2026), available on request. The facade benchmark covers one 500 m block only. Hourly live layer: statement by infrared.city, 24 Oct 2026, and the Products page for the climate live layer.

2. EnergyPlus is not in the table: building energy is a different job. infrared.city screens many buildings or variants; EnergyPlus goes deep on one building. It runs one building model at a time with thermal zones (energyplus.net, US Department of Energy), and districts need batch runs. About 2 min per annual run for a 15-zone office: 124 s on a 2008 desktop, version 2.2.0 (LBNL run-time report), so current runs may differ. A 2025 preprint (arXiv 2511.19463) ran about 25,000 buildings in under 30 min on a large compute cluster. Free, BSD-like licence (GitHub README).

3. Statement by infrared.city, 24 Oct 2026: the engine supports large areas.

4. PALM-4U: Maronga et al. (2020), Geosci. Model Dev. 13:1335. LES (optional RANS), building surface and indoor model, comfort indices (PT, UTCI, PET). Cartesian cells, each fully fluid or fully obstacle; studies use 1 to 24 m. Whole city: Maronga et al., ICUC10 (2018), conference abstract, "Building-resolving large-eddy simulations for entire Berlin" (elib.dlr.de/121678): "PALM-4U is able to compute entire city environments like Berlin (about 1 700 km²)" at 10 m, with a nested 1 km² domain at 1 m; computing cost not reported. Largest 2 m test in the 2020 paper: 1.8 × 1.8 km on 1,296 CPU cores. Cost: CoSynHealth project report (project 1443, 2025 to 2026, Central Altona, Hamburg): "Single 2 m simulations ended up consuming a total of around 2000 node hours (NH) for 24h of simulation"; domain size and node type are not stated. Wall time, derived: Krüger, Burmeister and Winkler (2023), "PALM-4U Handbuch für die Praxis", ProPolis, table on p. 26 ([PDF](https://www.uc2-propolis.de/imperia/md/assets/propolis/images/propolis_handbuch_fuer_die_praxis_final_31-08-2023.pdf)), Hamburg Oberbillwerder wind comfort: child domain 400 × 450 × 50 m at 1 m (0.18 km²) nested in a 480 × 480 × 50 m parent at 5 m, no spin-up, 6 h simulated per run, 8 wind directions, HPC Levante with 300 cores, "Rechenzeit" 39 h in total (about 5 h per direction). Arithmetic: 39 h ÷ 8 ≈ 5 h per 6 simulated hours, so 5 h × 24 / 6 ≈ 20 h per simulated day per wind direction. This is a neutral-stratification wind-comfort setup, not a thermal run, and the handbook's "Rechenzeit" is compute time, not stated to be wall-clock. It assumes the time scales linearly with the simulated hours. Built for HPC; small domains can run on workstations. GPL v3 for the model system. Developed at Leibniz University Hannover.

5. ENVI-met: 3D wind and turbulence fields with plants, soil and walls; grid typically 1 to 10 m, time step 1 to 5 s (help.envi-met.com). Typical model sizes 50 × 50 to 500 × 500 cells (envi-met.com). Windows 10 or 11, 64 bit; business edition uses all CPU cores. Subscription licence, no public prices (envi-met.com/pricing). Run time: measured about 65 h per simulated day for a 0.06 km² block at 1 m on version 5.9 (Sinsel et al. 2026, below). The vendor says version 6.0 "Simulations run up to 10x faster now" (envi-met.info); we have not tested 6.0. The per-km² figure in the table is an extrapolation; see footnote 14. The 65 h comes from Sinsel et al. (2026), "Comparative validation of ENVI-met versions 5.6 and 5.9…", Atmospheric Environment: X 31, 100479, [doi:10.1016/j.aeaoa.2026.100479](https://doi.org/10.1016/j.aeaoa.2026.100479) (CC BY 4.0): 340 × 171 × 35 cells of 1 × 1 × 2.5 m, 5 nesting grids, 168 h simulated, about 1,383 h on 5.6 and about 455 h on 5.9, which is about 65 h per simulated day on 5.9, on one AMD Threadripper Pro 5965WX desktop (24 cores, 512 GB). The authors call it a rough estimate. The paper shows about 3 times faster from 5.6 to 5.9; the 10 times for 6.0 is the vendor's claim and is not in the paper. Salvati and Kolokotroni (IBPSA BS2019, 500 × 300 m at 2 m, version 4.3.2): about 38 to 120 h.

6. SOLWEIG: a 2.5D model on height rasters of one resolution (UMEP manual, umep-docs.readthedocs.io). Full day: Zonato et al. (2026), Geosci. Model Dev. 19:7389 (GLIDE-SOL, SOLWEIG 2022a based), Dortmund, 3129 × 3113 pixels at 2 m (about 39 km²), 24 h simulated: "Using one NVIDIA A100 (40 GB) GPU, the 24 h simulation completed in 254 s", 1,285 s on CPU of the same node. Kamath et al. (2026), SOLWEIG-GPU, JOSS 11(118):9535, Table 1 (sky view factor and UTCI, mean of 4 to 5 runs, 1,000 × 1,000 pixels): CPU 1,187 s (Intel i7-10700), GPU 47 s (NVIDIA A6000); wall preparation excluded; pixel size and period not stated. Wall surface temperature: GMD 19:7389. Runs as the Python package solweig-gpu (PyTorch, CPU or GPU) or in QGIS (UMEP). Grids above 4 million pixels should be tiled. GPL-3.0.

7. Orbital Stack (RWDI), from the vendor's own pages only, checked 24 Oct 2026. Three levels. **AI** (since 28 Sep 2022): "Get wind and climate estimations in seconds" (orbitalstack.com/ai-powered-wind-simulations); about $100 for an AI wind run and $150 to $200 for AI thermal comfort. **Rapid CFD, self-serve**: "The CFD Engine provides a rapid, RANS based CFD evaluation" (2023 onboarding roadmap, help.orbitalstack.com) and "All results should be available within 2-3 business days" (help.orbitalstack.com/add-new-scenario/); about $350 for wind and $500 to $700 for thermal comfort per run. **Detailed CFD and LES**: "(available only through RWDI consulting engagements – simulated and delivered in Orbital Stack)" (orbitalstack.com/purpose-built-cfd). Size: "Buildings and structures located within a 300m radius of the study building" and "The total surface area of all structures and ground surfaces combined must be less than 3.5 km²" (help.orbitalstack.com/preparing-the-geometry-guide/). Analyses: wind comfort, thermal comfort, solar, airflow and cladding wind loading (orbitalstack.com/climate-analysis-overview/). Geometry: "All files must be exported from your CAD software in STL file format." Runs in a browser app. No public API or SDK was found on the vendor pages, and no live or hourly product; both are absence claims. No area or hardware is stated for the run times. Prices are the vendor list prices on its pricing page.

8. SimScale is not in the table: a general cloud CFD platform with an urban module (wind comfort, thermal comfort including UTCI, solar). Its lattice-Boltzmann runs take hours (vendor: "competition-stage results come back in hours", simscale.com/simulations/urban-microclimate/); AI surrogates are shown for other physics, not for urban.

9. Speed row and chart: a typical perceived heat (UTCI) calculation, as a rough estimate per km² and per simulated day. It assumes the run time scales linearly with area and simulated hours; real scaling is often worse than linear for 3D models, so large extrapolations are the least certain. Source values and arithmetic. **infrared.city**: measured, about 5 s for 1 km² at 1 m, warm, 08 to 18 h hourly (not scaled to 24 h); also one 512 × 512 m tile in 3.0 s. 100 km² in 37 s is 0.37 s per km². **SOLWEIG** (Zonato et al. 2026, GLIDE-SOL; the pipeline computes UTCI, per the abstract, and the benchmark times the full pipeline): 254 s on one GPU and 1,285 s on CPU for about 39 km², 24 h, 2 m; 254 / 39 = 6.5 s and 1,285 / 39 = 33 s per km². **ENVI-met**: extrapolated linearly from a published 168 h run of ENVI-met 5.9 on a 0.058 km² site at 1 m (455 h on a 24-core, 512 GB workstation; Sinsel et al. 2026, Atmospheric Environment: X 31, 100479): 65 h per simulated day, so about 1,120 h per km² per day, which is about 45 days. That is a ×17 extrapolation of one run, so read it as a size, not a measurement. Real run time depends on hardware, domain and settings. A 1 km² domain at 1 m is far above ENVI-met's documented large-model rule of thumb (250 × 250 × 30 cells) and usually needs tiling. The vendor says version 6.0 runs "up to 10x faster"; we have not measured it. At that best case one 0.06 km² block at 1 m would take about 6.5 h. The run computes a full microclimate and writes UTCI and PET for a standard person ([ENVI-met help centre, "Thermal Comfort", Sep 2025](https://help.envi-met.com/en/articles/378659-thermal-comfort) ↗). BIO-met adds personal settings and PMV, SET and dynamic comfort. **PALM-4U** (handbook): measured 39 h in total for 8 wind directions of 6 simulated hours each on 0.18 km² at 1 m with 300 cores, so about 5 h per direction and about 20 h per simulated day per direction; extrapolated to about 111 h per km², which is 4 to 5 days. This is a wind-comfort run, not UTCI. **Orbital Stack**: no area-time figure is published, so no time is extrapolated. For size only: a site has a 300 m context radius, so π × 0.3² = 0.28 km² (about 0.3 km²), which is about 3 to 4 sites per km². This size is our estimate from the vendor's 300 m radius, not a vendor figure.

10. SOLWEIG described as "a widely used urban radiation model for spatially resolving pedestrian radiative environments": Kang, Lindberg, Bridoux, Wallenberg and Kim, "Development of SOLWEIG-LEB v1.0: An urban radiation model integrating LAD-based canopy shortwave attenuation and leaf energy balance", EGUsphere preprint egusphere-2026-6123 (not peer reviewed; abstract quoted from the raw page, 24 Oct 2026). Same points, weather and 3D scene for both models; in-sample sites are lighter in the chart.

**Other comparisons**

Simulation and design tools: [ENVI-met](https://infrared.city/compare/envi-met), [SOLWEIG](https://infrared.city/compare/solweig), [PALM-4U](https://infrared.city/compare/palm-4u), [Orbital Stack](https://infrared.city/compare/orbital-stack), [Autodesk Forma](https://infrared.city/compare/autodesk-forma), [SimScale](https://infrared.city/compare/simscale), [Ladybug Tools](https://infrared.city/compare/ladybug-tools), [ClimateStudio](https://infrared.city/compare/climatestudio). Urban heat data: [FortyGuard](https://infrared.city/compare/fortyguard), [Satellite Vu](https://infrared.city/compare/satellite-vu), [constellr](https://infrared.city/compare/constellr), [Hydrosat](https://infrared.city/compare/hydrosat). Climate risk: [Jupiter Intelligence](https://infrared.city/compare/jupiter-intelligence), [XDI](https://infrared.city/compare/xdi). Digital twin and climate platforms: [VU.CITY](https://infrared.city/compare/vu-city), [Bentley iTwin](https://infrared.city/compare/bentley-itwin), [ArcGIS Urban](https://infrared.city/compare/arcgis-urban), [NVIDIA Earth-2](https://infrared.city/compare/nvidia-earth-2), [Destination Earth](https://infrared.city/compare/destination-earth). Building LCA and ESG: [LCA and ESG tools](https://infrared.city/compare/lca-and-esg-tools).
