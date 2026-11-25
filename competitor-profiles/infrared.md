# infrared.city — Competitor Profile

**URL**: https://infrared.city/ · https://infrared.city/products-live · https://infrared.city/solutions-2050-scenarios · https://infrared.city/pricing · https://infrared.city/docs/sdk/
**Generated**: 2026-11-25
**Depth**: quick scan
**Evidence convention**: **Observed** = verbatim claim on a source page; **Inferred** = our reading; **Implication** = option for wrf-wudapt. Claims on this vendor's comparison/validation pages are vendor statements, not independent findings.

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline (Observed) | "The climate intelligence layer for cities and buildings: wind, heat and sun at street level. API, SDK, plugins and a live layer for your digital climate twin." |
| Origin (Observed) | Started at the City Intelligence Lab, Austrian Institute of Technology, Vienna |
| Target audience (Observed) | Cities, real-estate developers, software platforms, architects; Enterprise for city scale |
| Pricing (Observed) | Free €0 (900 tokens, 42 days); Starter €240/yr; Advanced €1,200/yr; Pro €6,000/yr; Enterprise custom. Pricing page "Last updated 21 Nov 2026" |
| Free trial (Observed) | 900 tokens once, no card, valid 42 days |
| Domain rank / traffic / keywords / domains | **unavailable (no SEO data source)** |
| Review ratings | **Not observed** on pages checked, as of 2026-11-25 |

---

## Positioning & Messaging

**Primary value proposition (Observed)**: "Wind, heat, sun and daylight in seconds. From buildings to cities"; one engine across "plan, design and operate", with a "live layer for digital twins: the climate forecast for the next 72 hours, every hour, at metre scale."

**Positioning angle (Inferred, high confidence)**: decision-stage speed and side-by-side comparability over maximum physical detail. Their own comparison page says: "Use a detailed tool such as PALM-4U for a final check of one chosen design or a critical case."

**Key messaging themes (Observed)**:
- "Today and 2050 side by side, for every street, within minutes" — IPCC SSP scenarios (e.g. SSP2-4.5).
- "Compare the scenarios side by side, for the entire city"; "A district twin: the base, a cooling design and the difference, hour by hour."
- "Test your adaptation plan… trees, shade, cool and permeable surfaces, water or closures" against forecast, typical summer or 2050.
- Validation and transparency: "tested against street measurements in four cities", model cards for 12 models, published comparison footnotes.

---

## Product & Features

### Core capabilities (Observed)
- 12 analyses from one engine; SDK docs list wind speed, pedestrian wind comfort, solar radiation, direct sun hours, daylight availability, sky-view factor, UTCI, comfort/stress, interior daylight factor and energy balance.
- Live layer: city climate "every hour, tomorrow, a typical year or 2050"; 72 h forecast, typical-year weather file, or 2050 weather made by "morphing that file"; recompute entire city hourly (vendor-stated 500× faster than fresh SDK simulation).
- Scenario comparison: baseline vs cooling design vs difference, hour by hour; today vs 2050 with "same city, same physics, so 2050 and today compare directly".
- Inputs: one polygon, user model (buildings, trees, ground materials, terrain, context geometry), weather and a time period; hourly weather file with one year (8,760 rows), with date/hour windows (e.g. 1 Jun–31 Aug, 08–18 h).
- Outputs: ground maps, facade/roof values, room values, sensor-point values; exports "3D Tiles, map tiles, GeoTIFF and tables".
- Delivery: web platform, API, Python/TypeScript SDK (PyPI), design-tool plugins, custom deployment in EU cloud or on-prem (Enterprise).

### Notable differentiators (Observed)
- "One baseline for every submission: every design on the same model, weather and KPIs. Anyone can rerun the result."
- Ranking "cost per degree" for adaptation options and side-by-side PALM-4U checks.

### Integrations (Observed)
- Python SDK on PyPI, TypeScript SDK, Rhino/Grasshopper plug-in (work in progress), REST API, 3D Tiles / map tiles for digital twins and GIS; Enterprise integrations with client systems.

### Product direction signals (Observed)
- Pricing page updated 21 Nov 2026; validation page updated 23 Nov 2026; SDK docs note SDK 1.1 with Python on PyPI still 1.0; .NET SDK "coming".

---

## Pricing

| Tier | Price | Key inclusions |
|------|-------|----------------|
| Free | €0, 900 tokens once / 42 days | All models; 5 req/s; €1.00 per simulation equivalent |
| Starter | €240/yr | 500 tokens/mo; 10 req/s; ~€0.40 per simulation |
| Advanced | €1,200/yr | 3,000 tokens/mo; 30 req/s; ~€0.34 per simulation |
| Pro | €6,000/yr | 30,000 tokens/mo; 60 req/s; ~€0.17 per simulation |
| Enterprise | Custom | Custom quotas, SLA, OEM, on-prem, live layer |

