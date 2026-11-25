# PALM-4U / PALM model system — Competitor Profile

**URL**: https://palm.muk.uni-hannover.de/trac/wiki/WikiStart · https://palm.muk.uni-hannover.de/trac/wiki/palm4u · https://www.palm-model.org/
**Generated**: 2026-11-25
**Depth**: quick scan
**Evidence convention**: **Observed** = verbatim claim on a source page; **Inferred** = our reading; **Implication** = option for wrf-wudapt.

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline (Observed) | "The PALM model system" — LES/RANS atmospheric and oceanic boundary-layer modelling; PALM-4U are its urban components |
| Organisation (Observed) | Leibniz Universität Hannover / UC²-MOSAIK consortium (BMBF-funded); new docs at palm-model.org |
| Target audience (Inferred) | Boundary-layer researchers, climate-service staff, trained city-planning staff |
| Pricing / licence (Observed) | "PALM model system is free software… GNU General Public License (v3)" |
| GUI (Observed) | Wiki text says a "user-friendly graphical user interface… will not be available to the general public until further notice" — page text may be stale; not verified against a current release |
| Domain rank / traffic / keywords / domains | **unavailable (no SEO data source)** |
| Review ratings | **Not observed** on pages checked, as of 2026-11-25 |

---

## Positioning & Messaging

**Primary value proposition (Observed)**: state-of-the-art turbulence-resolving LES with RANS option; for urban applications "PALM-4U components offer a variety of capabilities… related to the urban microclimate and climate change", including buildings resolved on a Cartesian grid "at grid spacings down to 1 m and below".

**Positioning angle (Inferred, high confidence)**: physics-first, open-source, HPC-grade research model — depth of process representation over planning workflow convenience.

**Key messaging themes (Observed)**:
- Component architecture: energy balance, radiation in the urban canopy, wall/indoor models, chemistry, agents, biometeorology.
- Computational credibility: "excellent scaling, so far tested up to 32,000 cores".
- Transition signal: "we are currently working on the new official PALM documentation" at palm-model.org.

---

## Product & Features

### Core capabilities (Observed)
- LES and RANS turbulence; complex terrain on Cartesian grid; online data analysis; coupled land surface + RRTMG radiation; Lagrangian particle model; user code plug-ins; GPU support via CUDA-aware MPI.
- PALM-4U: energy-balance solvers for building and paved surfaces; urban-canopy radiative transfer with shadowing and multiple reflections; multi-layer wall/material model; indoor temperature, energy demand and waste heat fed back to atmosphere; online chemistry (KPP 2.3, SALSA aerosol); self-nesting; multi-agent pedestrian model.
- External forcing: INIFOR processes COSMO and (per the newer WikiStart text) ICON/WRF output as boundary conditions.
- Biometeorology: area-wide PET, PT, UTCI and wind comfort as direct output; also Lagrangian agent-based exposure.

### Notable differentiators (Observed)
- Indoor/outdoor coupling and anthropogenic waste heat as part of the physics, not post-processing.
- Multi-agent system for exposure and escape-route studies.

### Integrations (Observed)
- COSMO-DE/ICON/WRF forcing via INIFOR; self-nesting; no SaaS integrations observed.

### Product direction signals (Observed)
- PALM Academy and Foundation Course launched 2026; new official documentation in transition.
- GUI described as "will be developed within the framework of the MOSAIK-2 project" — i.e. not a public end-user app on the pages checked.

---

## Pricing

| Tier | Price | Key inclusions |
|------|-------|----------------|
| Model system | Free, GPL v3 (Observed) | Full PALM + PALM-4U components; user supplies compute |
| Training | **Not observed** on pages checked, as of 2026-11-25 | PALM Academy / Foundation Course exist; price not stated on pages checked |

**Hidden costs (Inferred, medium confidence)**: HPC time and expertise. A third-party vendor comparison page claims ~4–5 days per km² at 1 m for PALM-4U wind runs, extrapolated — attribute to that vendor, not to PALM developers, and do not use as a head-to-head fact without verification.

---

## Customers & Social Proof

**Named customers (Observed)**: none named; a "PALM users world map" lists groups with peer-reviewed publications.
**Industries (Observed)**: academic boundary-layer research, climate-service companies, city planning (aspirational in wiki text).
**Case-study themes (Observed)**: entire-city simulations at 10 m with 1 m nested domains are cited in the vendor comparison page, not on PALM's own pages checked.
**Review ratings**: not observed on pages checked, as of 2026-11-25.

---

## SEO & Content Strategy

**Organic strength**: unavailable (no SEO data source). No estimates made.
**Top organic pages**: unavailable (no SEO data source).
**Content signals (Observed, qualitative)**: wiki documentation, release notes, Trac timeline, gallery, academy announcements. No frequency measured.
**Backlink profile**: unavailable (no SEO data source).

---

## Strengths & Weaknesses

### Strengths (Observed)
- Richest urban process physics among the tools scanned: building energy, canopy radiation, chemistry, agents, UTCI/PET/PT.
- Open GPL v3 licence and explicit reproducibility via source distribution.
- Forcing chain from mesoscale models (COSMO/ICON/WRF) and self-nesting.

### Weaknesses / limits of evidence (Observed / Inferred)
- **Not observed on pages checked, as of 2026-11-25**: a multi-year/decadal scenario comparison product, a public GUI, a map/CSV output service, or published skill metrics on these pages.
- Inferred (high confidence): high expertise and compute barrier. The wiki itself says "extensive experience is an essential prerequisite".
- Some wiki text is visibly old (GUI "until further notice", "support for ICON will be added later" alongside ICON/WRF mentioned in a newer summary) — flag as stale before quoting.

---

## Competitive Implications for wrf-wudapt

**Where they're strong vs. us**: microscale building-resolving detail, indoor/waste-heat physics, biometeorological indices, mature user community and training.

**Where we're strong vs. them (Inferred, hypothesis)**: a turnkey counterfactual workflow (baseline vs. land-use proposal) with desktop/QGIS front-end and LCZ-driven inputs, at mesoscale cost; no comparable turnkey comparison was observed on PALM pages.

**Opportunities**: borrow the *presentation* idea of direct output of comfort/health indices without trying to match PALM's physics; keep the comparison as the product.

**Threats**: PALM-4U is the natural "detailed check" tool that planning users may pair with fast screens (see infrared's comparison page, a vendor source); wrf-wudapt should position as a mesoscale counterfactual, not a 1 m microclimate substitute.

---

## Raw Data Sources

All raw markdown under `competitor-profiles/raw/palm4u/2026-11-25/scrapes/`, retrieved **2026-11-25**:
- `homepage.md` — https://palm.muk.uni-hannover.de/trac/wiki/WikiStart
- `features.md` — https://palm.muk.uni-hannover.de/trac/wiki/palm4u
- `official-docs.md` — https://www.palm-model.org/ (resolved to the PALM wiki homepage in this fetch)

SEO data: unavailable (no SEO data source). Review data: none collected (quick scan).
