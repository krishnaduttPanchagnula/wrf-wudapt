# UrbClim / UrbSim (VITO) — Competitor Profile

**URL**: https://vito.be/en/applications/urbclim-limit-climate-risks-your-city · https://vito.be/en/applications/urbsim-urban-climate-simulator · https://climasys.vito.be/en/products/urbsim
**Generated**: 2026-11-25
**Depth**: quick scan
**Evidence convention**: **Observed** = verbatim claim on a source page; **Inferred** = our reading; **Implication** = option for wrf-wudapt, not a conclusion.

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline (Observed) | "UrbClim: limit the climate risks in your city"; "UrbSim, the Urban Climate Simulator" |
| Organisation (Observed) | VITO, Flemish research institute (Mol, Belgium); UrbSim sold via its Climasys unit |
| Target audience (Observed) | Local policymakers, researchers, city/government officials, consultants, study offices, development agencies, climate investors |
| Pricing (Observed) | "cheap and easy-to-process"; **no numeric public price observed** on pages checked, as of 2026-11-25 |
| Free tier/trial | **Not observed** on pages checked, as of 2026-11-25; free download of 2008–2017 data for 142 European cities is offered |
| Domain rank / organic traffic / keywords / referring domains | **unavailable (no SEO data source)** — web search and SEO MCPs were unavailable in this scan |
| Review ratings | **Not observed** on pages checked, as of 2026-11-25 |

---

## Positioning & Messaging

**Primary value proposition (Observed)**: UrbClim "generates accurate climate models for cities", solving "a set of simplified prognostic flow equations for the atmospheric boundary layer" with "detailed urban surface physics". UrbSim wraps it in "an attractive web interface" delivering "hourly spatial urban climate data according to your specifications".

**Positioning angle (Inferred, medium confidence)**: research-grade but service-packaged urban climate modelling — sell the *data package and decision support*, not the raw model. VITO's own framing is "make these predictions" so policymakers "can take concrete measures".

**Key messaging themes (Observed)**:
- Decades-long simulations at ~100 m "at an affordable computational cost", nested in "an ensemble of large-scale climate models" — homepage.
- "Discover how green/blue measures affect your urban climate" — homepage (measures → climate response).
- Any city worldwide, 2001–2100, any IPCC AR6 scenario, pre-selected land-use specifications — UrbSim/Climasys pages.

---

## Product & Features

### Core capabilities (Observed)
- Dynamical downscaling with simplified ABL flow equations + detailed urban surface physics; outputs temperature, wind speed, heat-wave days, cooling degree days.
- On-demand simulations: any city, any period 2001–2100, any IPCC AR6 scenario, up to 100 m, pre-selected land-use specifications.
- Deliverable data package: temperature/heat-stress indicators for requested domain, periods and scenarios; optional hourly output; technical documentation of methodology/input datasets/indicators; high-resolution PNG quicklooks.
- Input data from Copernicus CLMS and C3S; "extensive validation for several cities" (no numbers on these pages).
- Tailored add-on services: mortality/GDP impact calculations, adaptation planning with cost–benefit analysis, future projections including urban growth, heat-stress modelling up to 1 m.

### Notable differentiators (Observed)
- Explicit multi-decadal + ensemble + scenario framing: "one of the few models worldwide" able to run "decades" nested in an ensemble of large-scale climate models.
- Model applied "in hundreds of cities around the world" (vendor claim).

### Integrations (Observed)
- Copernicus Land Monitoring Service (CLMS) and Climate Change Service (C3S) as input sources; free historical data download at `provide.marvin.vito.be`.

### Product direction signals (Observed / Inferred)
- Climasys markets both the self-serve web tool and bespoke consulting; Inferred (low confidence) direction is toward service revenue around the model, not a public desktop app.

---

## Pricing

| Tier | Price | Key inclusions |
|------|-------|----------------|
| UrbSim web tool | **Not observed** on pages checked, as of 2026-11-25 | "cheap and easy-to-process"; request-driven simulation; data package |
| Tailored analytics | **Not observed** on pages checked, as of 2026-11-25 | Mortality/GDP, cost–benefit, urban-growth projections, 1 m heat stress |
| Historical data | Free download stated | 2008–2017, 142 European cities |

**Billing / trial / hidden costs**: not observed. "Cheap" is a qualitative claim, not a price — do not quote it as a number.

---

## Customers & Social Proof

**Named customers (Observed)**: none named on the pages checked.
**Industries (Observed)**: local/regional/national/international public clients, researchers, consultants, investors.
**Case-study themes (Observed)**: "hundreds of cities"; urban heat-island assessment, heat-stress forecasts, green/blue measure effects.
**Review ratings**: not observed on pages checked, as of 2026-11-25.

---

## SEO & Content Strategy

**Organic strength**: unavailable (no SEO data source). Web search returned HTTP 402 in this environment; no metrics were estimated.
**Top organic pages**: unavailable (no SEO data source).
**Content strategy signals (Observed, qualitative only)**: product/application pages, news items, technical downloads, a demo video, and a public data FTP. No post frequency measured.
**Backlink profile**: unavailable (no SEO data source).

---

## Strengths & Weaknesses

### Strengths (Observed)
- Multi-decadal, high-resolution, climate-scenario simulations with ensemble forcing — directly addresses long time horizons.
- Explicit green/blue-measure effect assessment and land-use specification choice.
- Validation and Copernicus-sourced inputs are stated; data package includes methodology docs.

### Weaknesses / limits of evidence (Observed / Inferred)
- **Not observed on pages checked, as of 2026-11-25**: a user-drawn counterfactual area with before/after ΔT maps, per-class differencing, a desktop app or QGIS plugin.
- **Not observed**: numeric validation skill metrics (bias/RMSE/MAE) on these pages; the claim is "extensive validation" only.
- **Not observed**: public pricing or self-serve cost calculator.
- Inferred (medium confidence): land-use scenarios are "pre-selected", so arbitrary user interventions may require bespoke work.

---

## Competitive Implications for wrf-wudapt

**Where they're strong vs. us**: time horizon (2001–2100 vs. our 18 h case), AR6 scenario ensemble, service delivery with documentation and quicklooks.

**Where we're strong vs. them (Inferred, hypothesis)**: we expose a concrete user-defined counterfactual (built-up → grassland in a chosen circle), an open reproducible pipeline (checksums, namelists, seeds per CONSTRAINTS.md), ΔT2 per LCZ tables, and a free desktop/QGIS front-end. No win/loss evidence was available, so treat this as a hypothesis.

**Opportunities**: a second-year comparison is now implemented (engine/CLI/GUIs, 2026-11-25) but not yet executed; running it would move us from "one event" toward the multi-period framing that UrbSim sells, without abandoning our counterfactual WRF design.

**Threats**: UrbSim's "decades at 100 m" and Copernicus-backed inputs set a scale expectation our 1–2 h per 18 h run cannot match; compete on intervention clarity, not on raw throughput.

---

## Raw Data Sources

All raw markdown under `competitor-profiles/raw/urbclim/2026-11-25/scrapes/`, retrieved **2026-11-25**:
- `homepage.md` — https://vito.be/en/applications/urbclim-limit-climate-risks-your-city
- `urbsim.md` — https://vito.be/en/applications/urbsim-urban-climate-simulator
- `climasys-urbsim.md` — https://climasys.vito.be/en/products/urbsim
- `urban-climate-model.md` — https://urban-climate.eu/model (JS-only; no text extracted; not used as evidence)

SEO data: unavailable (no SEO data source). Review data: none collected (quick scan).