**Billing (Observed)**: annual; token-based per simulation (10 tokens standard, 50 advanced), top-up packs; unused plan tokens roll within the paid year. Prices as stated on page last updated 21 Nov 2026.

---

## Customers & Social Proof

**Named customers (Observed)**: City of Luleå (ice-risk live-layer example); Hong Kong climate twin (example project); "Singapore tower study" and Vienna examples. Not stated as paying customers.
**Industries (Observed)**: cities, developers, architects, software platforms.
**Case-study themes (Observed)**: street-level heat forecast, 2050 adaptation, facade sun/daylight, ice risk.
**Review ratings**: not observed on pages checked, as of 2026-11-25.

---

## SEO & Content Strategy

**Organic strength**: unavailable (no SEO data source). No estimates made.
**Top organic pages**: unavailable (no SEO data source).
**Content signals (Observed, qualitative)**: an unusually strong structured content set — markdown mirrors of pages (`/index.md`, `/pricing.md`, etc.), detailed SDK docs, comparison pages targeting named alternatives (ENVI-met, SOLWEIG, PALM-4U, Orbital Stack, Destination Earth), validation page with numeric results, technical note PDFs. No posting frequency measured.
**Backlink profile**: unavailable (no SEO data source).

---

## Strengths & Weaknesses

### Strengths (Observed)
- Explicit multi-period and scenario UX: base / design / difference, today vs 2050, typical year, IPCC SSPs.
- Public, current pricing with a real free tier and transparent per-simulation cost.
- Validation page with held-out sites, RMSE values, standards alignment and a PALM-4U cross-check (r 0.92–0.94 for tree-option ranking).
- GIS-friendly exports and API/SDK; speed figures are measured and footnoted (100 km² UTCI in 37 s).

### Weaknesses / limits of evidence (Observed / Inferred)
- **Not observed on pages checked, as of 2026-11-25**: mesoscale WRF-based counterfactual runs, ERA5/GFS boundary data, LCZ-driven urban physics, or causal attribution from a land-surface intervention. Its adaptation tests run inside its own microclimate engine.
- Scale mismatch: 1 m street-level UTCI is not 2 m mesoscale air temperature (T2); comparisons must state the variable and height.
- Many headline claims (500× faster, 1,700 km² city runs, PALM cost estimates for competitors) are vendor statements or extrapolations explicitly marked as such on their own footnotes — treat as marketing evidence, not independent benchmarks.
- Inferred (medium confidence): "2050 weather made by morphing that file" is a climate-change signal applied to a weather file, not a full GCM-driven dynamical downscaling; verify before treating it as equivalent to AR6 ensemble runs.

---

## Competitive Implications for wrf-wudapt

**Where they're strong vs. us**: scenario UX, multi-year framing, validation communication, pricing transparency, GIS exports, click-through speed.

**Where we're strong vs. them (Inferred, hypothesis)**: counterfactual WRF physics with the user's land-use change actually perturbing the model, LCZ-based sampling, public reproducibility constraints, and a QGIS plugin — none of which were observed on infrared pages.

**Opportunities (high priority)**:
1. A second-year comparison now exists in the engine/CLI/GUIs (added 2026-11-25); no second-year run has been executed. Next step is the presentation they do well: base₂ / proposal₂ / ΔT2₂ beside period 1, hour by hour, with the difference-of-differences from `effect_year_on_year.csv`.
2. The trio presentation (base / proposal / difference) is now an HTML report generated with each comparison; next would be map layers and an hour slider, still without changing WRF physics.
3. `VALIDATION.md` now publishes our bias/RMSE/MAE and held-out numbers with provenance; remaining work is a public-facing version with variable/height stated, plus station data rather than ERA5.

**Threats**: infrared owns the language of "compare scenarios side by side" and will set user expectations for instant results; wrf-wudapt should be explicit that its answers come from a counterfactual physics run, not a fast screen.

---

## Raw Data Sources

All raw markdown under `competitor-profiles/raw/infrared/2026-11-25/scrapes/`, retrieved **2026-11-25**:
- `homepage-md.md` — https://infrared.city/index.md (mirror of https://infrared.city/)
- `solutions-cities.md` — https://infrared.city/solutions-cities.md
- `solutions-2050-scenarios.md` — https://infrared.city/solutions-2050-scenarios.md
- `solutions-one-baseline.md` — https://infrared.city/solutions-one-baseline.md
- `solutions-citywide-adaptation.md` — https://infrared.city/solutions-citywide-adaptation.md
- `products-live.md` — https://infrared.city/products-live.md
- `products-validation.md` — https://infrared.city/products-validation.md
- `products-compare.md` — https://infrared.city/products-compare.md (vendor comparison; untrusted claims attributed)
- `pricing.md` — https://infrared.city/pricing.md (page states "Last updated 21 Nov 2026")
- `sdk-docs.md` — https://infrared.city/docs/sdk/
- also `homepage.md`, `products.md`, `platform.md` (low-yield HTML scrapes)

SEO data: unavailable (no SEO data source). Review data: none collected (quick scan).
