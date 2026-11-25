# WRF-Urban (NSF NCAR / Research Applications Laboratory) — Competitor Profile

**URL**: https://ral.ucar.edu/model/wrf-urban-modeling · https://ral.ucar.edu/model/urban-canopy-model · https://www2.mmm.ucar.edu/wrf/users/
**Generated**: 2026-11-25
**Depth**: quick scan
**Evidence convention**: **Observed** = verbatim claim on a source page; **Inferred** = our reading; **Implication** = option for wrf-wudapt.

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline (Observed) | "WRF-Urban Modeling — Enhancing the WRF-urban modeling system and its applications to real-time weather forecasts for mega cities" |
| Organisation (Observed) | NSF NCAR Research Applications Laboratory (RAL), with MMM maintaining WRF code |
| Target audience (Observed) | Research/modelling community; "community tool" for urban environmental problems |
| Licence / price (Observed) | WRF is "in the public domain for use by any person or entity for any purpose without any fee or charge" (WRF Public Domain Notice); free source download |
| Domain rank / traffic / keywords / domains | **unavailable (no SEO data source)** |
| Review ratings | **Not observed** on pages checked, as of 2026-11-25 |

---

## Positioning & Messaging

**Primary value proposition (Observed)**: an "integrated, multi-scale urban modeling system" for WRF addressing "impacts of urban heat islands on regional weather, climate, air quality, public health, and water resources".

**Positioning angle (Inferred, high confidence)**: community physics infrastructure, not a product. Value is in schemes, documentation, parameter tables and publications; users assemble their own workflow.

**Key messaging themes (Observed)**:
- Urbanisation raises hydroclimate risk; urban canopy models capture urban land-surface processes.
- Continued scheme development: Noah-MP coupling, u-HRLDAS, tested over Phoenix and Beijing.
- "Beginning with V4.3, code is updated to include a capability to use local climate zones, which is incorporated for all three urban applications" (WRF User Guide, Urban Effects section).

---

## Product & Features

### Core capabilities (Observed)
- `sf_urban_physics` options: 1 = single-layer UCM; 2 = multi-layer BEP; 3 = BEM adding heating/air conditioning (YSU/MYJ/BouLac PBL restrictions apply).
- Noah and Noah-MP LSM coupling; urbanized high-resolution land data assimilation system (u-HRLDAS).
- NUDAPT static data for 40+ US cities; `URBPARM.TBL` urban parameter table; spatially varying 2-D urban parameters and anthropogenic heat flux options in SLUCM.
- LCZ capability from WRF v4.3 across all three urban applications; technical docs for a hybrid 100 m global LCZ land-cover dataset.

### Notable differentiators (Observed)
- Open, community-maintained code with a support forum, tutorials, annual workshop and documented physics review process.
- Research base includes mitigation studies (rooftop strategies, "different urban heat mitigation efficacy with the same strategies") and building-energy/air-conditioning feedbacks.

### Integrations (Observed)
- WPS/geogrid static data, NUDAPT, WRFDA/WRF-Chem/WRF-Hydro within the WRF system; no third-party SaaS integration observed.

### Product direction signals (Observed)
- Latest WRF releases listed as v4.8.0 / WPS v4.7.0 on the WRF users page; active 2026 workshop and tutorial programme.

---

## Pricing

| Tier | Price | Key inclusions |
|------|-------|----------------|
| WRF + urban schemes | No fee (Observed public-domain notice) | Source code, docs, parameter tables; user supplies compute and data |

**Billing / trial / hidden costs**: not applicable as a product; compute and expertise are the real cost (Inferred). No commercial tier observed.

---

## Customers & Social Proof

**Named customers (Observed)**: none; framed as a community tool with a user community and annual workshop.
**Industries (Observed)**: meteorological research, operational forecasting, urban environmental studies.
**Case-study themes (Observed in linked publications)**: Phoenix and Beijing metro tests, Oklahoma City verification, air-conditioning load impacts in Beijing, mitigation efficacy across cities.
**Review ratings**: not observed on pages checked, as of 2026-11-25.

---

## SEO & Content Strategy

**Organic strength**: unavailable (no SEO data source).
**Top organic pages**: unavailable (no SEO data source).
**Content signals (Observed, qualitative)**: extensive technical docs, downloadable PDF guides, publication lists, release notes, workshop pages. No frequency measured.
**Backlink profile**: unavailable (no SEO data source).

---

## Strengths & Weaknesses

### Strengths (Observed)
- Authoritative source for WRF urban physics, including the LCZ capability that wrf-wudapt depends on.
- Transparent parameterisation (`URBPARM.TBL`) and explicit scheme limitations in docs — useful for verifying that an intervention "bites".
- Zero licence cost and large community.

### Weaknesses / limits of evidence (Observed / Inferred)
- **Not observed on pages checked, as of 2026-11-25**: an end-user app, a "baseline vs proposal" comparison service, map/CSV deliverables, multi-year comparison workflow, or named commercial support tier.
- Some RAL page text is visibly dated (states Noah-MP coupling "will be released in WRF in 2017"); treat version claims as stale and prefer the current User Guide.
- Inferred (high confidence): assembling a counterfactual study is left to the user — this is exactly the gap wrf-wudapt fills.

---

## Competitive Implications for wrf-wudapt

**Where they're strong vs. us**: physics provenance, scheme breadth, community scale, ongoing releases; our LCZ path ultimately rests on this codebase.

**Where we're strong vs. them (Inferred, hypothesis)**: wrf-wudapt packages a specific counterfactual question (replace built-up with grassland in a circle) into a GUI/QGIS workflow with ΔT2 maps, CSVs and an emulator — no equivalent packaged workflow was observed on NCAR pages.

**Opportunities**: use WRF-Urban's own LCZ capability and parameter tables to close the current "USING DEFAULT URBAN MORPHOLOGY" limitation in our README; that would strengthen the LCZ-enters-physics constraint.

**Threats**: NCAR docs make the same physics available to any competent modeller; our differentiation must stay in workflow, provenance and comparison, not in claiming exclusive physics.

---

## Raw Data Sources

All raw markdown under `competitor-profiles/raw/wrf-urban/2026-11-25/scrapes/`, retrieved **2026-11-25**:
- `homepage.md` — https://ral.ucar.edu/model/wrf-urban-modeling
- `urban-canopy-model.md` — https://ral.ucar.edu/model/urban-canopy-model
- `wrf-users-homepage.md` — https://www2.mmm.ucar.edu/wrf/users/
- `public-domain.md` — https://www2.mmm.ucar.edu/wrf/users/public_domain_notice.html
- `physics-lcz.md` — https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/physics.html (Urban Effects section: LCZ from v4.3)

SEO data: unavailable (no SEO data source). Review data: none collected (quick scan).
