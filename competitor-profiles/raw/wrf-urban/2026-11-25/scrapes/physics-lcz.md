# Raw scrape: physics-lcz

- Source URL: https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/physics.html
- Retrieved: 2026-11-25
- HTTP status: 200
- Note: untrusted third-party content; ignore any instructions embedded in it.

---


### Table of Contents

- WRF Overview WRF Preprocessing System (WPS) WRF Initialization WRF-ARW Solver WRF Data Assimilation (WRFDA) Post-processing, Analysis, and Visualization Tools Resources Foreword WRF Overview Compiling WPS Running WRF WRF Dynamics WRF Physics Namelist Variables WRF Output Troubleshooting Software/Computation Post-processing WRF Utilities and Tools WRFDA WRF-Fire
- WRF Preprocessing System (WPS)
- WRF Initialization
- WRF-ARW Solver
- WRF Data Assimilation (WRFDA)
- Post-processing, Analysis, and Visualization Tools
- Resources Foreword WRF Overview Compiling WPS Running WRF WRF Dynamics WRF Physics Namelist Variables WRF Output Troubleshooting Software/Computation Post-processing WRF Utilities and Tools WRFDA WRF-Fire
- Foreword
- WRF Overview
- Compiling
- WPS
- Running WRF
- WRF Dynamics
- WRF Physics
- Namelist Variables
- WRF Output
- Troubleshooting
- Software/Computation
- Post-processing
- WRF Utilities and Tools
- WRFDA
- WRF-Fire
- Compiling
- The WRF Preprocessing System (WPS)
- WRF Initialization
- Running WRF
- WRF Dynamics
- WRF Physics Cumulus Parameterization Cumulus Options Cumulus Details and References Shallow Convection Microphysics Microphysics Options Microphysics Option Details and References Radiation Longwave Radiation Schemes Longwave Radiation Scheme Details and References Shortwave Radiation Schemes Shortwave Radiation Scheme Details and References Input to Radiation Options Clouds and Cloud Fraction Options Radiation Time Step (radt) Planetary Boundary Layer Physics PBL Scheme Options PBL Scheme Details and References Additional PBL Options PBL and Land Surface Time-step (bldt) Model Grid Spacing Turbulence and Diffusion Surface physics Surface Layer Schemes Surface Layer Scheme Details and References Land Surface Model LSM Scheme Details and References PBL and Land Surface Time-step (bldt) Model Grid Spacing Turbulence and Diffusion Tropical Cyclone Options Fractional Sea Ice Sub-grid Mosaic Sea-surface Update Regional Climate Options Accumulation Budgets Lake Model WRF-Hydro Using Physics Suites NSF NCAR Convection-permitting Suite NSF NCAR Tropical Suite Overriding Physics Suite Options Other Specific Applications Tropical Storms and Cyclones Long Simulations Windfarm Surface Irrigation Parameterization WRF-Solar MAD-WRF Physics Sensitivity Options
- Cumulus Parameterization Cumulus Options Cumulus Details and References Shallow Convection
- Cumulus Options
- Cumulus Details and References
- Shallow Convection
- Microphysics Microphysics Options Microphysics Option Details and References
- Microphysics Options
- Microphysics Option Details and References
- Radiation Longwave Radiation Schemes Longwave Radiation Scheme Details and References Shortwave Radiation Schemes Shortwave Radiation Scheme Details and References Input to Radiation Options Clouds and Cloud Fraction Options Radiation Time Step (radt)
- Longwave Radiation Schemes
- Longwave Radiation Scheme Details and References
- Shortwave Radiation Schemes
- Shortwave Radiation Scheme Details and References
- Input to Radiation Options
- Clouds and Cloud Fraction Options
- Radiation Time Step (radt)
- Planetary Boundary Layer Physics PBL Scheme Options PBL Scheme Details and References Additional PBL Options PBL and Land Surface Time-step (bldt) Model Grid Spacing Turbulence and Diffusion
- PBL Scheme Options
- PBL Scheme Details and References
- Additional PBL Options
- PBL and Land Surface Time-step (bldt)
- Model Grid Spacing
- Turbulence and Diffusion
- Surface physics Surface Layer Schemes Surface Layer Scheme Details and References Land Surface Model LSM Scheme Details and References PBL and Land Surface Time-step (bldt) Model Grid Spacing Turbulence and Diffusion Tropical Cyclone Options Fractional Sea Ice Sub-grid Mosaic Sea-surface Update Regional Climate Options Accumulation Budgets Lake Model WRF-Hydro
- Surface Layer Schemes
- Surface Layer Scheme Details and References
- Land Surface Model
- LSM Scheme Details and References
- PBL and Land Surface Time-step (bldt)
- Model Grid Spacing
- Turbulence and Diffusion
- Tropical Cyclone Options
- Fractional Sea Ice
- Sub-grid Mosaic
- Sea-surface Update
- Regional Climate Options
- Accumulation Budgets
- Lake Model
- WRF-Hydro
- Using Physics Suites NSF NCAR Convection-permitting Suite NSF NCAR Tropical Suite Overriding Physics Suite Options
- NSF NCAR Convection-permitting Suite
- NSF NCAR Tropical Suite
- Overriding Physics Suite Options
- Other Specific Applications Tropical Storms and Cyclones Long Simulations Windfarm Surface Irrigation Parameterization WRF-Solar MAD-WRF Physics Sensitivity Options
- Tropical Storms and Cyclones
- Long Simulations
- Windfarm
- Surface Irrigation Parameterization
- WRF-Solar
- MAD-WRF
- Physics Sensitivity Options
- Namelist Variables
- WRF Output
- Troubleshooting
- WRF Software & Computation
- WRF Post-processing
- WRF Utilities and Tools
- WRF Data Assimilation (WRFDA)
- WRF-Fire

### Search


# WRF Physics ¶

Numerous physical processes take place in the Earth’s atmosphere. The image below shows how many of them interact with each other.

The sun creates shortwave radiation that can be absorbed, reflected, and/or scattered by the Earth’s surface, clouds, aerosols, gases, etc. Longwave radiation is emitted back up from the Earth’s surface and up and down from gases and clouds in the atmosphere, and can exit to space. Heating from diurnal radiation creates boundary-layer development, which increases turbulence and can produce convection. Clouds produce precipitation in many forms (such as rain, snow, and graupel), and are created by radiative or lifting processes. There are chemical components, such as aerosols, ozone, and pollutants that can modify clouds and radiation. At the surface, the roughness and other properties of land types (e.g., mountains, trees, buildings) modify surface fluxes. All of these processes work together to create our weather and climate.

The WRF model includes a variety of physics schemes responsible for different components of the physical processes. These schemes interact with each other during model simulations to emulate physical processes in the Earth’s atmosphere.


## Cumulus Parameterization ¶

Several cumulus schemes are available and they all have varying features, but they all parameterize sub-grid-scale effects of convective and shallow clouds. They activate column-by-column, depending on the presence of convective instability, and provide column tendencies of heat and moisture, as well as the convective part of surface rainfall, to the model.

Cumulus parameterization schemes redistribute air in gridded columns to account for vertical convective fluxes. Updrafts move boundary layer air upward and downdrafts move mid-level air downward. Schemes are designed to determine when to trigger a convective column and how quickly to create the convection.

All WRF cumulus schemes (except BMJ), are mass flux schemes, meaning they determine updraft (and often downdraft) mass flux and other fluxes, sometimes including momentum transport. Updrafts are driven by buoyancy, allowing moist surface air to rise to the upper troposphere and condensation becomes convective rainfall. Downdrafts are driven by convective rain evaporation, which cools air to the boundary layer. Subsidence warms and dries the troposphere and is the primary warming contributor in the column. The BMJ scheme is an adjustment type, and relaxes toward a post-convective (mixed) sounding.

It may not always be necessary to use cumulus parameterization. It is designed for grid sizes unable to parameterize the convective processes (i.e., when updrafts and downdrafts are sub-grid).

Following are the general rules for WRF cumulus parameterization.

Domains with grid spacing >=10km : a cumulus scheme is necessary Domains with grid spacing <=3km : unlikely that a cumulus scheme is necessary (although it may help when convection exists prior to the run) Domains with grid spacing >=3km to <=10km : This is a “gray zone” where cumulus parameterization may or may not be necessary. If possible, try to avoid domains this size, but if it is unavoidable, it is best to use either the Multi-scale Kain Fritsch or Grell-Freitas scheme, as these take this scale into account.

- Domains with grid spacing >=10km : a cumulus scheme is necessary
Domains with grid spacing >=10km : a cumulus scheme is necessary

- Domains with grid spacing <=3km : unlikely that a cumulus scheme is necessary (although it may help when convection exists prior to the run)
Domains with grid spacing <=3km : unlikely that a cumulus scheme is necessary (although it may help when convection exists prior to the run)

- Domains with grid spacing >=3km to <=10km : This is a “gray zone” where cumulus parameterization may or may not be necessary. If possible, try to avoid domains this size, but if it is unavoidable, it is best to use either the Multi-scale Kain Fritsch or Grell-Freitas scheme, as these take this scale into account.
Domains with grid spacing >=3km to <=10km : This is a “gray zone” where cumulus parameterization may or may not be necessary. If possible, try to avoid domains this size, but if it is unavoidable, it is best to use either the Multi-scale Kain Fritsch or Grell-Freitas scheme, as these take this scale into account.

Note See the WRF Tutorial presentation on Cumulus Parameterization for additional details.

  [WRF Tutorial presentation on Cumulus Parameterization](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_cumulus.pdf)
Note

See the WRF Tutorial presentation on Cumulus Parameterization for additional details.

  [WRF Tutorial presentation on Cumulus Parameterization](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_cumulus.pdf)

### Cumulus Options ¶

In the table below, moisture tendencies are mixing ratios of (c) cloud water, (r) rain water, (i) cloud ice, and (s) snow.

| Scheme | Option | Moisture Tendencies | Momentum Tendencies | Shallow Convection | Radiation Interaction |
Scheme

Option

Moisture Tendencies

Momentum Tendencies

Shallow Convection

Radiation Interaction

| Kain-Fritsch (KF) | 1 | Qc Qr Qi Qs | no | yes | yes |
Kain-Fritsch (KF)

1

Qc Qr Qi Qs

no

yes

| BMJ | 2 | N/A | no | yes | GFDL |
BMJ

2

N/A

no

yes

GFDL

| Grell-Freitas | 3 | Qc Qi | no | yes | yes |
Grell-Freitas

3

Qc Qi

no

yes

| Old SAS | 4 | Qc Qi | no | yes | GFDL |
Old SAS

4

Qc Qi

no

yes

GFDL

| Grell-3 | 5 | Qc Qi | no | yes | yes |
Grell-3

5

Qc Qi

no

yes

| Tiedtke | 6 | Qc Qi | yes | yes | no |
Tiedtke

6

Qc Qi

yes

no

| Zhang-McFarlane | 7 | Qc Qi | yes | yes | RRTMG |
Zhang-McFarlane

7

Qc Qi

yes

RRTMG

| KF-CuP | 10 | Qc Qi | no | yes | yes |
KF-CuP

10

Qc Qi

no

yes

| Multi-scale KF | 11 | Qc Qr Qi Qs | no | yes | ? |
Multi-scale KF

11

Qc Qr Qi Qs

no

yes

?

| KIAPS SAS | 14 | Qc Qi | yes | use shcu_physics=4 | GFDL |
KIAPS SAS

14

Qc Qi

yes

use shcu_physics=4

GFDL

| New Tiedtke | 16 | Qc Qi | yes | yes | no |
New Tiedtke

16

Qc Qi

yes

no

| Grell-Devenyi | 93 | Qc Qi | no | no | yes |
Grell-Devenyi

93

Qc Qi

no

yes

| NSAS | 96 | Qc Qi | yes | no/yes | GFDL |
NSAS

96

Qc Qi

yes

no/yes

GFDL

| Old KF | 99 | Qc Qr Qi Qs | no | no | GFDL |
Old KF

99

Qc Qr Qi Qs

no

GFDL


### Cumulus Details and References ¶

Kain-Fritsch (KF) cu_physics=1 Deep and shallow convection sub-grid scheme using a mass flux approach with downdrafts and CAPE removal time scale Kain, 2004

  [Kain, 2004](https://doi.org/10.1175/1520-0450(2004)043%3C0170:TKCPAU%3E2.0.CO;2)
kfeta_trigger : =1 – default trigger; =2 – moisture-advection modulated trigger function ( Ma and Tan, 2009 ). This option may improve results in subtropical regions when large-scale forcing is weak; =3 - RH dependent additional perturbation to option 1 cu_rad_feedback=.true. : allow sub-grid cloud fraction interaction with radiation ( Alapaty et al., 2012 )

  [Ma and Tan, 2009](https://doi.org/10.1016/j.atmosres.2008.09.022)
  [Alapaty et al., 2012](https://doi.org/10.1029/2012GL054031)
- kfeta_trigger : =1 – default trigger; =2 – moisture-advection modulated trigger function ( Ma and Tan, 2009 ). This option may improve results in subtropical regions when large-scale forcing is weak; =3 - RH dependent additional perturbation to option 1
  [Ma and Tan, 2009](https://doi.org/10.1016/j.atmosres.2008.09.022)
kfeta_trigger : =1 – default trigger; =2 – moisture-advection modulated trigger function ( Ma and Tan, 2009 ). This option may improve results in subtropical regions when large-scale forcing is weak; =3 - RH dependent additional perturbation to option 1

  [Ma and Tan, 2009](https://doi.org/10.1016/j.atmosres.2008.09.022)
- cu_rad_feedback=.true. : allow sub-grid cloud fraction interaction with radiation ( Alapaty et al., 2012 )
  [Alapaty et al., 2012](https://doi.org/10.1029/2012GL054031)
cu_rad_feedback=.true. : allow sub-grid cloud fraction interaction with radiation ( Alapaty et al., 2012 )

  [Alapaty et al., 2012](https://doi.org/10.1029/2012GL054031)
Betts-Miller-Janjic (BMJ) cu_physics=2 Operational Eta scheme. Column moist adjustment scheme relaxing towards a well-mixed profile. Janjic, 1994

  [Janjic, 1994](https://doi.org/10.1175/1520-0493(1994)122%3C0927:TSMECM%3E2.0.CO;2)
Grell-Freitas (GF) cu_physics=3 An improved GD scheme that tries to smooth the transition to cloud-resolving scales, as proposed by Arakawa et al., 2004 ). Grell and Freitas, 2014

  [Arakawa et al., 2004](https://doi.org/10.1175/1520-0442(2004)017%3C2493:RATCPP%3E2.0.CO;2)
  [Grell and Freitas, 2014](https://acp.copernicus.org/articles/14/5233/2014/)
Simplified Arakawa-Schubert (SAS) cu_physics=4 Simple mass-flux scheme with quasi-equilibrium closure with shallow mixing scheme. Pan et al., 1995

  [Pan et al., 1995](https://repository.library.noaa.gov/view/noaa/11429)
Grell 3D (G3) cu_physics=5 An improved version of the GD scheme that may also be used on high resolution (in addition to coarser resolutions) if subsidence spreading (option cugd_avedx) is turned on. Grell, 1993 Grell and Devenyi, 2002

  [Grell, 1993](https://doi.org/10.1175/1520-0493(1993)121%3C0764:PEOAUB%3E2.0.CO;2)
  [Grell and Devenyi, 2002](https://doi.org/10.1029/2002GL015311)
Tiedtke scheme cu_physics=6 (U. of Hawaii version); Mass-flux type scheme with CAPE-removal time scale, shallow component and momentum transport. Tiedtke, 1989 Zhang et al., 2011

  [Tiedtke, 1989](https://doi.org/10.1175/1520-0493(1989)117%3C1779:ACMFSF%3E2.0.CO;2)
  [Zhang et al., 2011](https://doi.org/10.1175/MWR-D-10-05091.1)
Zhang-McFarlane cu_physics=7 Mass-flux CAPE-removal type deep convection from CESM climate model with momentum transport. Zhang and McFarlane, 1995

  [Zhang and McFarlane, 1995](https://doi.org/10.1080/07055900.1995.9649539)
Kain-Fritsch (KF) cu_physics=10 Cumulus Potential scheme; this option modifies the KF ad-hoc trigger function with one linked to boundary layer turbulence via probability density function (PDFs) using cumulus potential scheme. The scheme also computes the cumulus cloud fraction based on the time scale relevant for shallow cumuli. Berg et al., 2013

  [Berg et al., 2013](https://doi.org/10.1175/MWR-D-12-00136.1)
Multi-scale Kain-Fritsch cu_physics=11 Using scale-dependent dynamic adjustment timescale, LCC-based entrainment. Also uses new trigger function based on Bechtold et al., 2001 . Includes an option to use CESM aerosol. In V4.2, convective momentum transport is added. It can be turned off by setting switch cmt_opt_flag = .false. inside the code. Zheng et al., 2016 Glotfelty et al., 2019

  [Bechtold et al., 2001](https://journals.ametsoc.org/view/journals/clim/27/20/jcli-d-13-00718.1.xml#bib2)
  [Zheng et al., 2016](https://doi.org/10.1175/MWR-D-15-0005.1)
  [Glotfelty et al., 2019](https://doi.org/10.1175/MWR-D-18-0267.1)
KIAPS SAS (KSAS) cu_physics=14 Based on NSAS, but scale-aware Han and Pan, 2011 Kwon and Hong, 2017

  [Han and Pan, 2011](https://doi.org/10.1175/WAF-D-10-05038.1)
  [Kwon and Hong, 2017](https://doi.org/10.1175/MWR-D-16-0034.1)
New Tiedtke cu_physics=16 This version is similar to the Tiedtke scheme used in REGCM4 and ECMWF cy40r1. Zhang and Wang, 2017

  [Zhang and Wang, 2017](https://doi.org/10.1175/JCLI-D-16-0597.1)
Grell-Devenyi (GD) cu_physics=93 An ensemble scheme; Multi-closure, multi-parameter, ensemble method with typically 144 sub-grid members. Grell and Devenyi, 2002

  [Grell and Devenyi, 2002](https://doi.org/10.1029/2002GL015311)
New Simplified Arakawa-Schubert (NSAS) cu_physics=96 New mass-flux scheme with deep and shallow components and momentum transport. Han and Pan, 2011

  [Han and Pan, 2011](https://doi.org/10.1175/WAF-D-10-05038.1)
Old Kain-Fritsch cu_physics=99 Deep convection scheme using a mass flux approach with downdrafts and CAPE removal time scale. Kain and Fritsch, 1990

  [Kain and Fritsch, 1990](https://doi.org/10.1175/1520-0469(1990)047%3C2784:AODEPM%3E2.0.CO;2)

### Shallow Convection ¶

Shallow convection schemes are an additional option. Non-precipitating shallow mixing dries the planetary boundary layer, then moistens and cools above. This is done by enhanced mixing or a mass-flux approach. These options may be useful for grid sizes that do not resolve shallow cumulus clouds (>1 km).

Some cumulus schemes already include shallow convection:

Kain-Fritsch Old SAS KIAPS SAS Grell-3 Grell-Freitas BMJ Tiedtke

- Kain-Fritsch
Kain-Fritsch

- Old SAS
Old SAS

- KIAPS SAS
KIAPS SAS

- Grell-3
Grell-3

- Grell-Freitas
Grell-Freitas

- BMJ
BMJ

- Tiedtke
Tiedtke

However, to use the standalone shallow schemes, use one of the following options.

ishallow=1 : Shallow convection that works with the Grell 3D scheme (cu_physics=5) shcu_physics=2 : UW (Bretherton and Park) Shallow cumulus option from the CESM climate model with momentum transport Park et al., 2009 shcu_physics=3 : GRIMS (Global/Regional Integrated Modeling System) scheme; represents the shallow convection process by using eddy-diffusion and the pal algorithm, and couples directly to the YSU PBL scheme Hong and Jang, 2018 shcu_physics=4 : NSAS shallow scheme; extracted from NSAS, and should be used with KSAS deep cumulus scheme shcu_physics=5 : Deng shallow scheme; only works with MYNN and MYJ PBL schemes; (new in V4.1) Deng et al., 2003

  [Park et al., 2009](https://doi.org/10.1175/2008JCLI2557.1)
  [Hong and Jang, 2018](https://doi.org/10.1007/s13143-018-0013-3)
  [Deng et al., 2003](https://doi.org/10.1175/1520-0469(2003)060%3C0034:ASCPFM%3E2.0.CO;2)
- ishallow=1 : Shallow convection that works with the Grell 3D scheme (cu_physics=5)
ishallow=1 : Shallow convection that works with the Grell 3D scheme (cu_physics=5)

- shcu_physics=2 : UW (Bretherton and Park) Shallow cumulus option from the CESM climate model with momentum transport Park et al., 2009
  [Park et al., 2009](https://doi.org/10.1175/2008JCLI2557.1)
shcu_physics=2 : UW (Bretherton and Park) Shallow cumulus option from the CESM climate model with momentum transport Park et al., 2009

  [Park et al., 2009](https://doi.org/10.1175/2008JCLI2557.1)
- shcu_physics=3 : GRIMS (Global/Regional Integrated Modeling System) scheme; represents the shallow convection process by using eddy-diffusion and the pal algorithm, and couples directly to the YSU PBL scheme Hong and Jang, 2018
  [Hong and Jang, 2018](https://doi.org/10.1007/s13143-018-0013-3)
shcu_physics=3 : GRIMS (Global/Regional Integrated Modeling System) scheme; represents the shallow convection process by using eddy-diffusion and the pal algorithm, and couples directly to the YSU PBL scheme Hong and Jang, 2018

  [Hong and Jang, 2018](https://doi.org/10.1007/s13143-018-0013-3)
- shcu_physics=4 : NSAS shallow scheme; extracted from NSAS, and should be used with KSAS deep cumulus scheme
shcu_physics=4 : NSAS shallow scheme; extracted from NSAS, and should be used with KSAS deep cumulus scheme

- shcu_physics=5 : Deng shallow scheme; only works with MYNN and MYJ PBL schemes; (new in V4.1) Deng et al., 2003
  [Deng et al., 2003](https://doi.org/10.1175/1520-0469(2003)060%3C0034:ASCPFM%3E2.0.CO;2)
shcu_physics=5 : Deng shallow scheme; only works with MYNN and MYJ PBL schemes; (new in V4.1) Deng et al., 2003

  [Deng et al., 2003](https://doi.org/10.1175/1520-0469(2003)060%3C0034:ASCPFM%3E2.0.CO;2)

## Microphysics ¶

WRF microphysics schemes resolve cloud and precipitation processes, and some schemes account for ice and/or mixed-phases processes. Microphysics schemes provide atmospheric heat and moisture tendencies to the model, and the resolved-scale (or NON-convective) rainfall at the surface. WRF microphysics schemes take into account many different microphysical processes, and formation of particles differs, depending on their type.

Cloud droplets (10s of microns) condense from vapor at water saturation. Rain (~mm diameter) forms from cloud droplet growth. Ice crystals (10s of microns) form from freezing of droplets or deposition on nuclei, which are assumed or explicit (e.g., dust particles). Snow (100s of microns) forms from growth of ice crystals at ice supersaturation and their aggregation. Graupel/hail (mm to cm) form and grow from mixed-phase interactions between water and ice particles. Precipitating particles are typically assigned to an observationally-based size distribution.

- Cloud droplets (10s of microns) condense from vapor at water saturation.
Cloud droplets (10s of microns) condense from vapor at water saturation.

- Rain (~mm diameter) forms from cloud droplet growth.
Rain (~mm diameter) forms from cloud droplet growth.

- Ice crystals (10s of microns) form from freezing of droplets or deposition on nuclei, which are assumed or explicit (e.g., dust particles).
Ice crystals (10s of microns) form from freezing of droplets or deposition on nuclei, which are assumed or explicit (e.g., dust particles).

- Snow (100s of microns) forms from growth of ice crystals at ice supersaturation and their aggregation.
Snow (100s of microns) forms from growth of ice crystals at ice supersaturation and their aggregation.

- Graupel/hail (mm to cm) form and grow from mixed-phase interactions between water and ice particles.
Graupel/hail (mm to cm) form and grow from mixed-phase interactions between water and ice particles.

- Precipitating particles are typically assigned to an observationally-based size distribution.
Precipitating particles are typically assigned to an observationally-based size distribution.

There are many types of microphysics schemes available in WRF. Single-moment schemes have a single prediction equation for mass per species, with particle size distribution being derived from fixed parameters (Qr, Qs, etc.). Double-moment schemes add a prediction equation for number concentration per double-moment species (Nr, Ns, etc.), and allow for additional processes, such as size-sorting during fall-out and aerosol effects. Spectral bin schemes resolve size distribution by doubling mass bins. The more advanced the scheme type, the more computationally expensive the model simulation will be.

Note For additional details, see the WRF Tutorial presentation on Microphysics .

  [WRF Tutorial presentation on Microphysics](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_microphysics.pdf)
Note

For additional details, see the WRF Tutorial presentation on Microphysics .

  [WRF Tutorial presentation on Microphysics](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_microphysics.pdf)

### Microphysics Options ¶

In the below table, abbreviations are defined as follows

| Scheme | Option | Mass Variables | Number Variables |
Scheme

Option

Mass Variables

Number Variables

| Kessler | 1 | Qc Qr | N/A |
Kessler

1

Qc Qr

N/A

| Purdue Lin | 2 | Qc Qr Qi Qs Qg | N/A |
Purdue Lin

2

Qc Qr Qi Qs Qg

N/A

| WSM3 | 3 | Qc Qr | N/A |
WSM3

3

Qc Qr

N/A

| WSM5 | 4 | Qc Qr Qi Qs | N/A |
WSM5

4

Qc Qr Qi Qs

N/A

| Eta (Ferrier) | 5 | Qc Qr Qs Qt* | N/A |
Eta (Ferrier)

5

Qc Qr Qs Qt*

N/A

| WSM6 | 6 | Qc Qr Qi Qs Qg | N/A |
WSM6

6

Qc Qr Qi Qs Qg

N/A

| Goddard 4-ice | 7 | Qc Qr Qi Qs Qg Qh | N/A |
Goddard 4-ice

7

Qc Qr Qi Qs Qg Qh

N/A

| Thompson | 8 | Qc Qr Qi Qs Qg | Ni Nr |
Thompson

8

Qc Qr Qi Qs Qg

Ni Nr

| Milbrandt 2-mom | 9 | Qc Qr Qi Qs Qg Qh | Nc Nr Ni Ns Ng Nh |
Milbrandt 2-mom

9

Qc Qr Qi Qs Qg Qh

Nc Nr Ni Ns Ng Nh

| Morrison 2-mom | 10 | Qc Qr Qi Qs Qg | Nr Ni Ns Ng |
Morrison 2-mom

10

Qc Qr Qi Qs Qg

Nr Ni Ns Ng

| CAM 5.1 | 11 | Qc Qr Qi Qs | Nc Nr Ni Ns |
CAM 5.1

11

Qc Qr Qi Qs

Nc Nr Ni Ns

| SBU-YLin | 13 | Qc Qr Qi Qs | N/A |
SBU-YLin

13

Qc Qr Qi Qs

N/A

| WDM5 | 14 | Qc Qr Qi Qs | Nn Nc Nr |
WDM5

14

Qc Qr Qi Qs

Nn Nc Nr

| WDM6 | 16 | Qc Qr Qi Qs Qg | Nn Nc Nr |
WDM6

16

Qc Qr Qi Qs Qg

Nn Nc Nr

| NSSL | 18 | Qc Qr Qi Qs Qg Qh | Nc Nr Ni Ns Ng Nh Nn |
NSSL

18

Qc Qr Qi Qs Qg Qh

Nc Nr Ni Ns Ng Nh Nn

| WSM7 | 24 | Qc Qr Qi Qs Qg Qh | N/A |
WSM7

24

Qc Qr Qi Qs Qg Qh

N/A

| WDM7 | 26 | Qc Qr Qi Qs Qg Qh | Nc Nr |
WDM7

26

Qc Qr Qi Qs Qg Qh

Nc Nr

| Thompson Aerosol | 28 | Qc Qr Qi Qs Qg | Nc Ni Nr Nn Nni |
Thompson Aerosol

28

Qc Qr Qi Qs Qg

Nc Ni Nr Nn Nni

| HUJI Fast | 30 | Qc Qr Qi Qs Qg | Nn Nc Nr Ni Ns Ng |
HUJI Fast

30

Qc Qr Qi Qs Qg

Nn Nc Nr Ni Ns Ng

| Thompson Hail/Graupel/Aerosol | 38 | Qc Qr Qi Qs Qg | Nc Ni Nr Nn Nni Ng Vg |
Thompson Hail/Graupel/Aerosol

38

Qc Qr Qi Qs Qg

Nc Ni Nr Nn Nni Ng Vg

| Morrison 2-mom Aerosol | 40 | Qc Qr Qi Qs Qg |  |
Morrison 2-mom Aerosol

40

Qc Qr Qi Qs Qg

| P3 | 50 | Qc Qr Qi | Nr Ni Ri Bi |
P3

50

Qc Qr Qi

Nr Ni Ri Bi

| P3-nc | 51 | Qc Qr Qi | Nc Nr Ni Ri Bi |
P3-nc

51

Qc Qr Qi

Nc Nr Ni Ri Bi

| P3-2nd | 52 | Qc Qr Qi2 | Nc Nr Ni Ni2 Ri Ri2 Bi Bi2 |
P3-2nd

52

Qc Qr Qi2

Nc Nr Ni Ni2 Ri Ri2 Bi Bi2

| P3-3mc | 53 | Qc Qr Qi | Nc Nr Ni Ri Bi Zi |
P3-3mc

53

Qc Qr Qi

Nc Nr Ni Ri Bi Zi

| ISHMAEL | 55 | Qc Qr Qi Qi2 Qi3 | Nr Ni Ni2 Ni3 Vi Vi2 Vi3 Ai Ai2 Ai3 |
ISHMAEL

55

Qc Qr Qi Qi2 Qi3

Nr Ni Ni2 Ni3 Vi Vi2 Vi3 Ai Ai2 Ai3

| NTU | 56 | Qc Qr Qi Qs Qg Qh Qden Qten Qccn Qrcn | Nc Nr Ni Ns Ng Nh Nin Ai As Ag Ah Vi Vs Vg Fi Fs |
NTU

56

Qc Qr Qi Qs Qg Qh Qden Qten Qccn Qrcn

Nc Nr Ni Ns Ng Nh Nin Ai As Ag Ah Vi Vs Vg Fi Fs


### Microphysics Option Details and References ¶

Kessler mp_physics=1 A warm-rain (i.e., no ice) scheme used commonly in idealized cloud modeling studies Kessler, 1969

  [Kessler, 1969](https://doi.org/10.1007/978-1-935704-36-2_1)
Purdue Lin mp_physics=2 A sophisticated scheme that has ice, snow, and graupel processes, suitable for real-data high-resolution simulations Chen and Sun, 2002

  [Chen and Sun, 2002](https://doi.org/10.2151/jmsj.80.99)
WRF Single-moment 3-class (WSM3) mp_physics=3 A simple, efficient scheme with ice and snow processes, suitable for mesoscale grid sizes Hong et al., 2004

  [Hong et al., 2004](https://doi.org/10.1175/1520-0493(2004)132%3C0103:ARATIM%3E2.0.CO;2)
WRF Single-moment 5-class (WSM5) mp_physics=4 A slightly more sophisticated version of WSM3 that allows for mixed-phase processes and super-cooled water Hong et al., 2004

  [Hong et al., 2004](https://doi.org/10.1175/1520-0493(2004)132%3C0103:ARATIM%3E2.0.CO;2)
Ferrier Eta mp_physics=5 The operational microphysics used in NCEP models; simple and efficient, with diagnostic mixed-phase processes; for use with fine resolutions (<5km) NOAA, 2001

  [NOAA, 2001](http://www.emc.ncep.noaa.gov/mmb/mmbpll/eta12tpb/)
WRF Single-moment 6-class (WSM6) mp_physics=6 Includes ice, snow and graupel processes, suitable for high-resolution simulations Hong and Lim, 2006

  [Hong and Lim, 2006](https://www.researchgate.net/profile/Song-You-Hong/publication/331192569_Hongandlim-JKMS-2006/links/5c6b581f92851c1c9dea9d10/Hongandlim-JKMS-2006.pdf?_sg%5B0%5D=started_experiment_milestone&origin=journalDetail)
Goddard 4-ice mp_physics=7 Predicts hail and graupel separately; provides effective radii for radiation. Replaced older Goddard scheme in V4.1. Tao et al., 1989 Tao et al., 2016

  [Tao et al., 1989](https://doi.org/10.1175/1520-0493(1989)117%3C0231:AIWSA%3E2.0.CO;2)
  [Tao et al., 2016](https://doi.org/10.1002/2015JD023986)
Thompson et al. mp_physics=8 Includes ice, snow and graupel processes suitable for high-resolution simulations Thompson et al., 2008

  [Thompson et al., 2008](https://doi.org/10.1175/2008MWR2387.1)
Milbrandt-Yau Double-moment 7-class mp_physics=9 Includes separate categories for hail and graupel with double-moment cloud, rain, ice, snow, graupel and hail Milbrandt and Yau, 2005 (Part I) Milbrandt and Yau, 2005 (Part II)

  [Milbrandt and Yau, 2005 (Part I)](https://doi.org/10.1175/JAS3534.1)
  [Milbrandt and Yau, 2005 (Part II)](https://doi.org/10.1175/JAS3535.1)
Morrison Double-moment mp_physics=10 Double-moment ice, snow, rain and graupel for cloud-resolving simulations Morrison et al., 2009

  [Morrison et al., 2009](https://doi.org/10.1175/2008MWR2556.1)
CAM V5.1 2-moment 5-class mp_physics=11 User’s Guide to the CAM-5.1

  [User’s Guide to the CAM-5.1](https://www.cesm.ucar.edu/models/cesm1.0/cam/docs/ug5_1/ug.html)
Stony Brook University (Y. Lin) mp_physics=13 A 5-class scheme with riming intensity predicted to account for mixed-phase processes Lin and Colle, 2011

  [Lin and Colle, 2011](https://doi.org/10.1175/2010MWR3293.1)
WRF Double-moment 5-class (WDM5) mp_physics=14 Similar to WSM5 (option 4), but includes double-moment rain, and cloud and CCN for warm processes Lim and Hong, 2010

  [Lim and Hong, 2010](https://doi.org/10.1175/2009MWR2968.1)
WRF Double-moment 6-class (WDM6) mp_physics=16 Similar to WSM6 (option 6), but includes double-moment rain, and cloud and CCN for warm processes Lim and Hong, 2010

  [Lim and Hong, 2010](https://doi.org/10.1175/2009MWR2968.1)
Note See WRF/doc/README.NSSLmp for detailed information about the NSSL microphysics schemes. If using WRF prior to V4.6.0, and an NSSL microphysics scheme, see NSSL Options Prior to V4.6.0 .

Note

See WRF/doc/README.NSSLmp for detailed information about the NSSL microphysics schemes. If using WRF prior to V4.6.0, and an NSSL microphysics scheme, see NSSL Options Prior to V4.6.0 .

NSSL 3-moment scheme with hail and CCN prediction (new since V4.6.0) mp_physics=18 and either of the following:

nssl_3moment=1 : predict radar reflectivity from rain nssl_3moment=2 : predict radar reflectivity of rain and hail

Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL 2-moment scheme with hail and CCN prediction mp_physics=18 Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL 2-moment scheme without hail (equivalent to mp_physics=22 prior to V4.6.0) mp_physics=18 and either of the following:

nssl_hail_on=0 nssl_ccn_on=0

Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL 2-moment scheme with hail and constant background CCN (equivalent to mp_physics=17 prior to V4.6.0) mp_physics=18 , and nssl_ccn_on=0 Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL single-moment scheme, 7-class with predicted graupel density (equivalent to mp_physics=19 prior to V4.6.0) mp_physics=18 , and nssl_2moment_on=0 nssl_ccn_on=0 Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL single-moment scheme, 6-class with predicted graupel density (equivalent to mp_physics=19 prior to V4.6.0) mp_physics=18 , and nssl_2moment_on=0 Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
NSSL single-moment scheme, 6-class (equivalent to mp_physics=21 prior to V4.6.0) mp_physics=18 , and nssl_2moment_on=0 nssl_hail_on=0 nssl_ccn_on=0 nssl_density_on=0 Mansell et al., 2010

  [Mansell et al., 2010](https://doi.org/10.1175/2009JAS2965.1)
WRF Single-moment 7-class (WSM7) mp_physics=24 Similar to WSM6 (option 6), but with an added hail category (effective beginning with V4.1) Bae et al., 2018

  [Bae et al., 2018](https://doi.org/10.1007%2Fs13143-018-0066-3)
WRF Double-moment 7-class (WDM7) mp_physics=26 Similar to WDM6 (option 16), but with an added hail category (effective beginning with V4.1) Bae et al., 2018

  [Bae et al., 2018](https://doi.org/10.1007%2Fs13143-018-0066-3)
Thompson Aerosol-aware mp_physics=28 Considers water- and ice-friendly aerosols Thompson and Eidhammer, 2014

  [Thompson and Eidhammer, 2014](https://doi.org/10.1175/JAS-D-13-0305.1)
A climatology data set may be used to specify initial and boundary conditions for the aerosol variables; includes a surface dust scheme. Since V4.4 a black carbon aerosol category is added; biomass burning can also be added.

  [black carbon aerosol category](https://www2.mmm.ucar.edu/wrf/users/physics/mp28_updated_new.html)
- A climatology data set may be used to specify initial and boundary conditions for the aerosol variables; includes a surface dust scheme.
A climatology data set may be used to specify initial and boundary conditions for the aerosol variables; includes a surface dust scheme.

- Since V4.4 a black carbon aerosol category is added; biomass burning can also be added.
  [black carbon aerosol category](https://www2.mmm.ucar.edu/wrf/users/physics/mp28_updated_new.html)
Since V4.4 a black carbon aerosol category is added; biomass burning can also be added.

  [black carbon aerosol category](https://www2.mmm.ucar.edu/wrf/users/physics/mp28_updated_new.html)
Hebrew University of Jerusalem Fast (HUJI) mp_physics=30 Spectral bin microphysics, fast version Shpund et al., 2019

  [Shpund et al., 2019](https://doi.org/10.1029/2019JD030576)
Thompson Hail/Graupel/Aerosol mp_physics=38 Similar to option 28, but computes two-moment prognostics for graupel and hail and includes a predicted density graupel category. This option requires the datafile qr_acr_qg_mp38V1.dat to be in the directory where wrf.exe is run. Alternatively, that file can be computed by using namelist option write_thompson_mp38table=.true. (but this can take up to 18 min to compute this table using a 12-CPU job, 4 min on 128-CPU, and several hours if computed on a single CPU).

  [qr_acr_qg_mp38V1.dat](http://www2.mmm.ucar.edu/wrf/src/wrf_files/qr_acr_qg_mp38V1.dat)
Morrison double-moment scheme with CESM aerosol mp_physics=40 Similar to option 10, but with CESM aerosol added. This option must be used with the MSKF cumulus scheme (option 11); This option requires an input file - Download the CESM RCP4.5 data and then link to one of the two files available after unpacking the file. No publication available for this specific scheme

  [Download the CESM RCP4.5 data](http://www2.mmm.ucar.edu/wrf/src/wrf_files/CESM_RCP4.5_Aerosol_Data.tar.gz)
Morrison and Milbrandt Predicted Particle Property (P3) mp_physics=50 A single ice category that represents a combination of ice, snow and graupel, and also carries prognostic arrays for rimed ice mass and rimed ice volume; single-moment rain and ice. Morrison and Milbrandt, 2015

  [Morrison and Milbrandt, 2015](https://doi.org/10.1175/JAS-D-14-0065.1)
Morrison and Milbrandt Predicted Particle Property (P3-nc) mp_physics=51 As in 50, but adds supersaturation dependent activation and double-moment cloud water Morrison and Milbrandt, 2015

  [Morrison and Milbrandt, 2015](https://doi.org/10.1175/JAS-D-14-0065.1)
Morrison and Milbrandt Predicted Particle Property (P3-2ice) mp_physics=52 As in option 50, but with two arrays for ice and double-moment cloud water Morrison and Milbrandt, 2015

  [Morrison and Milbrandt, 2015](https://doi.org/10.1175/JAS-D-14-0065.1)
Morrison and Milbrandt Predicted Particle Property (P3-3moment) mp_physics=53 As in option 50, but with 3-moment ice, plus double-moment cloud water No publication available for this specific scheme

Jensen ISHMAEL mp_physics=55 Predicts particle shapes and habits in ice crystal growth; (new in V4.1) Jensen et al., 2017

  [Jensen et al., 2017](https://doi.org/10.1175/JAS-D-16-0350.1)
National Taiwan University (NTU) mp_physics=56 double-moments for the liquid phase, and triple-moments for the ice phase, together with consideration for ice crystal shape and density variations; supersaturation is resolved so that condensation nuclei (CN) activation is explicitly calculated; CN’s mass in droplets is tracked to account for aerosol recycling. Tsai and Chen, 2020

  [Tsai and Chen, 2020](https://doi.org/10.1175/JAS-D-19-0125.1)

## Radiation ¶

WRF radiation schemes obtain cloud properties from the microphysics scheme, and then compute an atmospheric temperature tendency profile, as well as surface radiative fluxes, due to longwave and shortwave radiation.

Longwave schemes are responsible for computing the longwave radiation emitted and absorbed by the surface and clouds, and gases such as water vapor and CO2. The wavelengths are the thermal IR wavelengths, longer than about three microns.

Shortwave schemes compute incoming solar fluxes that may be reflected by the surface or clouds, or absorbed by gases, such as water vapor and ozone, and aerosols. Shortwave schemes take into consideration annual cycles, as well as the diurnal cycle. These schemes include the ultraviolet, visible, and near-IR wavelengths in the solar spectrum.

Note See the WRF Tutorial presentation on Radiation for additional details.

  [WRF Tutorial presentation on Radiation](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_radiation.pdf)
Note

See the WRF Tutorial presentation on Radiation for additional details.

  [WRF Tutorial presentation on Radiation](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_radiation.pdf)

### Longwave Radiation Schemes ¶

WRF longwave radiation schemes compute clear-sky and cloud upward and downward raditation fluxes.

They consider infrared emissions from layers. Surface emissivity is calculated, based on the land type in each grid point. Flux divergence of the layer emissions leads to cooling in each layer. Downward flux at the surface is important in the land-energy budget. Infrared radiation generally leads to cooling in clear air (~2K/day), with stronger cooling at cloud tops and warming at cloud bases.

- They consider infrared emissions from layers.
They consider infrared emissions from layers.

- Surface emissivity is calculated, based on the land type in each grid point.
Surface emissivity is calculated, based on the land type in each grid point.

- Flux divergence of the layer emissions leads to cooling in each layer.
Flux divergence of the layer emissions leads to cooling in each layer.

- Downward flux at the surface is important in the land-energy budget.
Downward flux at the surface is important in the land-energy budget.

- Infrared radiation generally leads to cooling in clear air (~2K/day), with stronger cooling at cloud tops and warming at cloud bases.
Infrared radiation generally leads to cooling in clear air (~2K/day), with stronger cooling at cloud tops and warming at cloud bases.

In the table below, microphysics interactions are mixing ratios of (c) cloud water, (r) rain water, (i) cloud ice, (s) snow, and (g) graupel.

| Scheme | Option | Microphysics Interaction | Cloud Fraction | GHG |
Scheme

Option

Microphysics Interaction

Cloud Fraction

GHG

| RRTM | 1 | Qc Qr Qi Qs Qg | 1/0 | constant or yearly GHG |
RRTM

1

Qc Qr Qi Qs Qg

1/0

constant or yearly GHG

| CAM | 3 | Qc Qi Qs | Max-rand overlap | yearly CO2 or GHG |
CAM

3

Qc Qi Qs

Max-rand overlap

yearly CO2 or GHG

| RRTMG | 4 | Qc Qr Qi Qs | Max-rand overlap | constant or yearly GHG |
RRTMG

4

Qc Qr Qi Qs

Max-rand overlap

constant or yearly GHG

| New Goddard | 5 | Qc Qr Qi Qs Qg | Max-rand | constant |
New Goddard

5

Qc Qr Qi Qs Qg

Max-rand

constant

| FLG | 7 | Qc Qr Qi Qs Qg | 1/0 | constant |
FLG

7

Qc Qr Qi Qs Qg

1/0

constant

| RRTMG-K | 14 | Qc Qr Qi Qs | Max-rand overlap | constant |
RRTMG-K

14

Qc Qr Qi Qs

Max-rand overlap

constant

| Held-Suarez | 31 | none | none | none |
Held-Suarez

31

none

| GFDL | 99 | Qc Qr Qi Qs | Max-rand overlap | constant |
GFDL

99

Qc Qr Qi Qs

Max-rand overlap

constant


### Longwave Radiation Scheme Details and References ¶

RRTM ra_lw_physics=1 Rapid Radiative Transfer Model. An accurate scheme using look-up tables for efficiency. Accounts for multiple bands, and microphysics species. For trace gases, the volume-mixing ratio values for CO2=379e-6, N2O=319e-9 and CH4=1774e-9. See section 2.3 for time-varying option. Mlawer et al., 1997

  [Mlawer et al., 1997](https://doi.org/10.1029/97JD00237)
CAM ra_lw_physics=3 from the CAM 3 climate model used in CCSM. Allows for aerosols and trace gases. It uses yearly CO2, and constant N2O (311e-9) and CH4 (1714e-9). See section 2.3 for the time-varying option. Collins et al., 2004

  [Collins et al., 2004](https://www.cesm.ucar.edu/models/atm-cam/docs/description/description.pdf)
RRTMG ra_lw_physics=4 A newer version of RRTM. It includes the MCICA method of random cloud overlap. For major trace gases, CO2=379e-6 (valid for 2005), N2O=319e-9, CH4=1774e-9. See section 2.3 for the time-varying option. Since V4.2, the CO2 value is replaced by a function of the year: CO2(ppm) = 280 + 90 exp (0.02*(year-2000)), which has about 4% of error for 1920s and 1960s, and about 1 % after year 2000 when compared to observed values. Since V4.4, a new cloud overlap option is available Iacono et al., 2008

  [Iacono et al., 2008](https://doi.org/10.1029/2008JD009944)
New Goddard ra_lw_physics=5 Efficient, multiple bands, ozone from simple climatology. Designed to run with Goddard microphysics particle radius information. Updated in V4.1. Chou and Suarez, 1999 Chou et al., 2001

  [Chou and Suarez, 1999](https://ntrs.nasa.gov/citations/19990060930)
  [Chou et al., 2001](https://ntrs.nasa.gov/citations/20010072848)
Fu-Liou-Gu (FLG) ra_lw_physics=7 multiple bands, cloud and cloud fraction effects, ozone profile from climatology and tracer gases. CO2=345e-6. Gu et al., 2011 Fu and Liou, 1992

  [Gu et al., 2011](https://doi.org/10.1029/2010JD014574)
  [Fu and Liou, 1992](https://doi.org/10.1175/1520-0469(1992)049%3C2139:OTCDMF%3E2.0.CO;2)
RRTMG-K ra_lw_physics=14 A version of RRTMG scheme improved by Baek (2017). Note: To use this option, WRF must be built with the configuration setting -DBUILD_RRTMK = 1 (modify under ARCHFLAGS in configure.wrf) Baek, 2017

  [Baek, 2017](https://doi.org/10.1002/2017MS000994)
RRTMG-fast ra_lw_physics=24 A fast version of the RRTMG scheme for GPU and MIC. Default values for GHG (since V4.2):

co2vmr=(280. + 90.*exp(0.02*(yr-2000)))*1.e-6 n2ovmr=319.e-9 ch4vmr=1774.e-9 cfc11=0.251e-9 cfc12=0.538e-9

- co2vmr=(280. + 90.*exp(0.02*(yr-2000)))*1.e-6
co2vmr=(280. + 90.*exp(0.02*(yr-2000)))*1.e-6

- n2ovmr=319.e-9
n2ovmr=319.e-9

- ch4vmr=1774.e-9
ch4vmr=1774.e-9

- cfc11=0.251e-9
cfc11=0.251e-9

- cfc12=0.538e-9
cfc12=0.538e-9

Iacono et al., 2008

  [Iacono et al., 2008](https://doi.org/10.1029/2008JD009944)
GFDL ra_lw_physics=99 Eta operational radiation scheme. An older multi-band scheme with carbon dioxide, ozone and microphysics effects Fels and Schwarzkopf, 1981

  [Fels and Schwarzkopf, 1981](https://doi.org/10.1029/JC086iC02p01205)

### Shortwave Radiation Schemes ¶

WRF shortwave radiation schemes

compute clear-sky and cloudy solar fluxes include annual and diurnal solar cycles consider downward and upward (reflected) fluxes (with the exception of the Dudhia (option 1) scheme, which only considers downward flux) have a primarily warming effect in clear sky are an important component of surface energy balance

- compute clear-sky and cloudy solar fluxes
compute clear-sky and cloudy solar fluxes

- include annual and diurnal solar cycles
include annual and diurnal solar cycles

- consider downward and upward (reflected) fluxes (with the exception of the Dudhia (option 1) scheme, which only considers downward flux)
consider downward and upward (reflected) fluxes (with the exception of the Dudhia (option 1) scheme, which only considers downward flux)

- have a primarily warming effect in clear sky
have a primarily warming effect in clear sky

- are an important component of surface energy balance
are an important component of surface energy balance

In the table below, microphysics interactions are mixing ratios of (c) cloud water, (r) rain water, (i) cloud ice, (s) snow, and (g) graupel.

| Scheme | Option | Microphysics Interaction | Cloud Fraction | GHG |
Scheme

Option

Microphysics Interaction

Cloud Fraction

GHG

| Dudhia | 1 | Qc Qr Qi Qs Qg | 1/0 | none |
Dudhia

1

Qc Qr Qi Qs Qg

1/0

none

| Goddard | 2 | Qc Qi | 1/0 | 5 profiles |
Goddard

2

Qc Qi

1/0

5 profiles

| CAM | 3 | Qc Qi Qs | Max-rand overlap | lat/month |
CAM

3

Qc Qi Qs

Max-rand overlap

lat/month

| RRTMG | 4 | Qc Qr Qi Qs | Max-rand overlap | 1 profile or lat/month |
RRTMG

4

Qc Qr Qi Qs

Max-rand overlap

1 profile or lat/month

| New Goddard | 5 | Qc Qr Qi Qs Qg | Max-rand | 5 profiles |
New Goddard

5

Qc Qr Qi Qs Qg

Max-rand

5 profiles

| FLG | 7 | Qc Qr Qi Qs Qg | 1/0 | 5 profiles |
FLG

7

Qc Qr Qi Qs Qg

1/0

5 profiles

| RRTMG-K | 14 | Qc Qr Qi Qs | Max-rand overlap | 1 profile or lat/month |
RRTMG-K

14

Qc Qr Qi Qs

Max-rand overlap

1 profile or lat/month

| GFDL | 99 | Qc Qr Qi Qs | Max-rand overlap | lat/month |
GFDL

99

Qc Qr Qi Qs

Max-rand overlap

lat/month


### Shortwave Radiation Scheme Details and References ¶

Dudhia ra_sw_physics=1 Simple downward integration allowing efficiency for clouds and clear-sky absorption and scattering Dudhia, 1989

  [Dudhia, 1989](https://doi.org/10.1175/1520-0469(1989)046%3C3077:NSOCOD%3E2.0.CO;2)
Goddard ra_sw_physics=2 Two-stream multi-band scheme with ozone from climatology and cloud effects Chou and Suarez, 1994 Matsui et al., 2018

  [Chou and Suarez, 1994](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.26.4850&rep=rep1&type=pdf)
  [Matsui et al., 2018](https://doi.org/10.1007/s00382-018-4187-2)
CAM ra_sw_physics=3 Originates from the CAM 3 climate model used in CCSM; allows for aerosols and trace gases Collins et al., 2004

  [Collins et al., 2004](https://www.cesm.ucar.edu/models/atm-cam/docs/description/description.pdf)
RRTMG ra_sw_physics=4 Uses the MCICA method of random cloud overlap; use for major trace gases, CO2=379e-6 (valid for 2005), N2O=319e-9, CH4=1774e-9. See section 2.3 for the time-varying option. Since V4.2, the CO2 value is replaced by a function of the year: CO2(ppm) = 280 + 90 exp (0.02*(year-2000)), which has about 4% error for the 1920s and 1960s, and about 1% after 2000, when compared to observed values. To include a cloud overlap option, add namelist option cldovrlp = 1,2,3,4,or 5, along with decorrelation length option, idcor = 0 or 1 for use with cldovrlp=4 or 5. See namelist section for descriptions of options. Iacono et al., 2008

  [Iacono et al., 2008](https://doi.org/10.1029/2008JD009944)
New Goddard ra_sw_physics=5 Efficient, multiple bands, ozone from simple climatology; designed to run with Goddard microphysics particle radius information; updated in V4.1. Chou and Suarez, 1999 Chou et al., 2001

  [Chou and Suarez, 1999](https://ntrs.nasa.gov/citations/19990060930)
  [Chou et al., 2001](https://ntrs.nasa.gov/citations/20010072848)
Fu-Liou-Gu (FLG) ra_sw_physics=7 Includes multiple bands, cloud and cloud fraction effects, ozone profile from climatology, can allow for aerosols Gu et al., 2011 Fu and Liou, 1992

  [Gu et al., 2011](https://doi.org/10.1029/2010JD014574)
  [Fu and Liou, 1992](https://doi.org/10.1175/1520-0469(1992)049%3C2139:OTCDMF%3E2.0.CO;2)
RRTMG-K ra_sw_physics=14 An improved version of the RRTMG scheme; note: To use this option, WRF must be built with the configuration setting -DBUILD_RRTMK = 1 (modify under ARCHFLAGS in configure.wrf) Baek, 2017

  [Baek, 2017](https://doi.org/10.1002/2017MS000994)
RRTMG-fast ra_sw_physics=24 A fast version of RRTMG (option 4) Iacono et al., 2008

  [Iacono et al., 2008](https://doi.org/10.1029/2008JD009944)
Held-Suarez ra_sw_physics=31 A temperature relaxation scheme designed for idealized tests only No publication available

GFDL ra_sw_physics=99 Eta operational scheme; two-stream multi-band scheme with ozone from climatology and cloud effects Fels and Schwarzkopf, 1981

  [Fels and Schwarzkopf, 1981](https://doi.org/10.1029/JC086iC02p01205)
Namelist Options Related to Shortwave Radiation

slope_rad=1 : include slope and shading effects; modifies surface solar radiation flux according to terrain slope topo_shading=1 : allows for shadowing of neighboring grid cells; use only with high-resolution runs with grid size less than a few kilometers swrad_scat : scattering turning parameter for use with “ra_sw_physics=1;” default value is 1, which is equivalent to 1.e-5 m2/kg; when the value is greater than 1, scattering is increased ra_sw_eclipse=1 : eclipse effect on shotwave radiation; only works with ra_sw_physics options 4 (RRTMG), 5 (New Goddard), 2 (Goddard), and 1 (Duhhia). The eclipse data from 1950 – 2050 is provided in WRF/run/eclipse_besselian_elements.dat. swint_opt=1 : interpolation of short-wave radiation based on the updated solar zenith angle between shortwave calls swint_opt=2 : activates the Fast All-sky Radiation Model for Solar applications (FARMS). FARMS is a fast radiative transfer model that allows simulations of broadband solar radiation every model time step. The model uses lookup tables of cloud transmittances and reflectances by varying cloud optical thicknesses, cloud particle sizes, and solar zenith angles. A more detailed description is provided in Xie et al., 2016

  [Xie et al., 2016](https://doi.org/10.1016/j.solener.2016.06.003)
- slope_rad=1 : include slope and shading effects; modifies surface solar radiation flux according to terrain slope
slope_rad=1 : include slope and shading effects; modifies surface solar radiation flux according to terrain slope

- topo_shading=1 : allows for shadowing of neighboring grid cells; use only with high-resolution runs with grid size less than a few kilometers
topo_shading=1 : allows for shadowing of neighboring grid cells; use only with high-resolution runs with grid size less than a few kilometers

- swrad_scat : scattering turning parameter for use with “ra_sw_physics=1;” default value is 1, which is equivalent to 1.e-5 m2/kg; when the value is greater than 1, scattering is increased
swrad_scat : scattering turning parameter for use with “ra_sw_physics=1;” default value is 1, which is equivalent to 1.e-5 m2/kg; when the value is greater than 1, scattering is increased

- ra_sw_eclipse=1 : eclipse effect on shotwave radiation; only works with ra_sw_physics options 4 (RRTMG), 5 (New Goddard), 2 (Goddard), and 1 (Duhhia). The eclipse data from 1950 – 2050 is provided in WRF/run/eclipse_besselian_elements.dat.
ra_sw_eclipse=1 : eclipse effect on shotwave radiation; only works with ra_sw_physics options 4 (RRTMG), 5 (New Goddard), 2 (Goddard), and 1 (Duhhia). The eclipse data from 1950 – 2050 is provided in WRF/run/eclipse_besselian_elements.dat.

- swint_opt=1 : interpolation of short-wave radiation based on the updated solar zenith angle between shortwave calls
swint_opt=1 : interpolation of short-wave radiation based on the updated solar zenith angle between shortwave calls

- swint_opt=2 : activates the Fast All-sky Radiation Model for Solar applications (FARMS). FARMS is a fast radiative transfer model that allows simulations of broadband solar radiation every model time step. The model uses lookup tables of cloud transmittances and reflectances by varying cloud optical thicknesses, cloud particle sizes, and solar zenith angles. A more detailed description is provided in Xie et al., 2016
  [Xie et al., 2016](https://doi.org/10.1016/j.solener.2016.06.003)
swint_opt=2 : activates the Fast All-sky Radiation Model for Solar applications (FARMS). FARMS is a fast radiative transfer model that allows simulations of broadband solar radiation every model time step. The model uses lookup tables of cloud transmittances and reflectances by varying cloud optical thicknesses, cloud particle sizes, and solar zenith angles. A more detailed description is provided in Xie et al., 2016

  [Xie et al., 2016](https://doi.org/10.1016/j.solener.2016.06.003)

### Input to Radiation Options ¶

CAM Green House Gases Provides yearly green house gases from 1765 to 2500. Beginning with V4.4, this is a runtime option (controlled by ghg_input=1 in the &physics section of the namelist; previously had to be activated by compiling WRF with the macro –DCLWRFGHG added in configure.wrf). Once compiled, CAM (3), RRTM (1), and RRTMG (4) long-wave schemes will see these gases. Ten scenario files are available in the test/em_real and run/ directories:

from IPCC AR5: CAMtr_volume_mixing_ratio.RCP4.5/RCP6/RCP8.5 from IPCC AR4: CAMtr_volume_mixing_ratio.A1B/A2 from IPCC AR6: CAMtr_volume_mixing_ratio.SSP119/SSP126/SSP245/SSP370/SSP585 the default points to the CAMtr_volume_mixing_ratio.SSP245 file

- from IPCC AR5: CAMtr_volume_mixing_ratio.RCP4.5/RCP6/RCP8.5
from IPCC AR5: CAMtr_volume_mixing_ratio.RCP4.5/RCP6/RCP8.5

- from IPCC AR4: CAMtr_volume_mixing_ratio.A1B/A2
from IPCC AR4: CAMtr_volume_mixing_ratio.A1B/A2

- from IPCC AR6: CAMtr_volume_mixing_ratio.SSP119/SSP126/SSP245/SSP370/SSP585
from IPCC AR6: CAMtr_volume_mixing_ratio.SSP119/SSP126/SSP245/SSP370/SSP585

- the default points to the CAMtr_volume_mixing_ratio.SSP245 file
the default points to the CAMtr_volume_mixing_ratio.SSP245 file

Climatological ozone and aerosol data for RRTMG The ozone data are adapted from CAM radiation (ra_*_physics=3), and have latitudinal (2.82 degrees), height, and temporal (monthly) variation, as opposed to the default ozone used in the scheme, which only varies with height. This is activated by namelist option “o3input=2,” which is the default option. The aerosol data are based on Tegen et al., 1997 , which has 6 types: organic carbon, black carbon, sulfate, sea salt, dust, and stratospheric aerosol (volcanic ash, which is zero). The data also have spatial (5 degrees in longitude and 4 degrees in latitudes) and temporal (monthly) variations. The option is activated by the namelist option “aer_opt=1.”

  [Tegen et al., 1997](https://doi.org/10.1029/97JD01864)
Aerosol input for RRTMG and Goddard radiation options (aer_opt=2) Either AOD or AOD plus Angstrom exponent, single scattering albedo, and cloud asymmetry parameter can be provided via constant values from the namelist or 2D input fields via auxiliary input stream 15. Aerosol type can also be set.

Aerosol input for RRTMG radiation scheme (aer_opt=3) From climatological water- and ice-friendly aerosols. This option only works with Thompson aerosol-aware microphysics (option 28).

Effective cloud water, ice and snow radii for RRTMG radiation scheme (use_mp_re=1) These come from Thompson (8), WSM (3,4,6,24), WDM (14,16,26), Goddard 4-ice (7), NSSL (17,18,19,21,22), and P3 (50-53) microphysics schemes.


### Clouds and Cloud Fraction Options ¶

Longwave Radation and Clouds All radiation schemes interact with resolved model cloud fields, allowing for ice and water clouds and precipitating species. Some nuances include

Some microphysics options pass their own particle sizes to RRTMG radiation (cloud droplets, ice and snow) Other combinations only use mass information from microphysics, and assume effective sizes in the radiation scheme Rain and graupel effects are smaller than cloud and snow, and are not often explicitly considered

- Some microphysics options pass their own particle sizes to RRTMG radiation (cloud droplets, ice and snow)
Some microphysics options pass their own particle sizes to RRTMG radiation (cloud droplets, ice and snow)

- Other combinations only use mass information from microphysics, and assume effective sizes in the radiation scheme
Other combinations only use mass information from microphysics, and assume effective sizes in the radiation scheme

- Rain and graupel effects are smaller than cloud and snow, and are not often explicitly considered
Rain and graupel effects are smaller than cloud and snow, and are not often explicitly considered

Clouds strongly affect IR at all wavelengths (considered “grey bodies”) and are almost opaque to it.

Shortwave Radiation and Clouds Considerations for shortwave radiation schemes are similar to those of longwave schemes. There are interactions with model resolved clouds, and, in some cases, cumulus schemes. There are also fraction and overlap assumptions, as well as cloud albedo reflection. Surface albedo reflection is based on the land-surface type and snow cover.

Cloud Fraction for Microphysics Clouds

icloud=1 : Xu and Randall method; fraction is only <1 for small cloud amounts, 0 for no resolved cloud icloud=2 : Simple 0 or 1 method with small resolved cloud threshold icloud=3 : Thompson option (RH dependent); 1 > Fraction > 0 for high RH and no resolved clouds

- icloud=1 : Xu and Randall method; fraction is only <1 for small cloud amounts, 0 for no resolved cloud
icloud=1 : Xu and Randall method; fraction is only <1 for small cloud amounts, 0 for no resolved cloud

- icloud=2 : Simple 0 or 1 method with small resolved cloud threshold
icloud=2 : Simple 0 or 1 method with small resolved cloud threshold

- icloud=3 : Thompson option (RH dependent); 1 > Fraction > 0 for high RH and no resolved clouds
icloud=3 : Thompson option (RH dependent); 1 > Fraction > 0 for high RH and no resolved clouds

Cloud Fraction for Unresolved Convective Clouds

cu_rad_feedback=.true. : only works for Grell Freitas (3), Grell 3 (5), Grell-Devenyi (93), and Kain Fritsch (1) radiation options. ZM separately provides cloud fraction to radiation

- cu_rad_feedback=.true. : only works for Grell Freitas (3), Grell 3 (5), Grell-Devenyi (93), and Kain Fritsch (1) radiation options.
cu_rad_feedback=.true. : only works for Grell Freitas (3), Grell 3 (5), Grell-Devenyi (93), and Kain Fritsch (1) radiation options.

- ZM separately provides cloud fraction to radiation
ZM separately provides cloud fraction to radiation


### Radiation Time Step (radt) ¶

The namelist parameter “radt” controls the radiation time step. Consider the following when setting radt.

Radiation is too expensive to call every step. Frequency should resolve cloud-cover changes with time. radt=1 minute per km grid size (of innermost domain) is about right (e.g., radt=10 for dx=10 km). Each domain can have its own value but it is recommended to use the same value on all 2-way nests.

- Radiation is too expensive to call every step.
Radiation is too expensive to call every step.

- Frequency should resolve cloud-cover changes with time.
Frequency should resolve cloud-cover changes with time.

- radt=1 minute per km grid size (of innermost domain) is about right (e.g., radt=10 for dx=10 km).
radt=1 minute per km grid size (of innermost domain) is about right (e.g., radt=10 for dx=10 km).

- Each domain can have its own value but it is recommended to use the same value on all 2-way nests.
Each domain can have its own value but it is recommended to use the same value on all 2-way nests.


## Planetary Boundary Layer Physics ¶

WRF Planetary Boundary Layer (PBL) schemes’ purpose is to distribute surface fluxes with boundary layer eddy fluxes, and allow for PBL growth by entrainment. They are also responsible for any vertical mixing above the boundary layer.

There are two different classes of PBL schemes: Turbulent kinetic energy prediction (Mellor-Yamada Janjic, MYNN, Bougeault-Lacarrere, TEMF, QNSE, and CAM UW). Some also include non-local mass-flux terms (QNSE-EDMF, MYNN, and TEMF) Diagnostic non-local (YSU, GFS, MRF, ACM2) Above the PBL, all schemes also do vertical diffusion due to turbulence. PBL schemes can be used for most grid sizes when surface fluxes are present; however, at grid size dx << 1 km, this assumption breaks down. To get around this, you can use 3d diffusion instead of a PBL scheme (coupled to surface physics). This works best when dx and dz are comparable. The lowest level should be in the surface layer (0.1h). This is important for surface (2m, 10m) diagnostic interpolation. With ACM2, GFS, and MRF PBL schemes, the lowest full level should be .99 or .995 (not too close to 1). TKE schemes and YSU can use thinner surface layers. PBL schemes assume PBL eddies are not resolved.

- There are two different classes of PBL schemes: Turbulent kinetic energy prediction (Mellor-Yamada Janjic, MYNN, Bougeault-Lacarrere, TEMF, QNSE, and CAM UW). Some also include non-local mass-flux terms (QNSE-EDMF, MYNN, and TEMF) Diagnostic non-local (YSU, GFS, MRF, ACM2)
- Turbulent kinetic energy prediction (Mellor-Yamada Janjic, MYNN, Bougeault-Lacarrere, TEMF, QNSE, and CAM UW). Some also include non-local mass-flux terms (QNSE-EDMF, MYNN, and TEMF)
Turbulent kinetic energy prediction (Mellor-Yamada Janjic, MYNN, Bougeault-Lacarrere, TEMF, QNSE, and CAM UW). Some also include non-local mass-flux terms (QNSE-EDMF, MYNN, and TEMF)

- Diagnostic non-local (YSU, GFS, MRF, ACM2)
Diagnostic non-local (YSU, GFS, MRF, ACM2)

- Above the PBL, all schemes also do vertical diffusion due to turbulence.
Above the PBL, all schemes also do vertical diffusion due to turbulence.

- PBL schemes can be used for most grid sizes when surface fluxes are present; however, at grid size dx << 1 km, this assumption breaks down. To get around this, you can use 3d diffusion instead of a PBL scheme (coupled to surface physics). This works best when dx and dz are comparable.
PBL schemes can be used for most grid sizes when surface fluxes are present; however, at grid size dx << 1 km, this assumption breaks down. To get around this, you can use 3d diffusion instead of a PBL scheme (coupled to surface physics). This works best when dx and dz are comparable.

- The lowest level should be in the surface layer (0.1h). This is important for surface (2m, 10m) diagnostic interpolation.
The lowest level should be in the surface layer (0.1h). This is important for surface (2m, 10m) diagnostic interpolation.

- With ACM2, GFS, and MRF PBL schemes, the lowest full level should be .99 or .995 (not too close to 1).
With ACM2, GFS, and MRF PBL schemes, the lowest full level should be .99 or .995 (not too close to 1).

- TKE schemes and YSU can use thinner surface layers.
TKE schemes and YSU can use thinner surface layers.

- PBL schemes assume PBL eddies are not resolved.
PBL schemes assume PBL eddies are not resolved.

Note See the WRF Tutorial presentation on PBL for additional details.

  [WRF Tutorial presentation on PBL](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_pbl_turbulence.pdf)
Note

See the WRF Tutorial presentation on PBL for additional details.

  [WRF Tutorial presentation on PBL](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_pbl_turbulence.pdf)

### PBL Scheme Options ¶

| Scheme | Option | Works With sfclay Option | Prognostic Variables | Diagnostic Variables | Cloud Mixing |
Scheme

Option

Works With sfclay Option

Prognostic Variables

Diagnostic Variables

Cloud Mixing

| YSU | 1 | 1 91 | none | exch_h | QC QI |
YSU

1

1 91

none

exch_h

QC QI

| MYJ | 2 | 2 | 4 | EL_PBL exch_h | QC QI |
MYJ

2

4

EL_PBL exch_h

QC QI

| QNSE-EDMF | 4 | 4 | TKE_PBL | EL_PBL exch_h exch_m | QC QI |
QNSE-EDMF

4

TKE_PBL

EL_PBL exch_h exch_m

QC QI

| MYNN2 | 5 | 1 2 5 91 | QKE | Tsq Qsq Cov exch_h exch_m | QC |
MYNN2

5

1 2 5 91

QKE

Tsq Qsq Cov exch_h exch_m

QC

| MYNN3 | 6 | 1 2 5 91 | QKE Tsq Qsq Cov | exch_h exch_m | QC |
MYNN3

6

1 2 5 91

QKE Tsq Qsq Cov

exch_h exch_m

QC

| ACM2 | 7 | 1 7 91 |  |  | QC QI |
ACM2

7

1 7 91

QC QI

| BouLac | 8 | 1 2 91 | TKE_PBL | EL_PBL exch_h exch_m | QC |
BouLac

8

1 2 91

TKE_PBL

EL_PBL exch_h exch_m

QC

| UW | 9 | 1 2 91 | TKE_PBL | exch_h exch_m | QC |
UW

9

1 2 91

TKE_PBL

exch_h exch_m

QC

| TEMF | 10 | 10 | TE_TEMF | *_temf | QC QI |
TEMF

10

TE_TEMF

*_temf

QC QI

| Shin-Hong | 11 | 1 91 |  | exch_h | QC QI |
Shin-Hong

11

1 91

exch_h

QC QI

| GBM | 12 | 1 91 | TKE_PBL | EL_PBL exch_h exch_m | QC QI |
GBM

12

1 91

TKE_PBL

EL_PBL exch_h exch_m

QC QI

| EEPS | 16 | 1 5 91 | PEK_PBL PEP_PBL | exch_h exch_m | QC QI |
EEPS

16

1 5 91

PEK_PBL PEP_PBL

exch_h exch_m

QC QI

| KEPS | 17 | 1 2 | TPE_PBL DISS_PBL TKE_PBL | exch_h exch_m | QC |
KEPS

17

1 2

TPE_PBL DISS_PBL TKE_PBL

exch_h exch_m

QC

| MRF | 99 | 1 91 |  |  | QC QI |
MRF

99

1 91

QC QI


### PBL Scheme Details and References ¶

Yonsei University (YSU) bl_pbl_physics=1 Non-local-K scheme with explicit entrainment layer and parabolic K profile in unstable mixed layer; includes capability of topdown mixing for turbulence driven by cloud-top radiative cooling, which is separate from bottom-up surface-flux-driven mixing Hong et al., 2006

  [Hong et al., 2006](https://doi.org/10.1175/MWR3199.1)
Additional options specific for use with YSU:

topo_wind : =1 - topographic correction for surface winds to represent extra drag from sub-grid topography and enhanced flow at hill tops ( Jimenez and Dudhia, 2012 ); =2 - a simpler terrain variance-related correction ysu_topdown_pblmix=1 : option for top-down mixing driven by radiative cooling ( Wilson and Fovell, 2018 )

  [Jimenez and Dudhia, 2012](https://doi.org/10.1175/JAMC-D-11-084.1)
  [Wilson and Fovell, 2018](https://doi.org/10.1175/WAF-D-17-0109.1)
- topo_wind : =1 - topographic correction for surface winds to represent extra drag from sub-grid topography and enhanced flow at hill tops ( Jimenez and Dudhia, 2012 ); =2 - a simpler terrain variance-related correction
  [Jimenez and Dudhia, 2012](https://doi.org/10.1175/JAMC-D-11-084.1)
topo_wind : =1 - topographic correction for surface winds to represent extra drag from sub-grid topography and enhanced flow at hill tops ( Jimenez and Dudhia, 2012 ); =2 - a simpler terrain variance-related correction

  [Jimenez and Dudhia, 2012](https://doi.org/10.1175/JAMC-D-11-084.1)
- ysu_topdown_pblmix=1 : option for top-down mixing driven by radiative cooling ( Wilson and Fovell, 2018 )
  [Wilson and Fovell, 2018](https://doi.org/10.1175/WAF-D-17-0109.1)
ysu_topdown_pblmix=1 : option for top-down mixing driven by radiative cooling ( Wilson and Fovell, 2018 )

  [Wilson and Fovell, 2018](https://doi.org/10.1175/WAF-D-17-0109.1)
Mellor-Yamada-Janjic (MYJ) bl_pbl_physics=2 Eta operational scheme; one-dimensional prognostic turbulent kinetic energy scheme with local vertical mixing Janjic, 1994 Mesinger, 1993

  [Janjic, 1994](https://doi.org/10.1175/1520-0493(1994)122%3C0927:TSMECM%3E2.0.CO;2)
  [Mesinger, 1993](https://www2.mmm.ucar.edu/wrf/users/physics/phys_refs/PBL/MYJ_part2.pdf)
Quasi-Normal Scale Elimination (QNSE-EDMF) bl_pbl_physics=4 A TKE-prediction option that uses a new theory for stably-stratified regions; daytime part uses eddy diffusivity mass-flux method with shallow convection (mfshconv = 1); includes shallow convection using a mass-flux approach through the whole cloud-topped boundary layer Sukoriansky et al., 2005

  [Sukoriansky et al., 2005](https://doi.org/10.1007/s10546-004-6848-4)
Mellor-Yamada Nakanishi and Niino Level 2.5 (MYNN2) bl_pbl_physics=5 Predicts sub-grid TKE terms; includes shallow convection using a mass-flux approach through the whole cloud-topped boundary layer; includes a capability of top-down mixing for turbulence driven by cloud-top radiative cooling, which is separate from bottom-up surface-flux-driven mixing Nakanishi and Niino, 2006 Nakanishi and Niino, 2009 Olson et al., 2019

  [Nakanishi and Niino, 2006](https://doi.org/10.1007/s10546-005-9030-8)
  [Nakanishi and Niino, 2009](https://doi.org/10.2151/jmsj.87.895)
  [Olson et al., 2019](https://doi.org/10.25923/n9wm-be49)
Additional options specific for use with MYNN:

icloud_bl=1 : option to couple subgrid-scale clouds from MYNN to radiation bl_mynn_cloudpdf : =1 - Kuwano et al., 2010 ; =2 - Chaboureau and Bechtold, 2002 (with mods, default) bl_mynn_cloudmix=1 : mixing cloud water and ice (qnc and qni are mixed when scalar_pblmix=1) bl_mynn_edmf=1 : activate mass-flux in MYNN bl_mynn_mixlength : =1 is from RAP/HRRR; =2 is from blending

  [Kuwano et al., 2010](https://doi.org/10.1002/qj.660)
  [Chaboureau and Bechtold, 2002](https://doi.org/10.1175/1520-0469(2002)059%3C2362:ASCPDF%3E2.0.CO;2)
- icloud_bl=1 : option to couple subgrid-scale clouds from MYNN to radiation
icloud_bl=1 : option to couple subgrid-scale clouds from MYNN to radiation

- bl_mynn_cloudpdf : =1 - Kuwano et al., 2010 ; =2 - Chaboureau and Bechtold, 2002 (with mods, default)
  [Kuwano et al., 2010](https://doi.org/10.1002/qj.660)
  [Chaboureau and Bechtold, 2002](https://doi.org/10.1175/1520-0469(2002)059%3C2362:ASCPDF%3E2.0.CO;2)
bl_mynn_cloudpdf : =1 - Kuwano et al., 2010 ; =2 - Chaboureau and Bechtold, 2002 (with mods, default)

  [Kuwano et al., 2010](https://doi.org/10.1002/qj.660)
  [Chaboureau and Bechtold, 2002](https://doi.org/10.1175/1520-0469(2002)059%3C2362:ASCPDF%3E2.0.CO;2)
- bl_mynn_cloudmix=1 : mixing cloud water and ice (qnc and qni are mixed when scalar_pblmix=1)
bl_mynn_cloudmix=1 : mixing cloud water and ice (qnc and qni are mixed when scalar_pblmix=1)

- bl_mynn_edmf=1 : activate mass-flux in MYNN
bl_mynn_edmf=1 : activate mass-flux in MYNN

- bl_mynn_mixlength : =1 is from RAP/HRRR; =2 is from blending
bl_mynn_mixlength : =1 is from RAP/HRRR; =2 is from blending

Mellor-Yamada Nakanishi and Niino Level 3 (MYNN3) bl_pbl_physics=6 Predicts TKE and other second-moment terms Nakanishi and Niino, 2006 Nakanishi and Niino, 2009 Olson et al., 2019

  [Nakanishi and Niino, 2006](https://doi.org/10.1007/s10546-005-9030-8)
  [Nakanishi and Niino, 2009](https://doi.org/10.2151/jmsj.87.895)
  [Olson et al., 2019](https://doi.org/10.25923/n9wm-be49)
Note

bl_pbl_physics option 6 is only available through WRFV4.4.2. See the below bl_mynn_closure option if using V4.5+.

MYNN Closure bl_mynn_closure

= 2.5 : level 2.5 = 2.6 : level 2.6 = 3.0 : level 3.0

- = 2.5 : level 2.5
= 2.5 : level 2.5

- = 2.6 : level 2.6
= 2.6 : level 2.6

- = 3.0 : level 3.0
= 3.0 : level 3.0

ACM2 bl_pbl_physics=7 Asymmetric Convective Model with non-local upward mixing and local downward mixing Pleim, 2007

  [Pleim, 2007](https://doi.org/10.1175/JAM2539.1)
BouLac bl_pbl_physics=8 Bougeault-Lacarrère PBL; a TKE-prediction option; designed for use with BEP urban model Bougeault, 1989

  [Bougeault, 1989](https://doi.org/10.1175/1520-0493(1989)117%3C1872:POOITI%3E2.0.CO;2)
UW bl_pbl_physics=9 TKE scheme from CESM climate model; includes shallow convection using a mass-flux approach from the cloud base; includes capability of topdown mixing for turbulence driven by cloud-top radiative cooling, which is separate from bottom-up surface-flux-driven mixing Bretherton and Park, 2009

  [Bretherton and Park, 2009](https://doi.org/10.1175/2008JCLI2556.1)
Total Energy - Mass Flux (TEMF) bl_pbl_physics=10 Sub-grid total energy prognostic variable, plus mass-flux type shallow convection; includes shallow convection using a mass-flux approach through the whole cloud-topped boundary layer Angevine et al., 2010

  [Angevine et al., 2010](https://doi.org/10.1175/2010MWR3142.1)
Shin-Hong bl_pbl_physics=11 Includes scale dependency for vertical transport in convective PBL; vertical mixing in the stable PBL and free atmosphere follows YSU; this scheme also has diagnosed TKE and mixing length output Shin and Hong, 2015

  [Shin and Hong, 2015](https://doi.org/10.1175/MWR-D-14-00116.1)
Grenier-Bretherton-McCaa (GBM) bl_pbl_physics=12 A TKE scheme; tested in cloud-topped PBL cases; includes shallow convection using a mass-flux approach from the cloud base Grenier and Bretherton, 2001

  [Grenier and Bretherton, 2001](https://doi.org/10.1175/1520-0493(2001)129%3C0357:AMPPFL%3E2.0.CO;2)
TKE (E)-TKE dissipation rate (epsilon) (EEPS) bl_pbl_physics=16 This scheme predicts TKE, as well as TKE dissipation rate; it also advects both TKE and the dissipation rate; Only works with sf_sfclay_physics options 1, 91, and 5 No publication available

K-epsilon-theta^2 (KEPS) bl_pbl_physics=17 This scheme includes two additional prognostic equations for dissipation rate and temperature variance. Zonato et al., 2022

  [Zonato et al., 2022](https://journals.ametsoc.org/view/journals/mwre/150/8/MWR-D-21-0299.1.xml)
MRF bl_pbl_physics=99 Older version of YSU (option 1) with implicit treatment of entrainment layer as part of non-local-K mixed layer Hong and Pan, 1996

  [Hong and Pan, 1996](https://doi.org/10.1175/1520-0493(1996)124%3C2322:NBLVDI%3E2.0.CO;2)

### Additional PBL Options ¶

LES PBL Settings for a large-eddy-simulation (LES) boundary layer:

bl_pbl_physic = 0 isfflx = 1 sf_sfclay_physics = any option, except 0 sf_surface_physics = any option, except 0 diff_opt = 2 km_opt = 2 or 3

This uses diffusion for vertical mixing. Alternative idealized ways of running the LES PBL are chosen with “isfflx = 0 or 2”. It is best to use dx~dz, especially in the boundary layer, and avoid stretching to very large dz/dx aspect ratios at upper levels. This also tends to work better with continuous stretching to the top, rather than with fixed upper-level dz when dz >> dx.

SMS-3DTKE This is a 3D TKE subgrid mixing scheme that is self-adaptive to the grid size between the large-eddy simulation (LES) and mesoscale limits (new since V4.2). It can be activated by setting

bl_pbl_physic = 0 km_opt = 5 diff_opt = 2 sf_sfclay_physics = 1, 5, or 91

See Zhang et al., 2018 for details.

  [See Zhang et al., 2018](https://doi.org/10.1175/MWR-D-17-0356.1)
Orographic Gravity Wave Drag gwd_opt Can be used with the appropriate input fields from geogrid to represent sub-grid orographic gravity-wave vertical momentum transport

=1 : (default); gravity wave drag and blocking; recommended grid sizes > 5km; includes the subgrid topography effects gravity wave drag and low-level flow blocking; input wind is rotated to the earth coordinate, and output is adjusted back to the projection domain - this enables the scheme to be used for all map projections supported by WRF; to apply this option, appropriate input fields from geogrid must be used; see the Selecting Static Data for the Gravity Wave Drag Scheme in the WPS Chapter of this guide for details. =3 : gravity wave drag, blocking, small-scale gravity drag and turbulent orographic form drag; similar to option 1, with an additional two subgrid-scale sources of orographic drag: one is small-scale GWD ( Tsiringakis et al., 2017 ), which represents gravity wave propagation and breaking in and above stable boundary layers; the other is the turbulent orographic form drag of Beljaars et al., 2004 . Both are applicable down to a grid size of 1 km. Large-scale GWD and low-level flow blocking from gwd_opt=1 are properly adjusted for the horizontal grid resolution. More diagnostic fields from the scheme can be output by setting namelist option “gwd_diags=1.” New GWD input fields are required from WPS.

  [Beljaars et al., 2004](https://doi.org/10.1256/qj.03.73)
- =1 : (default); gravity wave drag and blocking; recommended grid sizes > 5km; includes the subgrid topography effects gravity wave drag and low-level flow blocking; input wind is rotated to the earth coordinate, and output is adjusted back to the projection domain - this enables the scheme to be used for all map projections supported by WRF; to apply this option, appropriate input fields from geogrid must be used; see the Selecting Static Data for the Gravity Wave Drag Scheme in the WPS Chapter of this guide for details.
=1 : (default); gravity wave drag and blocking; recommended grid sizes > 5km; includes the subgrid topography effects gravity wave drag and low-level flow blocking; input wind is rotated to the earth coordinate, and output is adjusted back to the projection domain - this enables the scheme to be used for all map projections supported by WRF; to apply this option, appropriate input fields from geogrid must be used; see the Selecting Static Data for the Gravity Wave Drag Scheme in the WPS Chapter of this guide for details.

- =3 : gravity wave drag, blocking, small-scale gravity drag and turbulent orographic form drag; similar to option 1, with an additional two subgrid-scale sources of orographic drag: one is small-scale GWD ( Tsiringakis et al., 2017 ), which represents gravity wave propagation and breaking in and above stable boundary layers; the other is the turbulent orographic form drag of Beljaars et al., 2004 . Both are applicable down to a grid size of 1 km. Large-scale GWD and low-level flow blocking from gwd_opt=1 are properly adjusted for the horizontal grid resolution. More diagnostic fields from the scheme can be output by setting namelist option “gwd_diags=1.” New GWD input fields are required from WPS.
  [Beljaars et al., 2004](https://doi.org/10.1256/qj.03.73)
=3 : gravity wave drag, blocking, small-scale gravity drag and turbulent orographic form drag; similar to option 1, with an additional two subgrid-scale sources of orographic drag: one is small-scale GWD ( Tsiringakis et al., 2017 ), which represents gravity wave propagation and breaking in and above stable boundary layers; the other is the turbulent orographic form drag of Beljaars et al., 2004 . Both are applicable down to a grid size of 1 km. Large-scale GWD and low-level flow blocking from gwd_opt=1 are properly adjusted for the horizontal grid resolution. More diagnostic fields from the scheme can be output by setting namelist option “gwd_diags=1.” New GWD input fields are required from WPS.

  [Beljaars et al., 2004](https://doi.org/10.1256/qj.03.73)
Fog grav_settling=2 Gravitational settling of fog/cloud droplets


### PBL and Land Surface Time-step (bldt) ¶

“bldt” is a namelist.input parameter used to determine the minutes between boundary layer and land-surface model calls. The typical value is 0 (every step), and this is reasonable for all schemes, with the exception of the CSM land-surface scheme. CSM LSM is expensive, so it may be better to consider increasing the value of bldt when using it.


### Model Grid Spacing ¶

WRF PBL schemes are designed for grid resolution >> I in the image above, while LES schemes are designed for grid resolution << I. For coarse grid spacing, all eddies are sub-grid, and 1-D column schemes handle sub-grid vertical fluxes. For fine grid spacing, all major eddies are resolved, and 3-D turbulence schemes handle sub-grid mixing.

The remaining grid-spacing is a grey-zone, which is sub-kilometer grids, where PBL and LES assumptions are not perfect. There are scale-aware schemes that can be used for this zone.

Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions

- Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases
Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases

- New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes
New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes

- Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions
Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions

For grid sizes up to about 100m, LES is preferable.


### Turbulence and Diffusion ¶

The namelist.input parameter “diff_opt” is used to specify the turbulence and mixing option. When diffusion is used with a PBL scheme, vertical diffusion is deactivated, so diff_opt only affects horizontal diffusion.

diff_opt=0 : no turbulence or explicit spatial numerical filters diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)

- diff_opt=0 : no turbulence or explicit spatial numerical filters
diff_opt=0 : no turbulence or explicit spatial numerical filters

- diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level
diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level

- diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)
diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)

Recommended Diffusion Options

- Real-data case with PBL option on diff_opt=2 km_opt=4 Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes) These options compliment vertical diffusion done by the PBL scheme
- diff_opt=2
diff_opt=2

- km_opt=4
km_opt=4

- Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes)
Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes)

- These options compliment vertical diffusion done by the PBL scheme
These options compliment vertical diffusion done by the PBL scheme

- High-resolution real-data cases (~100m grid) No PBL scheme diff_opt=2 km_opt=2 or 3 (TKE or Smagorinsky scheme)
- No PBL scheme
No PBL scheme

- diff_opt=2
diff_opt=2

- km_opt=2 or 3 (TKE or Smagorinsky scheme)
km_opt=2 or 3 (TKE or Smagorinsky scheme)

- Idealized cloud-resolving (dx= 1-3 km) modeling (smooth or no topography, no surface heat fluxes) diff_opt=2 km_opt=2 or 3
- diff_opt=2
diff_opt=2

- km_opt=2 or 3
km_opt=2 or 3


## Surface physics ¶

WRF surface physics consist of surface layer (sfclay) schemes and land surface model (LSM) schemes. Surface layer schemes determine surface layer diagnostics, which includes exchange and transfer coefficients. They provide these exchange coefficients for heat and moisture to the land surface model (LSM), which then provides land-surface fluxes of heat and moisture to the planetary boundary layer (PBL). The surface schemes also provide friction stress and water-surface fluxes of heat and moisture to the PBL. LSMs are responsible for soil temperature, moisture, snow prediction and sea-ice temperature.

Note See the WRF Tutorial presentation on surface physics for additional details.

  [WRF Tutorial presentation on surface physics](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_surface.pdf)
Note

See the WRF Tutorial presentation on surface physics for additional details.

  [WRF Tutorial presentation on surface physics](https://www2.mmm.ucar.edu/wrf/users/tutorial/presentation_pdfs/202101/dudhia_physics_surface.pdf)

### Surface Layer Schemes ¶

The surface layer has a constant flux layer of about 0.1 x PBL height (~100 m). The lowest WRF model level is found within this layer (typically 10-50 m). The WRF surface layer scheme is chosen by the namelist.input parameter “sf_sfclay_physics” in the &physics section. Some key points to note about WRF sfclay schemes is

They use similarity theory to determine exchange coefficients and diagnostics of 2m temperature, 2m qvapor, and 10m winds. They provide exchange coefficient to land-surface models. They provide friction velocity to the PBL scheme. They provide surface fluxes over water points. Schemes have variations in stability functions and roughness lengths.

- They use similarity theory to determine exchange coefficients and diagnostics of 2m temperature, 2m qvapor, and 10m winds.
They use similarity theory to determine exchange coefficients and diagnostics of 2m temperature, 2m qvapor, and 10m winds.

- They provide exchange coefficient to land-surface models.
They provide exchange coefficient to land-surface models.

- They provide friction velocity to the PBL scheme.
They provide friction velocity to the PBL scheme.

- They provide surface fluxes over water points.
They provide surface fluxes over water points.

- Schemes have variations in stability functions and roughness lengths.
Schemes have variations in stability functions and roughness lengths.


### Surface Layer Scheme Details and References ¶

Revised MM5 sf_sfclay_physics=1 Removes limits and uses updated stability functions; thermal and moisture roughness lengths (or exchange coefficients for heat and moisture) over the ocean use the COARE 3 formula ( Fairall et al., 2003 ) Jimenez et al., 2012

  [Fairall et al., 2003](https://doi.org/10.1175/1520-0442(2003)016%3C0571:BPOASF%3E2.0.CO;2)
  [Jimenez et al., 2012](https://doi.org/10.1175/MWR-D-11-00056.1)
Eta Similarity sf_sfclay_physics=2 Used in Eta model; based on Monin-Obukhov with Zilitinkevich thermal roughness length and standard similarity functions from look-up tables Monin and Obukhov, 1954 Janjic, 1994 Janjic, 1996 Janjic, 2001

  [Monin and Obukhov, 1954](https://moodle2.units.it/pluginfile.php/267453/mod_resource/content/1/ABL_lecture_13.pdf)
  [Janjic, 1994](https://doi.org/10.1175/1520-0493(1994)122%3C0927:TSMECM%3E2.0.CO;2)
  [Janjic, 1996](https://www2.mmm.ucar.edu/wrf/users/physics/phys_refs/SURFACE_LAYER/eta_part3.pdf)
  [Janjic, 2001](https://repository.library.noaa.gov/view/noaa/11409)
QNSE sf_sfclay_physics=4 Quasi-Normal Scale Elimination PBL scheme’s surface layer option No publication available

MYNN sf_sfclay_physics=5 Nakanishi and Niino PBL’s surface layer scheme Olson et al, 2021

  [Olson et al, 2021](https://repository.library.noaa.gov/view/noaa/30605)
Pleim-Xiu sf_sfclay_physics=7 Pleim, 2006

  [Pleim, 2006](https://doi.org/10.1175/JAM2339.1)
Total Energy - Mass Flux (TEMF) sf_sfclay_physics=10 Angevine et al., 2010

  [Angevine et al., 2010](https://doi.org/10.1175/2010MWR3142.1)
MM5 Similarity sf_sfclay_physics=91 Based on Monin-Obukhov, with Carslon-Boland viscous sub-layer and standard similarity functions from look-up tables thermal and moisture roughness lengths (or exchange coefficients for heat and moisture) over ocean use the COARE 3 formula ( Fairall et al., 2003 ) Paulson, 1970 Dyer and Hicks, 1970 Webb, 1970 Belijaars, 1994 Zhang and Anthes, 1982

  [Fairall et al., 2003](https://doi.org/10.1175/1520-0442(2003)016%3C0571:BPOASF%3E2.0.CO;2)
  [Paulson, 1970](https://doi.org/10.1175/1520-0450(1970)009%3C0857:TMROWS%3E2.0.CO;2)
  [Dyer and Hicks, 1970](https://doi.org/10.1002/qj.49709641012)
  [Webb, 1970](https://doi.org/10.1002/qj.49709640708)
  [Belijaars, 1994](https://doi.org/10.1002/qj.49712152203)
  [Zhang and Anthes, 1982](https://doi.org/10.1175/1520-0450(1982)021%3C1594:AHRMOT%3E2.0.CO;2)
Other Options Related to Surface Layer

iz0tlnd : =1 - Chen-Zhang thermal roughness length over land, which depends on vegetation height (works with sf_sfclay_physics = 1, 91, and 5); =0 - original thermal roughness length in each sfclay option Chen and Zhang, 2009 shalwater_z0=1 : Shallow-water roughness for offshore roughness adjustment in water depths less tha 100 m. This option works with a specified depth or real bathymetry input, and only with sf_sfclay_physics=1. The bathymetry data is available from the WPS V4 Geographical Static Data Downloads Page . If no bathymetry data is available, set constant depth (in meters; must be positive) using namelist option “shalwater_depth.” Any depths outside the range of 10-100 m are rounded to the nearest limit value. GEBCO Compilation Group, 2021 Jimenez and Dudhia, 2018

  [Chen and Zhang, 2009](https://doi.org/10.1029/2009GL037980)
  [WPS V4 Geographical Static Data Downloads Page](https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html)
  [GEBCO Compilation Group, 2021](https://www.bodc.ac.uk/data/published_data_library/catalogue/10.5285/c6612cbe-50b3-0cff-e053-6c86abc09f8f)
  [Jimenez and Dudhia, 2018](https://doi.org/10.1175/JAMC-D-17-0137.1)
- iz0tlnd : =1 - Chen-Zhang thermal roughness length over land, which depends on vegetation height (works with sf_sfclay_physics = 1, 91, and 5); =0 - original thermal roughness length in each sfclay option Chen and Zhang, 2009
  [Chen and Zhang, 2009](https://doi.org/10.1029/2009GL037980)
iz0tlnd : =1 - Chen-Zhang thermal roughness length over land, which depends on vegetation height (works with sf_sfclay_physics = 1, 91, and 5); =0 - original thermal roughness length in each sfclay option Chen and Zhang, 2009

  [Chen and Zhang, 2009](https://doi.org/10.1029/2009GL037980)
- shalwater_z0=1 : Shallow-water roughness for offshore roughness adjustment in water depths less tha 100 m. This option works with a specified depth or real bathymetry input, and only with sf_sfclay_physics=1. The bathymetry data is available from the WPS V4 Geographical Static Data Downloads Page . If no bathymetry data is available, set constant depth (in meters; must be positive) using namelist option “shalwater_depth.” Any depths outside the range of 10-100 m are rounded to the nearest limit value. GEBCO Compilation Group, 2021 Jimenez and Dudhia, 2018
  [WPS V4 Geographical Static Data Downloads Page](https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html)
  [GEBCO Compilation Group, 2021](https://www.bodc.ac.uk/data/published_data_library/catalogue/10.5285/c6612cbe-50b3-0cff-e053-6c86abc09f8f)
  [Jimenez and Dudhia, 2018](https://doi.org/10.1175/JAMC-D-17-0137.1)
shalwater_z0=1 : Shallow-water roughness for offshore roughness adjustment in water depths less tha 100 m. This option works with a specified depth or real bathymetry input, and only with sf_sfclay_physics=1. The bathymetry data is available from the WPS V4 Geographical Static Data Downloads Page . If no bathymetry data is available, set constant depth (in meters; must be positive) using namelist option “shalwater_depth.” Any depths outside the range of 10-100 m are rounded to the nearest limit value. GEBCO Compilation Group, 2021 Jimenez and Dudhia, 2018

  [WPS V4 Geographical Static Data Downloads Page](https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html)
  [GEBCO Compilation Group, 2021](https://www.bodc.ac.uk/data/published_data_library/catalogue/10.5285/c6612cbe-50b3-0cff-e053-6c86abc09f8f)
  [Jimenez and Dudhia, 2018](https://doi.org/10.1175/JAMC-D-17-0137.1)

### Land Surface Model ¶

WRF LSM schemes are driven by surface energy and water fluxes. They predict soil temperature and soil moisture in 3 or 4 layers, depending on the scheme, as well as snow water equivalent on the ground.

Vegetation and Soil

LSMs consider the effects of vegetation and soil components, such as vegetation fraction, vegetation categories (e.g., cropland, forest types, etc.), and soil categories (e.g., sandy, clay, etc.). Below are some key notes.

Processes include evapotranspiration, root zone, and leaf effects. Vegetation fraction varies seasonally. Soil categories are considered for drainage and thermal conductivity.

- Processes include evapotranspiration, root zone, and leaf effects.
Processes include evapotranspiration, root zone, and leaf effects.

- Vegetation fraction varies seasonally.
Vegetation fraction varies seasonally.

- Soil categories are considered for drainage and thermal conductivity.
Soil categories are considered for drainage and thermal conductivity.

Snow Cover

LSMs include fractional snow cover and predict snow water equivalent development based on precipitation, sublimation, melting, and run-off. The number of layers is dependent on the scheme.

Single-layer snow (Noah, PX) Multi-layer snow (RUC, NoahMP, SSiB,CLM4) 5-layer option has no snow prediction

- Single-layer snow (Noah, PX)
Single-layer snow (Noah, PX)

- Multi-layer snow (RUC, NoahMP, SSiB,CLM4)
Multi-layer snow (RUC, NoahMP, SSiB,CLM4)

- 5-layer option has no snow prediction
5-layer option has no snow prediction

Note: Frozen soil water is also predicted by the Noah, NoahMP, RUC, and CLM4 schemes.

Urban Effects

An urban category in LSMs is typically adequate for larger-scale studies. An alternative is to use an urban model with either the Noah or NoahMP LSM scheme. To do this, set sf_urban_physics in namelist.input to one of the following options.

=1 : Urban Canopy Model (UCM); single layer; The following options are available when sf_urban_physics=1. slucm_distributed_drag : Option to use spatially varying 2-D urban Zero-plane Displacement, Roughness length for momentum, Frontal area index (default is .false.) (NOTE: this option requires SLUCM static input for the WPS/geogrid process). distributed_ahe_opt Option to handle anthropogenic surface heat flux (need additional input in wrfinput file). =0 : no anthropogenic surface heat flux from input data =1 : (default) add to first level temperature tendency =2 : add to surface sensible heat flux =2 : Building Environment Parameterization (BEP); multi-layer; only works with YSU, MYJ and BouLac PBL schemes =3 : Building Energy Model (BEM); adds heating and air-conditioning to BEP; only works with YSU, MYJ and BouLac PBL schemes Note NUDAPT detailed map data is available for use in WPS, and includes data for 40+ U.S. cities. Beginning with V4.3, code is updated to include a capability to use local climate zones, which is incorporated for all three urban applications ( additional details )

  [SLUCM static input](https://www2.mmm.ucar.edu/wrf/src/wps_files/slucm.tar.gz)
  [additional details](https://ral.ucar.edu/sites/default/files/public/product-tool/urban-canopy-model/WRF_urban_update_Readme_file_WRF4.3.pdf)
- =1 : Urban Canopy Model (UCM); single layer; The following options are available when sf_urban_physics=1. slucm_distributed_drag : Option to use spatially varying 2-D urban Zero-plane Displacement, Roughness length for momentum, Frontal area index (default is .false.) (NOTE: this option requires SLUCM static input for the WPS/geogrid process). distributed_ahe_opt Option to handle anthropogenic surface heat flux (need additional input in wrfinput file). =0 : no anthropogenic surface heat flux from input data =1 : (default) add to first level temperature tendency =2 : add to surface sensible heat flux
  [SLUCM static input](https://www2.mmm.ucar.edu/wrf/src/wps_files/slucm.tar.gz)
=1 : Urban Canopy Model (UCM); single layer; The following options are available when sf_urban_physics=1.

slucm_distributed_drag : Option to use spatially varying 2-D urban Zero-plane Displacement, Roughness length for momentum, Frontal area index (default is .false.) (NOTE: this option requires SLUCM static input for the WPS/geogrid process). distributed_ahe_opt Option to handle anthropogenic surface heat flux (need additional input in wrfinput file). =0 : no anthropogenic surface heat flux from input data =1 : (default) add to first level temperature tendency =2 : add to surface sensible heat flux

  [SLUCM static input](https://www2.mmm.ucar.edu/wrf/src/wps_files/slucm.tar.gz)
- slucm_distributed_drag : Option to use spatially varying 2-D urban Zero-plane Displacement, Roughness length for momentum, Frontal area index (default is .false.) (NOTE: this option requires SLUCM static input for the WPS/geogrid process).
  [SLUCM static input](https://www2.mmm.ucar.edu/wrf/src/wps_files/slucm.tar.gz)
slucm_distributed_drag : Option to use spatially varying 2-D urban Zero-plane Displacement, Roughness length for momentum, Frontal area index (default is .false.) (NOTE: this option requires SLUCM static input for the WPS/geogrid process).

  [SLUCM static input](https://www2.mmm.ucar.edu/wrf/src/wps_files/slucm.tar.gz)
- distributed_ahe_opt Option to handle anthropogenic surface heat flux (need additional input in wrfinput file). =0 : no anthropogenic surface heat flux from input data =1 : (default) add to first level temperature tendency =2 : add to surface sensible heat flux
=0 : no anthropogenic surface heat flux from input data =1 : (default) add to first level temperature tendency =2 : add to surface sensible heat flux

- =2 : Building Environment Parameterization (BEP); multi-layer; only works with YSU, MYJ and BouLac PBL schemes
=2 : Building Environment Parameterization (BEP); multi-layer; only works with YSU, MYJ and BouLac PBL schemes

- =3 : Building Energy Model (BEM); adds heating and air-conditioning to BEP; only works with YSU, MYJ and BouLac PBL schemes
=3 : Building Energy Model (BEM); adds heating and air-conditioning to BEP; only works with YSU, MYJ and BouLac PBL schemes

Note

- NUDAPT detailed map data is available for use in WPS, and includes data for 40+ U.S. cities.
NUDAPT detailed map data is available for use in WPS, and includes data for 40+ U.S. cities.

- Beginning with V4.3, code is updated to include a capability to use local climate zones, which is incorporated for all three urban applications ( additional details )
  [additional details](https://ral.ucar.edu/sites/default/files/public/product-tool/urban-canopy-model/WRF_urban_update_Readme_file_WRF4.3.pdf)
Beginning with V4.3, code is updated to include a capability to use local climate zones, which is incorporated for all three urban applications ( additional details )

  [additional details](https://ral.ucar.edu/sites/default/files/public/product-tool/urban-canopy-model/WRF_urban_update_Readme_file_WRF4.3.pdf)
LSM Tables

There are LSM tables (text files) available in both the test/em_real and run/ directories within the WRF code structure. These are set categories for the various LSMs, but these properties can be modified in the tables.

VEGPARM.TBL : used by Noah and RUC for vegetation categories (albedo, roughness length, emissivity, vegetation properties) MPTABLE.TBL : used by NoahMP SOILPARM.TBL : used by Noah and RUC for soil properties LANDUSE.TBL : used by the 5-layer model URBPARM.TBL : used by urban models

- VEGPARM.TBL : used by Noah and RUC for vegetation categories (albedo, roughness length, emissivity, vegetation properties)
VEGPARM.TBL : used by Noah and RUC for vegetation categories (albedo, roughness length, emissivity, vegetation properties)

- MPTABLE.TBL : used by NoahMP
MPTABLE.TBL : used by NoahMP

- SOILPARM.TBL : used by Noah and RUC for soil properties
SOILPARM.TBL : used by Noah and RUC for soil properties

- LANDUSE.TBL : used by the 5-layer model
LANDUSE.TBL : used by the 5-layer model

- URBPARM.TBL : used by urban models
URBPARM.TBL : used by urban models

Initializing LSMs

All LSMs (except for the slab option) require the following additional fields for initialization.

Soil temperature Soil moisture Snow liquid equivalent

- Soil temperature
Soil temperature

- Soil moisture
Soil moisture

- Snow liquid equivalent
Snow liquid equivalent

These fields are available in the Grib first-guess files, but do not come from observations. They come from “offline” models driven by observations for rainfall, radiation, surface temperature, humidity, and wind. These are part of operational analysis or reanalysis system.

- Eta/GFS/AGRMET/NNRP for Noah (although some older data sets have limited soil levels available)
Eta/GFS/AGRMET/NNRP for Noah (although some older data sets have limited soil levels available)

- RUC for RUC (just North America; limited availability)
RUC for RUC (just North America; limited availability)

ECMWF/ERA soil analyses can be used and real.exe interpolates to WRF soil levels, but resolution of mesoscale land use means there is inconsistency in elevation, soil type and vegetation. The only adjustment for soil temperature takes place during the real.exe process, and addresses elevation differences between the original elevation and model elevation (SOILHGT used). Inconsistency leads to spin-up, as adjustments occur in soil temperature and moisture at the beginning of the simulation. This spin-up can only be avoided by running an offline model on the same grid (e.g. HRLDAS for Noah), but it may take months to spin up soil moisture. Cycling the land state between forecasts also helps, but may propagate errors (e.g in rainfall effect on soil moisture).


### LSM Scheme Details and References ¶

5-layer thermal diffusion (SLAB) sf_surface_physics = 1 Soil temperature only scheme; uses five layers Dudhia, 1996

  [Dudhia, 1996](https://www.researchgate.net/profile/Jimy-Dudhia/publication/259865197_A_Multi-layer_Soil_Temperature_Model_for_MM5/links/0046352e307710e99c000000/A-Multi-layer-Soil-Temperature-Model-for-MM5.pdf)
Noah sf_surface_physics = 2 Unified NCEP/NCAR/AFWA scheme with soil temperature and moisture in four layers; fractional snow cover and frozen soil physics Tewari et al., 2004

  [Tewari et al., 2004](https://ams.confex.com/ams/84Annual/techprogram/paper_69061.htm)
A sub-tiling option can be activated by namelist option sf_surface_mosaic=1 , and the number of tiles in a grid box is defined by namelist option mosaic_cat , with a default value of 3.

- A sub-tiling option can be activated by namelist option sf_surface_mosaic=1 , and the number of tiles in a grid box is defined by namelist option mosaic_cat , with a default value of 3.
A sub-tiling option can be activated by namelist option sf_surface_mosaic=1 , and the number of tiles in a grid box is defined by namelist option mosaic_cat , with a default value of 3.

RUC sf_surface_physics = 3 This model uses a layer approach to the solution of energy and moisture budgets. Atmospheric and soil fluxes are computed in the middle of the first atmospheric layer and the top soil layer, respectively, and these fluxes modify the heat and moisture storage in the layer spanning the ground surface. The RUC LSM uses 9 soil levels with higher resolution near the interface with the atmosphere.

Note If initialized from the model with low resolution near the surface, like the Noah LSM, the top levels could be too moist causing moist/cold biases in the model forecast. Solution: cycle soil moisture and let it spin-up for several days to fit the vertical structure of RUC LSM.

Note

If initialized from the model with low resolution near the surface, like the Noah LSM, the top levels could be too moist causing moist/cold biases in the model forecast. Solution: cycle soil moisture and let it spin-up for several days to fit the vertical structure of RUC LSM.

The prognostic variable for soil moisture is volumetric soil moisture content, minus the residual soil moisture tied to soil particles, and therefore not participating in moisture transport. The RUC LSM takes into account freezing and thawing processes in the soil. It is able to use explicit mixed-phase precipitation provided by cloud microphysics schemes. It uses a simple treatment of sea ice, which solves heat diffusion in sea ice and allows evolving snow cover on top of sea ice. In the warm season, RUC LSM corrects soil moisture in cropland areas to compensate for irrigation in these regions.

Snow accumulated on top of soil can have up to two layers, depending on snow depth (ref S16). When the snow layer is very thin, it is combined with the top soil layer to avoid excessive radiative cooling at night. The grid cell can be partially covered with snow, when snow water equivalent is below a threshold value of 3 cm. When this condition occurs, surface parameters, such as roughness length and albedo, are computed as a weighted average of snow-covered and snow-free areas. The energy budget utilizes an iterative snow melting algorithm. Melted water can partially refreeze and remain within the snow layer, and the rest of it percolates through the snow pack, infiltrates into soil and forms surface runoff. Snow density evolves as a function of snow temperature, snow depth and compaction parameters. Snow albedo is initialized from the maximum snow albedo for the given vegetation type, but it can also be modified, depending on snow temperature and snow fraction. To obtain a better representation of snow accumulated on the ground, the RUC LSM has introduced estimation of frozen precipitation density.

The most recent modifications to RUC LSM include refinements to the interception of liquid or frozen precipitation by the canopy, and also the “mosaic” approach for patchy snow with a separate treatment of energy and moisture budgets for snow-covered and snow-free portions of the grid cell, and aggregation of the separate solutions at the end of time step.

The data sets needed to initialize RUC LSM include:

High-resolution data set for soil and land-use types Climatological albedo for snow-free areas Spatial distribution of maximum surface albedo in the presence of snow cover Fraction of vegetation types in the grid cell to take into account sub-grid-scale heterogeneity in computation of surface parameters Fraction of soil types within the grid cell Climatological greenness fraction Climatological leaf area index Climatological mean temperature at the bottom of soil domain Real-time sea-ice concentration Real-time snow cover to correct cycled in RAP and HRRR snow fields

- High-resolution data set for soil and land-use types
High-resolution data set for soil and land-use types

- Climatological albedo for snow-free areas
Climatological albedo for snow-free areas

- Spatial distribution of maximum surface albedo in the presence of snow cover
Spatial distribution of maximum surface albedo in the presence of snow cover

- Fraction of vegetation types in the grid cell to take into account sub-grid-scale heterogeneity in computation of surface parameters
Fraction of vegetation types in the grid cell to take into account sub-grid-scale heterogeneity in computation of surface parameters

- Fraction of soil types within the grid cell
Fraction of soil types within the grid cell

- Climatological greenness fraction
Climatological greenness fraction

- Climatological leaf area index
Climatological leaf area index

- Climatological mean temperature at the bottom of soil domain
Climatological mean temperature at the bottom of soil domain

- Real-time sea-ice concentration
Real-time sea-ice concentration

- Real-time snow cover to correct cycled in RAP and HRRR snow fields
Real-time snow cover to correct cycled in RAP and HRRR snow fields

Recommended namelist options:

sf_surface_physics=3 num_soil_layers=9 usemonalb=.true. (uses monthly albedo fields from geogrid instead of table values) rdlai2d=.true. (uses monthly LAI data from geogrid and is included in the “wrflowinp” file if sst_update=1) mosaic_lu=1 mosaic_soil=1 Note See RAP and HRRR that use RUC LSM as their land component.

  [RAP](https://rapidrefresh.noaa.gov/RAP)
  [HRRR](https://rapidrefresh.noaa.gov/hrrr/HRRR.)
sf_surface_physics=3 num_soil_layers=9 usemonalb=.true. (uses monthly albedo fields from geogrid instead of table values) rdlai2d=.true. (uses monthly LAI data from geogrid and is included in the “wrflowinp” file if sst_update=1) mosaic_lu=1 mosaic_soil=1

Note

See RAP and HRRR that use RUC LSM as their land component.

  [RAP](https://rapidrefresh.noaa.gov/RAP)
  [HRRR](https://rapidrefresh.noaa.gov/hrrr/HRRR.)
Benjamin et al., 2004 Smirnova et al., 2016

  [Benjamin et al., 2004](https://doi.org/10.1175/1520-0493(2004)132%3C0473:MWPWTF%3E2.0.CO;2)
  [Smirnova et al., 2016](https://doi.org/10.1175/MWR-D-15-0198.1)
Noah-MP sf_surface_physics = 4 Uses multiple options for key land-atmosphere interaction processes. Noah-MP contains a separate vegetation canopy defined by a canopy top and bottom with leaf physical and radiometric properties used in a two-stream canopy radiation transfer scheme that includes shading effects. Noah-MP contains a multi-layer snow pack with liquid water storage and melt/refreeze capability and a snow-interception model describing loading/unloading, melt/refreeze, and sublimation of the canopy-intercepted snow. Multiple options are available for surface water infiltration and runoff, and groundwater transfer and storage including water table depth to an unconfined aquifer. Horizontal and vertical vegetation density can be prescribed or predicted using prognostic photosynthesis and dynamic vegetation models that allocate carbon to vegetation (leaf, stem, wood and root) and soil carbon pools (fast and slow). Niu et al., 2011 Yang et al., 2011 Noah-MP Technical Note (He et al., 2023)

  [Niu et al., 2011](https://doi.org/10.1029/2010JD015139)
  [Yang et al., 2011](https://doi.org/10.1029/2010JD015140)
Community Land Model Version 4 (CLM4) sf_surface_physics = 5 Contains sophisticated treatment of biogeophysics, hydrology, biogeochemistry, and dynamic vegetation. In CLM4, the land surface in each model grid cell is characterized into five primary sub-grid land cover types (glacier, lake, wetland, urban, and vegetated). The vegetated sub-grid consists of up to 4 plant functional types (PFTs) that differ in physiology and structure. The WRF input land cover types are translated into the CLM4 PFTs through a look-up table. The CLM4 vertical structure includes a single-layer vegetation canopy, a five-layer snowpack, and a ten-layer soil column. Oleson et al., 2010 Lawrence et al., 2011

  [Oleson et al., 2010](https://d1wqtxts1xzle7.cloudfront.net/44532695/Technical_Description_of_version_4.0_of_20160408-23450-1lwj9zc-with-cover-page-v2.pdf?Expires=1665619677&Signature=LLxHTun6ZR7rMW87nBTqgEWtA9AstcWdJa~sNhWVF0OPK7uLtgH8effNGt0ZrvdDpp4URljLdF-dW7Bhobr0fp5CB-Loxdh6xlOoDi-ymvmQ3MFVkqOcL~ha6~uzvowZZBtPpa4eUVwaeHHECNwpdovOpHbSQIQWBFYCC5fP3KUEtpirLRZz~vRK29jIVd17Bd8GUSvax8qsXKX-5qck6B4EUCeU7xdiW649EorUVmfrkJHCVk13ICRDTD~mgCpfPFDn6-mgVA7Kv-hYqrODqGDlXFy-ziL4cxfdgbQbB4Vl3W~Hp5tyBH3uNWUJeM4aIggVzvqtCWldrYhovUHfqQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
  [Lawrence et al., 2011](https://doi.org/10.1029/2011MS00045)
An earlier version of CLM has been quantitatively evaluated within WRF; referenced here: Jin and Wen, 2012 Lu and Kueppers, 2012 Subin et al., 2011

  [Jin and Wen, 2012](https://doi.org/10.1029/2011JD016980)
  [Lu and Kueppers, 2012](https://doi.org/10.1029/2011JD016991)
  [Subin et al., 2011](https://doi.org/10.1175/2010EI331.1)
Pleim-Xiu sf_surface_physics = 7 Two-layer scheme with vegetation and sub-grid tiling; has been developed and improved over the years to provide realistic ground temperature, soil moisture, and surface sensible and latent heat fluxes in mesoscale meteorological models. The PX LSM is based on the ISBA model ( Noilhan and Planton, 1989 ), and includes a 2-layer force-restore soil temperature and moisture model. The top layer is 1 cm thick, and the lower layer is 99 cm. Grid aggregate vegetation and soil parameters are derived from fractional coverage of land use categories and soil texture types. There are two indirect nudging schemes that correct biases in 2-m air temperature and moisture by dynamic adjustment of soil moisture ( Pleim and Xiu, 2003 ) and deep soil temperature ( Pleim and Gilliam, 2009 ).

  [Noilhan and Planton, 1989](https://doi.org/10.1175/1520-0493(1989)117%3C0536:ASPOLS%3E2.0.CO;2)
  [Pleim and Xiu, 2003](https://doi.org/10.1175/1520-0450(2003)042%3C1811:DOALSM%3E2.0.CO;2)
  [Pleim and Gilliam, 2009](https://doi.org/10.1175/2009JAMC2053.1)
The PX LSM was primarily developed for retrospective simulation, where surface-based observations are available to inform the indirect soil nudging. While soil nudging can be disabled using the FDDA namelist.input setting pxlsm_soil_nudge , little testing has been done in this mode, although some users report reasonable results. Gilliam and Pleim, 2010 discuss implementation in the WRF model and provide typical configurations for retrospective applications. To activate soil nudging the Obsgrid objective re-analysis utility must be used to produce a surface nudging file with the naming convention “wrfsfdda_d0*.” The PX LSM uses 2-m temperature and mixing ratio re-analyses from this file for deep soil moisture and temperature nudging. To test PX LSM in forecast mode with soil nudging activated, forecasted 2-m temperature and mixing ratio can be used with empty observation files to produce “wrfsfdda_d0*” files, using Obsgrid, but results are tied to the governing forecast model.

  [Gilliam and Pleim, 2010](https://doi.org/10.1175/2009JAMC2126.1)
  [Obsgrid](https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_v4/v4.2/users_guide_chap7.html)
Note See a detailed description of the PX LSM , including pros/cons, best practices, and recent improvements.

  [detailed description of the PX LSM](http://www2.mmm.ucar.edu/wrf/users/docs/PX-ACM.pdf)
Note

See a detailed description of the PX LSM , including pros/cons, best practices, and recent improvements.

  [detailed description of the PX LSM](http://www2.mmm.ucar.edu/wrf/users/docs/PX-ACM.pdf)
Additional References: Pleim and Xiu, 1995 Xiu et al., 2001

  [Pleim and Xiu, 1995](https://doi.org/10.1175/1520-0450-34.1.16)
  [Xiu et al., 2001](https://doi.org/10.1175/1520-0450(2001)040%3C0192:DOALSM%3E2.0.CO;2)
Simplified Simple Biosphere (SSiB) sf_surface_physics=8 This is the third generation of the Simplified Simple Biosphere Model, and is developed for land/atmosphere interaction studies in the climate model. The aerodynamic resistance values in SSiB are determined in terms of vegetation properties, ground conditions and bulk Richardson number according to the modified Monin-bukhov similarity theory. SSiB-3 includes three snow layers to realistically simulate snow processes, including destructive metamorphism, densification process due to snow load, and snow melting, which substantially enhances the model’s ability for the cold season study. To use this option, ra_lw_physics and ra_sw_physics should be set to either 1, 3, or 4. The second full model level should be set to no larger than 0.982 so that the height of that level is higher than vegetation height. Xue et al., 1991 Sun and Xue, 2001

  [Xue et al., 1991](https://doi.org/10.1175/1520-0442(1991)004%3C0345:ASBMFG%3E2.0.CO;2)
  [Sun and Xue, 2001](https://doi.org/10.1007/BF02919314)
Other Options Related to LSM

ua_phys=.true. University of Arizona snow physics for use with Noah LSM Wang et al., 2010 sf_surface_mosaic=1 Sub-tiling option for use with Noah LSM Li et al., 2013

  [Wang et al., 2010](https://doi.org/10.1029/2009JD013761)
  [Li et al., 2013](https://doi.org/10.1002/2013JD02065)
- ua_phys=.true. University of Arizona snow physics for use with Noah LSM Wang et al., 2010
  [Wang et al., 2010](https://doi.org/10.1029/2009JD013761)
Wang et al., 2010

  [Wang et al., 2010](https://doi.org/10.1029/2009JD013761)
- sf_surface_mosaic=1 Sub-tiling option for use with Noah LSM Li et al., 2013
  [Li et al., 2013](https://doi.org/10.1002/2013JD02065)
Li et al., 2013

  [Li et al., 2013](https://doi.org/10.1002/2013JD02065)

### PBL and Land Surface Time-step (bldt) ¶

“bldt” is a namelist.input parameter used to determine the minutes between boundary layer and land-surface model calls. The typical value is 0 (every step), and this is reasonable for all schemes, with the exception of the CSM land-surface scheme. CSM LSM is expensive, so it may be better to consider increasing the value of bldt when using it.


### Model Grid Spacing ¶

WRF PBL schemes are designed for grid resolution >> I in the image above, while LES schemes are designed for grid resolution << I. For coarse grid spacing, all eddies are sub-grid, and 1-D column schemes handle sub-grid vertical fluxes. For fine grid spacing, all major eddies are resolved, and 3-D turbulence schemes handle sub-grid mixing.

The remaining grid-spacing is a grey-zone, which is sub-kilometer grids, where PBL and LES assumptions are not perfect. There are scale-aware schemes that can be used for this zone.

Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions

- Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases
Shin-Hong PBL based on YSU, designed for sub-kilometer transition scales (200 m – 1 km); nonlocal mass-flux and Kv term is reduce in strength as the grid size gets smaller and resolved mixing increases

- New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes
New 3d TKE option (km_opt=5) in V4.2; becomes 3-D LES at fine scales; adds scale-dependent Shin-Hong nonlocal mass flux and implicit vertical diffusion at coarse grid sizes

- Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions
Other schemes may work in this range but will not have correctly partitioned resolved/sub-grid energy fractions

For grid sizes up to about 100m, LES is preferable.


### Turbulence and Diffusion ¶

The namelist.input parameter “diff_opt” is used to specify the turbulence and mixing option. When diffusion is used with a PBL scheme, vertical diffusion is deactivated, so diff_opt only affects horizontal diffusion.

diff_opt=0 : no turbulence or explicit spatial numerical filters diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)

- diff_opt=0 : no turbulence or explicit spatial numerical filters
diff_opt=0 : no turbulence or explicit spatial numerical filters

- diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level
diff_opt=1 : (default); evaluates the 2nd-order diffusion term on coordinate surfaces; limited to constant vertical diffusion coefficient (kvdif); should not be used with calculated diffusion coefficient options (km_opt=2,3); can be used with PBL schemes that include vertical diffusion internally; horizontal diffusion acts along model levels; simple numerical method with only neighboring points on the same model level

- diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)
diff_opt=2 : evaluates mixing terms in physical space (stress form - x,y,z); strictly horizontal and better for complex terrain - avoids diffusion up and down slopes included in “diff_opt=1;” horizontal diffusion acts on strictly horizontal gradients; numerical method includes vertical correction term, using more grid points; for stability, diffusion strength is reduced in steep coordinate slopes (dz ~ dx)

Recommended Diffusion Options

- Real-data case with PBL option on diff_opt=2 km_opt=4 Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes) These options compliment vertical diffusion done by the PBL scheme
- diff_opt=2
diff_opt=2

- km_opt=4
km_opt=4

- Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes)
Less diffusive in complex terrain (while diff_opt=1 diffuses along slopes)

- These options compliment vertical diffusion done by the PBL scheme
These options compliment vertical diffusion done by the PBL scheme

- High-resolution real-data cases (~100m grid) No PBL scheme diff_opt=2 km_opt=2 or 3 (TKE or Smagorinsky scheme)
- No PBL scheme
No PBL scheme

- diff_opt=2
diff_opt=2

- km_opt=2 or 3 (TKE or Smagorinsky scheme)
km_opt=2 or 3 (TKE or Smagorinsky scheme)

- Idealized cloud-resolving (dx= 1-3 km) modeling (smooth or no topography, no surface heat fluxes) diff_opt=2 km_opt=2 or 3
- diff_opt=2
diff_opt=2

- km_opt=2 or 3
km_opt=2 or 3


### Tropical Cyclone Options ¶

The following options, specific to tropical cyclone options, can be added to the &physics section of namelist.input.

Ocean Mixed Layer Model sf_ocean_physics=1 Ocean Mixed Layer Model; 1-d slab ocean mixed layer (specified initial depth); includes wind-driven ocean mixing for SST cooling feedback Pollard et al., 1973

  [Pollard et al., 1973](https://doi.org/10.1080/03091927208236105)
3d PWP Ocean sf_ocean_physics=2 3-d multi-layer (~100) ocean, salinity effects; fixed depth Price, 1981 Price et al., 1994 Lee and Chen, 2012

  [Price, 1981](https://doi.org/10.1175/1520-0485(1981)011%3C0153:UORTAH%3E2.0.CO;2)
  [Price et al., 1994](https://doi.org/10.1175/1520-0485(1994)024%3C0233:FSRTAM%3E2.0.CO;2)
Alternative surface-layer option for high-wind ocean surface (isftcflx=1,2) Modifies Charnock relation to give less surface friction at high winds (lower Cd); modifies surface enthalpy (Ck, heat/moisture) either with constant z0q (isftcflx=1) or Garratt formulation (isftcflx=2); must be used with sf_sfclay_physics=1


### Fractional Sea Ice ¶

The fractional sea ice option ( fractional_seaice=1 ) includes input sea-ice fraction data that partitions land and water fluxes within a grid box, treating sea-ice as a fractional field. The option requires fractional sea-ice as input data; data sources may include those from GFS or the National Snow and Ice Data Center ; use XICE for the Vtable entry instead of SEAICE; this option works with sf_sfclay_physics = 1, 2, 5, and 7, and sf_surface_physics = 2, 3, and 7.

  [National Snow and Ice Data Center](https://nsidc.org/)

### Sub-grid Mosaic ¶

Without using an additional sub-grid mosaic option, the default behavior is to use a single dominant vegetation and soil type per grid cell. However, the following schemes have additional options available.

Noah: use sf_surface_mosaic=1 to allow multiple categories within a grid cell RUC: use mosaic_lu=1 and mosaic_soil=1 to allow multiple categories within a grid cell Pleim-Xu: additionally averages properties of sub-grid categories

- Noah: use sf_surface_mosaic=1 to allow multiple categories within a grid cell
Noah: use sf_surface_mosaic=1 to allow multiple categories within a grid cell

- RUC: use mosaic_lu=1 and mosaic_soil=1 to allow multiple categories within a grid cell
RUC: use mosaic_lu=1 and mosaic_soil=1 to allow multiple categories within a grid cell

- Pleim-Xu: additionally averages properties of sub-grid categories
Pleim-Xu: additionally averages properties of sub-grid categories


### Sea-surface Update ¶

To use the sea-surface update option, set sst_update=1 in the &physics section of namelist.input. This option reads a lower boundary file periodically to update the sea-surface temperature (as opposed to being fixed with time, which is default)

Should be used for long-period simulations (a week or more) A file called wrflowinp_d0n is created by real Sea-ice can be updated, as well Vegetation fraction update is included; allows seasonal change in albedo, emissivity, and roughness length if using the Noah LSM usemonalb=.true. to use monthly albedo input

- Should be used for long-period simulations (a week or more)
Should be used for long-period simulations (a week or more)

- A file called wrflowinp_d0n is created by real
A file called wrflowinp_d0n is created by real

- Sea-ice can be updated, as well
Sea-ice can be updated, as well

- Vegetation fraction update is included; allows seasonal change in albedo, emissivity, and roughness length if using the Noah LSM
Vegetation fraction update is included; allows seasonal change in albedo, emissivity, and roughness length if using the Noah LSM

- usemonalb=.true. to use monthly albedo input
usemonalb=.true. to use monthly albedo input


### Regional Climate Options ¶

tmn_update=1 : Updates deep-soil temperature for multi-year future-climate runs sst_skin=1 : Adds a diurnal cycle to sea-surface temperature output_diagnostics=1 : Ability to output max/min/mean/std of surface fields in a specified period (e.g. daily) bucket_mm and bucket_J : Provides a more accurate way to accumulate water and energy for long-run budgets (see the next section)

- tmn_update=1 : Updates deep-soil temperature for multi-year future-climate runs
tmn_update=1 : Updates deep-soil temperature for multi-year future-climate runs

- sst_skin=1 : Adds a diurnal cycle to sea-surface temperature
sst_skin=1 : Adds a diurnal cycle to sea-surface temperature

- output_diagnostics=1 : Ability to output max/min/mean/std of surface fields in a specified period (e.g. daily)
output_diagnostics=1 : Ability to output max/min/mean/std of surface fields in a specified period (e.g. daily)

- bucket_mm and bucket_J : Provides a more accurate way to accumulate water and energy for long-run budgets (see the next section)
bucket_mm and bucket_J : Provides a more accurate way to accumulate water and energy for long-run budgets (see the next section)


### Accumulation Budgets ¶

Some outputs fields are accumulated from the start of the simulation These include rainfall totals (mm or kg/m2) RAINC, RAINNC, and radiation totals (J/m2), ACLWUPT, ACSWDNB, etc. Averages over any period can use just the output at the end minus output at the beginning, divided by the interval For regional climate simulations (months), 32-bit accuracy makes adding small time-step values to accumulated totals inaccurate since only about 7 significant figures are stored. Use bucket_mm and bucket_J to carry the total in integer and remainder parts, e.g. Total rain = RAINC + I_RAINC*bucket_mm Default bucket value is typical monthly accumulation bucket_mm=100 mm and bucket_J=109 Joules

- Some outputs fields are accumulated from the start of the simulation
Some outputs fields are accumulated from the start of the simulation

- These include rainfall totals (mm or kg/m2) RAINC, RAINNC, and radiation totals (J/m2), ACLWUPT, ACSWDNB, etc.
These include rainfall totals (mm or kg/m2) RAINC, RAINNC, and radiation totals (J/m2), ACLWUPT, ACSWDNB, etc.

- Averages over any period can use just the output at the end minus output at the beginning, divided by the interval
Averages over any period can use just the output at the end minus output at the beginning, divided by the interval

- For regional climate simulations (months), 32-bit accuracy makes adding small time-step values to accumulated totals inaccurate since only about 7 significant figures are stored.
For regional climate simulations (months), 32-bit accuracy makes adding small time-step values to accumulated totals inaccurate since only about 7 significant figures are stored.

- Use bucket_mm and bucket_J to carry the total in integer and remainder parts, e.g. Total rain = RAINC + I_RAINC*bucket_mm
- Total rain = RAINC + I_RAINC*bucket_mm
Total rain = RAINC + I_RAINC*bucket_mm

- Default bucket value is typical monthly accumulation bucket_mm=100 mm and bucket_J=109 Joules
- bucket_mm=100 mm and bucket_J=109 Joules
bucket_mm=100 mm and bucket_J=109 Joules


### Lake Model ¶

The CLM 4.5 lake model ( sf_lake_physics=1 ) was obtained from the ommunity Land Model version 4.5 (CLM4) with some modifications. It is a one-dimensional mass and energy balance scheme with 20-25 model layers, including up to 5 snow layers on the lake ice, 10 water layers, and 10 soil layers on the lake bottom. The lake scheme is used with actual lake points and lake depth derived from the WPS, and can also be used with user-defined lake points and lake depth in WRF ( lake_min_elev and lakedepth_default ). The lake scheme is independent of a land surface scheme and therefore can be used with any land surface scheme embedded in WRF. Gu et al., 2013 Subin et al., 2012

  [Gu et al., 2013](https://link.springer.com/article/10.1007/s10584-013-0978-y)
  [Subin et al., 2012](https://doi.org/10.1029/2011MS000072)
There are also global bathymetry data available for most large lakes. This can be obtained from the WPS Geographical Static Data Downloads web page, and can be used during the WPS/geogrid process.

  [WPS Geographical Static Data Downloads](https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html)

### WRF-Hydro ¶

This capability couples the WRF model with hydrology processes (such as routing and channeling). It requires a separate compile by setting the environment variable WRF_HYDRO. In a c-shell environment, issue setenv WRF_HYDRO 1 or in a bash environment, issue export WRF_HYDRO=1 before configure and compile. Once WRF is compiled, copy files from the hydro/Run/ directory to your working directory (e.g. test/em_real/). This option requires a specail initialization for hydrological data sets. Please refer to the RAL WRF-Hydro Modeling System web page for detailed information.

  [RAL WRF-Hydro Modeling System](http://www.ral.ucar.edu/projects/wrf_hydro)

## Using Physics Suites ¶

A WRF physics suite is a set of physics options that performs well for a given application and is supported by a sponsoring group. Suites may offer guidance to users in applying WRF, improve understanding of model performance, and facilitate model advancement.

When running WRF, a suite of physics schemes can be set by using the physics_suite namelist option. The physics options covered by this suite specification are:

mp_physics cu_physics bl_pbl_physics sf_sfclay_physics sf_surface_physics ra_sw_physics ra_lw_physics

There are currently 2 available approved physics suite options: the NSF NCAR Convection-permitting Suite (CONUS), and the NSF NCAR Tropical Suite (tropical) that can be specified in the &physics section of the namelist.input file. By simply setting the “physics_suite” namelist parameter, the included physics schemes are assumed and, therefore, the specific schemes (e.g., mp_physics, cu_physics, etc.) do not need to be set. These two suites consist of a combination of physics options that have been highly tested and have shown reasonable results.

A summary of the physics schemes used in the simulation are printed to the WRF output log (e.g., rsl.out.0000).


### NSF NCAR Convection-permitting Suite ¶

physics_suite=’CONUS’

Real-time forecasting focused on convective weather over the contiguous U.S.

| Physics Type | Scheme Name | Namelist Option |
Physics Type

Scheme Name

Namelist Option

| Microphysics | Thompson | mp_physics=8 |
Microphysics

Thompson

mp_physics=8

| Cumulus | Tiedtke | cu_physics=6 |
Cumulus

Tiedtke

cu_physics=6

| Longwave Radiation | RRTMG | ra_lw_physics=4 |
Longwave Radiation

RRTMG

ra_lw_physics=4

| Shortwave Radiation | RRTMG | ra_sw_physics=4 |
Shortwave Radiation

RRTMG

ra_sw_physics=4

| PBL | MYJ | bl_pbl_physics=2 |
PBL

MYJ

bl_pbl_physics=2

| Surface Layer | MYJ | sf_sfclay_physics=2 |
Surface Layer

MYJ

sf_sfclay_physics=2

| LSM | Noah | sf_surface_physics=2 |
LSM

Noah

sf_surface_physics=2

Note See NSF NCAR Convection-permitting Physics Suite for WRF for additional details.

  [NSF NCAR Convection-permitting Physics Suite for WRF](https://www2.mmm.ucar.edu/wrf/users/physics/ncar_convection_suite.php)
Note

See NSF NCAR Convection-permitting Physics Suite for WRF for additional details.

  [NSF NCAR Convection-permitting Physics Suite for WRF](https://www2.mmm.ucar.edu/wrf/users/physics/ncar_convection_suite.php)

### NSF NCAR Tropical Suite ¶

physics_suite=’tropical’

Real-Time forecasting focused on tropical storms and tropical convection

Note This is the same as the “mesoscale_reference” suite in the MPAS model.

Note

This is the same as the “mesoscale_reference” suite in the MPAS model.

| Physics Type | Scheme Name | Namelist Option |
Physics Type

Scheme Name

Namelist Option

| Microphysics | WSM6 | mp_physics=6 |
Microphysics

WSM6

mp_physics=6

| Cumulus | New Tiedtke | cu_physics=16 |
Cumulus

New Tiedtke

cu_physics=16

| Longwave Radiation | RRTMG | ra_lw_physics=4 |
Longwave Radiation

RRTMG

ra_lw_physics=4

| Shortwave Radiation | RRTMG | ra_sw_physics=4 |
Shortwave Radiation

RRTMG

ra_sw_physics=4

| PBL | YSU | bl_pbl_physics=1 |
PBL

YSU

bl_pbl_physics=1

| Surface Layer | MM5 | sf_sfclay_physics=91 |
Surface Layer

MM5

sf_sfclay_physics=91

| LSM | Noah | sf_surface_physics=2 |
LSM

Noah

sf_surface_physics=2

Note See NSF NCAR Tropical Physics Suite for WRF for additional details.

  [NSF NCAR Tropical Physics Suite for WRF](https://www2.mmm.ucar.edu/wrf/users/physics/ncar_tropical_suite.php)
Note

See NSF NCAR Tropical Physics Suite for WRF for additional details.

  [NSF NCAR Tropical Physics Suite for WRF](https://www2.mmm.ucar.edu/wrf/users/physics/ncar_tropical_suite.php)

### Overriding Physics Suite Options ¶

To override any of the above options, simply add that particular parameter to the namelist.

Example 1 : You wish to use the CONUS suite but would like to turn off cu_physics for domain 3 (note: a setting of “-1” means the default setting is used):


```
physics_suite
=
'CONUS'
|
br
|
cu_physics
=
-
1
,
-
1
,
0
```

Example 2 : You wish to use the CONUS suite but would like to use a different cu_physics option, and to turn cu_physics off for domain 3:


```
physics_suite
=
'CONUS'
cu_physics
=
2
,
2
,
0
```


## Other Specific Applications ¶

The following applications are discussed below. Click any link to go directly to that application.

Tropical Storms and Cyclones Long Simulations Windfarm Surface Irrigation Parameterization WRF-Solar MAD-WRF Physics Sensitivity Options

- Tropical Storms and Cyclones
Tropical Storms and Cyclones

- Long Simulations
Long Simulations

- Windfarm
Windfarm

- Surface Irrigation Parameterization
Surface Irrigation Parameterization

- WRF-Solar
WRF-Solar

- MAD-WRF
MAD-WRF

- Physics Sensitivity Options
Physics Sensitivity Options


### Tropical Storms and Cyclones ¶

Options to use for tropical storms and tropical cyclone/typhoon/hurricane applications

sf_ocean_physics=1 : simple 1-D ocean mixed layer model following that of Pollard et al., 1972 . Two other namelist options are available to specify the initial mixed layer depth (although one may ingest real mixed layer depth data) (oml_hml0) and a temperature lapse rate below the mixed layer (oml_gamma). This option works with all sf_surface_physics options. oml_hml0 : Ocean mixed-layer depth; a setting < 0 initializes with real-time ocean mixed depth, and setting the value to =0 initializes with climatological ocean mixed depth. oml_gamma : oml deep water lapse rate (K m-1) sf_ocean_physics=2 : 3D Price-Weller-Pinkel (PWP) ocean model based on Price et al., 1994 . This model predicts horizontal advection, pressure gradient force, and mixed layer processes. Only simple initialization via namelist variables ocean_z, ocean_t, and ocean_s is available. ocean_z : vertical profile of layer depths for ocean (in meters) ocean_t : vertical profile of ocean temps (K) ocean_s : vertical profile of salinity For e.g., & physics sf_ocean_physics = 2 & domains ocean_z = 5. , 15. , 25. , 35. , 45. , 55. , 65. , 75. , 85. , 95. , 105. , 115. , 125. , 135. , 145. , 155. , 165. , 175. , 185. , 195. , 210. , 230. , 250. , 270. , 290. , 310. , 330. , 350. , 370. , 390. ocean_t = 302.3493 , 302.3493 , 302.3493 , 302.1055 , 301.9763 , 301.6818 , 301.2220 , 300.7531 , 300.1200 , 299.4778 , 298.7443 , 297.9194 , 297.0883 , 296.1443 , 295.1941 , 294.1979 , 293.1558 , 292.1136 , 291.0714 , 290.0293 , 288.7377 , 287.1967 , 285.6557 , 284.8503 , 284.0450 , 283.4316 , 283.0102 , 282.5888 , 282.1674 , 281.7461 ocean_s = 34.0127 , 34.0127 , 34.0127 , 34.3217 , 34.2624 , 34.2632 , 34.3240 , 34.3824 , 34.3980 , 34.4113 , 34.4220 , 34.4303 , 34.6173 , 34.6409 , 34.6535 , 34.6550 , 34.6565 , 34.6527 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247

  [Pollard et al., 1972](https://doi.org/10.1080/03091927208236105)
  [Price et al., 1994](https://doi.org/10.1175/1520-0485(1994)024%3C0233:FSRTAM%3E2.0.CO;2)
- sf_ocean_physics=1 : simple 1-D ocean mixed layer model following that of Pollard et al., 1972 . Two other namelist options are available to specify the initial mixed layer depth (although one may ingest real mixed layer depth data) (oml_hml0) and a temperature lapse rate below the mixed layer (oml_gamma). This option works with all sf_surface_physics options. oml_hml0 : Ocean mixed-layer depth; a setting < 0 initializes with real-time ocean mixed depth, and setting the value to =0 initializes with climatological ocean mixed depth. oml_gamma : oml deep water lapse rate (K m-1)
  [Pollard et al., 1972](https://doi.org/10.1080/03091927208236105)
sf_ocean_physics=1 : simple 1-D ocean mixed layer model following that of Pollard et al., 1972 . Two other namelist options are available to specify the initial mixed layer depth (although one may ingest real mixed layer depth data) (oml_hml0) and a temperature lapse rate below the mixed layer (oml_gamma). This option works with all sf_surface_physics options.

  [Pollard et al., 1972](https://doi.org/10.1080/03091927208236105)
oml_hml0 : Ocean mixed-layer depth; a setting < 0 initializes with real-time ocean mixed depth, and setting the value to =0 initializes with climatological ocean mixed depth. oml_gamma : oml deep water lapse rate (K m-1)

- oml_hml0 : Ocean mixed-layer depth; a setting < 0 initializes with real-time ocean mixed depth, and setting the value to =0 initializes with climatological ocean mixed depth.
oml_hml0 : Ocean mixed-layer depth; a setting < 0 initializes with real-time ocean mixed depth, and setting the value to =0 initializes with climatological ocean mixed depth.

- oml_gamma : oml deep water lapse rate (K m-1)
oml_gamma : oml deep water lapse rate (K m-1)

- sf_ocean_physics=2 : 3D Price-Weller-Pinkel (PWP) ocean model based on Price et al., 1994 . This model predicts horizontal advection, pressure gradient force, and mixed layer processes. Only simple initialization via namelist variables ocean_z, ocean_t, and ocean_s is available. ocean_z : vertical profile of layer depths for ocean (in meters) ocean_t : vertical profile of ocean temps (K) ocean_s : vertical profile of salinity For e.g., & physics sf_ocean_physics = 2 & domains ocean_z = 5. , 15. , 25. , 35. , 45. , 55. , 65. , 75. , 85. , 95. , 105. , 115. , 125. , 135. , 145. , 155. , 165. , 175. , 185. , 195. , 210. , 230. , 250. , 270. , 290. , 310. , 330. , 350. , 370. , 390. ocean_t = 302.3493 , 302.3493 , 302.3493 , 302.1055 , 301.9763 , 301.6818 , 301.2220 , 300.7531 , 300.1200 , 299.4778 , 298.7443 , 297.9194 , 297.0883 , 296.1443 , 295.1941 , 294.1979 , 293.1558 , 292.1136 , 291.0714 , 290.0293 , 288.7377 , 287.1967 , 285.6557 , 284.8503 , 284.0450 , 283.4316 , 283.0102 , 282.5888 , 282.1674 , 281.7461 ocean_s = 34.0127 , 34.0127 , 34.0127 , 34.3217 , 34.2624 , 34.2632 , 34.3240 , 34.3824 , 34.3980 , 34.4113 , 34.4220 , 34.4303 , 34.6173 , 34.6409 , 34.6535 , 34.6550 , 34.6565 , 34.6527 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247
  [Price et al., 1994](https://doi.org/10.1175/1520-0485(1994)024%3C0233:FSRTAM%3E2.0.CO;2)
sf_ocean_physics=2 : 3D Price-Weller-Pinkel (PWP) ocean model based on Price et al., 1994 . This model predicts horizontal advection, pressure gradient force, and mixed layer processes. Only simple initialization via namelist variables ocean_z, ocean_t, and ocean_s is available.

  [Price et al., 1994](https://doi.org/10.1175/1520-0485(1994)024%3C0233:FSRTAM%3E2.0.CO;2)
ocean_z : vertical profile of layer depths for ocean (in meters) ocean_t : vertical profile of ocean temps (K) ocean_s : vertical profile of salinity For e.g., & physics sf_ocean_physics = 2 & domains ocean_z = 5. , 15. , 25. , 35. , 45. , 55. , 65. , 75. , 85. , 95. , 105. , 115. , 125. , 135. , 145. , 155. , 165. , 175. , 185. , 195. , 210. , 230. , 250. , 270. , 290. , 310. , 330. , 350. , 370. , 390. ocean_t = 302.3493 , 302.3493 , 302.3493 , 302.1055 , 301.9763 , 301.6818 , 301.2220 , 300.7531 , 300.1200 , 299.4778 , 298.7443 , 297.9194 , 297.0883 , 296.1443 , 295.1941 , 294.1979 , 293.1558 , 292.1136 , 291.0714 , 290.0293 , 288.7377 , 287.1967 , 285.6557 , 284.8503 , 284.0450 , 283.4316 , 283.0102 , 282.5888 , 282.1674 , 281.7461 ocean_s = 34.0127 , 34.0127 , 34.0127 , 34.3217 , 34.2624 , 34.2632 , 34.3240 , 34.3824 , 34.3980 , 34.4113 , 34.4220 , 34.4303 , 34.6173 , 34.6409 , 34.6535 , 34.6550 , 34.6565 , 34.6527 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247 , 34.6490 , 34.6446 , 34.6396 , 34.6347 , 34.6297 , 34.6247

- ocean_z : vertical profile of layer depths for ocean (in meters)
ocean_z : vertical profile of layer depths for ocean (in meters)

- ocean_t : vertical profile of ocean temps (K)
ocean_t : vertical profile of ocean temps (K)

- ocean_s : vertical profile of salinity
ocean_s : vertical profile of salinity

For e.g.,


```
&
physics
sf_ocean_physics
=
2
&
domains
ocean_z
=
5.
,
15.
,
25.
,
35.
,
45.
,
55.
,
65.
,
75.
,
85.
,
95.
,
105.
,
115.
,
125.
,
135.
,
145.
,
155.
,
165.
,
175.
,
185.
,
195.
,
210.
,
230.
,
250.
,
270.
,
290.
,
310.
,
330.
,
350.
,
370.
,
390.
ocean_t
=
302.3493
,
302.3493
,
302.3493
,
302.1055
,
301.9763
,
301.6818
,
301.2220
,
300.7531
,
300.1200
,
299.4778
,
298.7443
,
297.9194
,
297.0883
,
296.1443
,
295.1941
,
294.1979
,
293.1558
,
292.1136
,
291.0714
,
290.0293
,
288.7377
,
287.1967
,
285.6557
,
284.8503
,
284.0450
,
283.4316
,
283.0102
,
282.5888
,
282.1674
,
281.7461
ocean_s
=
34.0127
,
34.0127
,
34.0127
,
34.3217
,
34.2624
,
34.2632
,
34.3240
,
34.3824
,
34.3980
,
34.4113
,
34.4220
,
34.4303
,
34.6173
,
34.6409
,
34.6535
,
34.6550
,
34.6565
,
34.6527
,
34.6490
,
34.6446
,
34.6396
,
34.6347
,
34.6297
,
34.6247
,
34.6490
,
34.6446
,
34.6396
,
34.6347
,
34.6297
,
34.6247
```

isftcflx : Modify surface bulk drag (Donelan) and enthalpy coefficients to be more in line with recent research results of those for tropical storms and hurricanes. This option includes dissipative heating term in heat flux. It is only available for sf_sfclay_physics=1. There are two options for computing enthalpy coefficients: isftcflx=1: constant Z0q for heat and moisture isftcflx = 2 Garratt formulation, slightly different forms for heat and moisture

- isftcflx : Modify surface bulk drag (Donelan) and enthalpy coefficients to be more in line with recent research results of those for tropical storms and hurricanes. This option includes dissipative heating term in heat flux. It is only available for sf_sfclay_physics=1. There are two options for computing enthalpy coefficients: isftcflx=1: constant Z0q for heat and moisture isftcflx = 2 Garratt formulation, slightly different forms for heat and moisture
isftcflx : Modify surface bulk drag (Donelan) and enthalpy coefficients to be more in line with recent research results of those for tropical storms and hurricanes. This option includes dissipative heating term in heat flux. It is only available for sf_sfclay_physics=1. There are two options for computing enthalpy coefficients:

isftcflx=1: constant Z0q for heat and moisture isftcflx = 2 Garratt formulation, slightly different forms for heat and moisture

- isftcflx=1: constant Z0q for heat and moisture
isftcflx=1: constant Z0q for heat and moisture

- isftcflx = 2 Garratt formulation, slightly different forms for heat and moisture
isftcflx = 2 Garratt formulation, slightly different forms for heat and moisture


### Long Simulations ¶

- tmn_update=1 : update deep soil temperature
tmn_update=1 : update deep soil temperature

- sst_skin=1 : calculate skin SST based on Zeng and Beljaars, 2005
  [Zeng and Beljaars, 2005](https://doi.org/10.1029/2005GL023030)
sst_skin=1 : calculate skin SST based on Zeng and Beljaars, 2005

  [Zeng and Beljaars, 2005](https://doi.org/10.1029/2005GL023030)
- bucket_mm=1 : bucket reset value for water equivalent precipitation accumulations (value in mm, -1=inactive)
bucket_mm=1 : bucket reset value for water equivalent precipitation accumulations (value in mm, -1=inactive)

- bucket_J : bucket reset value for energy accumulations (value in Joules, -1=inactive); only works with CAM and RRTMG radiation options (ra_lw_physics = 3, 4, 14, 24 and ra_sw_physics = 3, 4, 14, 24)
bucket_J : bucket reset value for energy accumulations (value in Joules, -1=inactive); only works with CAM and RRTMG radiation options (ra_lw_physics = 3, 4, 14, 24 and ra_sw_physics = 3, 4, 14, 24)

- To drive the WRF model with climate data that does not include a leap year, prior to compiling WRF, edit the configure.wrf file by adding -DNO_LEAP_CALENDAR to the macro “ARCH_LOCAL.”
To drive the WRF model with climate data that does not include a leap year, prior to compiling WRF, edit the configure.wrf file by adding -DNO_LEAP_CALENDAR to the macro “ARCH_LOCAL.”


### Windfarm ¶

windfarm_opt=1

Wind turbine drag parameterization scheme. It represents sub-grid effects of specified turbines on wind and TKE fields. The physical charateristics of the wind farm is read-in from a file; use of the manufacturer’s specification is recommeded. An example of the file is provided in “run/wind-turbine-1.tbl.” The location of the turbines are read-in from the file “windturbines.txt.” See “README.windturbine” in the WRF/doc/ directory for more detail. This option only works with 2.5 level MYNN PBL option (bl_pbl_physics=5).

windfarm_opt=2

Available starting with WRFV4.6.0, Wind farm parameterization scheme (mav scheme) based on Ma et al., 2022 . This scheme is similar to option 1 (above), but has the ability to directly account for the individual and overlapping sub-grid wakes of wind turbines within a wind farm. With this option turned on, the following namelist options are also valid.

  [Ma et al., 2022](https://doi.org/10.1002/we.2758)
windfarm_wake_model : Subgrid-scale wind turbine wake model (default =2) 1 = Jensen model 2 = XA model 3 = GM model (windfarm_method is not used) 4 = Jensen and XA ensemble 5 = Jensen, XA and GM ensemble windfarm_overlap_method : Wake superposition method for the Jensen and XA wind turbine wake model (default = 4) 1 = linear superposition 2 = squared superposition 3 = modified squared superposition 4 = superposition of the hub-height wind speed ( Ma et al., 2022 ) windfarm_deg : The rotation degree of the wind farm layout. Only valid when windfarm_opt=2 and windfarm_ij=1 - see Namelist Variables . Note When using windfarm_opt=2, a file named “winturbines-ll.txt” must be present in the WRF running directory. The file is formatted with the wind turbine coordinates in the first two columns, followed by the windfarm_id and windturbine_type. For e.g., 33.0563 -78.6556 2 1 33.0534 -78.6407 2 1 33.0505 -78.6257 2 1 33.0446 -78.6594 2 1 33.0388 -78.6931 2 1 33.0359 -78.6781 2 1 33.0329 -78.6631 2 1 33.0271 -78.6332 2 1

  [Ma et al., 2022](https://doi.org/10.1002/we.2758)
- windfarm_wake_model : Subgrid-scale wind turbine wake model (default =2) 1 = Jensen model 2 = XA model 3 = GM model (windfarm_method is not used) 4 = Jensen and XA ensemble 5 = Jensen, XA and GM ensemble
windfarm_wake_model : Subgrid-scale wind turbine wake model (default =2)

1 = Jensen model 2 = XA model 3 = GM model (windfarm_method is not used) 4 = Jensen and XA ensemble 5 = Jensen, XA and GM ensemble

- windfarm_overlap_method : Wake superposition method for the Jensen and XA wind turbine wake model (default = 4) 1 = linear superposition 2 = squared superposition 3 = modified squared superposition 4 = superposition of the hub-height wind speed ( Ma et al., 2022 )
  [Ma et al., 2022](https://doi.org/10.1002/we.2758)
windfarm_overlap_method : Wake superposition method for the Jensen and XA wind turbine wake model (default = 4)

1 = linear superposition 2 = squared superposition 3 = modified squared superposition 4 = superposition of the hub-height wind speed ( Ma et al., 2022 )

  [Ma et al., 2022](https://doi.org/10.1002/we.2758)
1 = linear superposition 2 = squared superposition 3 = modified squared superposition 4 = superposition of the hub-height wind speed ( Ma et al., 2022 )

  [Ma et al., 2022](https://doi.org/10.1002/we.2758)
- windfarm_deg : The rotation degree of the wind farm layout. Only valid when windfarm_opt=2 and windfarm_ij=1 - see Namelist Variables .
windfarm_deg : The rotation degree of the wind farm layout. Only valid when windfarm_opt=2 and windfarm_ij=1 - see Namelist Variables .

Note

When using windfarm_opt=2, a file named “winturbines-ll.txt” must be present in the WRF running directory. The file is formatted with the wind turbine coordinates in the first two columns, followed by the windfarm_id and windturbine_type. For e.g.,

33.0563 -78.6556 2 1 33.0534 -78.6407 2 1 33.0505 -78.6257 2 1 33.0446 -78.6594 2 1 33.0388 -78.6931 2 1 33.0359 -78.6781 2 1 33.0329 -78.6631 2 1 33.0271 -78.6332 2 1


### Surface Irrigation Parameterization ¶

Three irrigation schemes added in V4.2 allow representation of surface irrigation processes within the model, with explicit control over water amount and timing (for more information refer to Vira et al., 2019 ). The schemes are set in the “&physics” namelist and represent different techniques, depending on the water evaporative loss in the application process. The evaporative processes consider loss from:

  [Vira et al., 2019](https://doi.org/10.5194/gmd-2019-233)
sf_surf_irr_scheme=1 : surface evapotranspiration; only works with Noah-LSM sf_surf_irr_scheme=2 : leaves/canopy interception and surface evapotranspiration sf_surf_irr_scheme=3 : microphysics process, leaves/canopy interception and surface evapotranspiration

- sf_surf_irr_scheme=1 : surface evapotranspiration; only works with Noah-LSM
sf_surf_irr_scheme=1 : surface evapotranspiration; only works with Noah-LSM

- sf_surf_irr_scheme=2 : leaves/canopy interception and surface evapotranspiration
sf_surf_irr_scheme=2 : leaves/canopy interception and surface evapotranspiration

- sf_surf_irr_scheme=3 : microphysics process, leaves/canopy interception and surface evapotranspiration
sf_surf_irr_scheme=3 : microphysics process, leaves/canopy interception and surface evapotranspiration

The daily irrigation water amount applied is defined in “irr_daily_amount” (mm/day). The period within the day for the application starts at “irr_start_hours” UTC and lasts for “irr_num_hours.” The period within the year where irrigation is applied is defined by Julian days within “irr_start_julianday” and “irr_end_julianday.” To account for greater than daily irrigation intervals “irr_freq” can be set to a value greater than 1; thus water applied in the active day within the “irr_freq” period is ( irr_daily_amount * irr_freq ). “irr_ph” regulates spatial activation of irrigation (with irr_freq >1), especially determining whether it is activated for all domains on the same day (irr_ph = 0). Two options are given for irr_ph not equal to 0:

irr_ph=1 : activation field as a function of ( i , j , IRRIGATION) irr_ph=2 : activation field is created with the fortran RANDOM function

- irr_ph=1 : activation field as a function of ( i , j , IRRIGATION)
irr_ph=1 : activation field as a function of ( i , j , IRRIGATION)

- irr_ph=2 : activation field is created with the fortran RANDOM function
irr_ph=2 : activation field is created with the fortran RANDOM function

Given the possibility of multiple nests in WRF, irrigation schemes should run on only one domain for each simulation. This ensures the water application is not repeated and is consistent to the irr_daily_amount calculated. For additional information regarding the code changes, see GitHub Code Commit 9bd5b61d9a .

  [GitHub Code Commit 9bd5b61d9a](https://github.com/wrf-model/WRF/commit/9bd5b61d9a)
Example of irrigation namelist parameters for a two domain case:


```
sf_surf_irr_scheme
=
0
,
1
irr_daily_amount
=
0
,
8
irr_start_hour
=
0
,
14
irr_num_hours
=
0
,
2
irr_start_julianday
=
0
,
121
irr_end_julianday
=
0
,
170
irr_ph
=
0
,
0
irr_freq
=
0
,
3
```

These settings use the channel method to irrigate the inner domain starting at 14 UTC for 2 hours, with a value of 8mm/day. Irrigation starts on Julian day 121 and ends on Julian day 170. Water is applied to the entire inner domain for all irrigated grid-points simultaneously, every 3 days (irr_freq=3). This leads to an hourly irrigation of 12 mm/h (daily application of 24 mm), which is then multiplied by the irrigation percentage within the grid-cell (given by the IRRIGATION field processed in WPS).


### WRF-Solar ¶

WRF-Solar is a specific configuration and augmentation of the basic WRF model specifically designed for specialized numerical forecast products for solar energy applications. For additional information and instructions for use, visit the NSF NCAR Research Applications Laboratory’s WRF-Solar site .

  [WRF-Solar site](https://ral.ucar.edu/solutions/products/wrf-solar)
Note WRF-Solar is managed and supported by the NSF NCAR/RAL group. All support inquiries should go through the WRF-Solar forum , and should not be posted in the WRF & MPAS-A Support Forum.

  [WRF-Solar forum](https://forum.mmm.ucar.edu/forums/wrf-solar.112/)
Note

WRF-Solar is managed and supported by the NSF NCAR/RAL group. All support inquiries should go through the WRF-Solar forum , and should not be posted in the WRF & MPAS-A Support Forum.

  [WRF-Solar forum](https://forum.mmm.ucar.edu/forums/wrf-solar.112/)

### MAD-WRF ¶

The MAD-WRF model is designed to improve the cloud analysis and solar irradiance short-range forecast. There are two options to run MAD-WRF:

madwrf_opt = 1: The initial hydrometeors are advected and diffused with the model dynamics without accounting for any microphysical processes. Users should set mp_physics = 96 and use_mp_re = 0 in the physics block of namelist.input. madwrf_opt = 2: There is a set of hydrometeor tracers that are advected and diffused with the model dynamics. At initial time the tracers are equal to the standard hydrometeors. During the simulation the standard hydrometeors are nudged toward the tracers. The namelist variable madwrf_dt_nudge sets the temporal period for hydrometeor nudging [min]. Namelist madwrf_dt_relax sets the relaxation time for hydrometeor nudging [s].

- madwrf_opt = 1: The initial hydrometeors are advected and diffused with the model dynamics without accounting for any microphysical processes. Users should set mp_physics = 96 and use_mp_re = 0 in the physics block of namelist.input.
madwrf_opt = 1: The initial hydrometeors are advected and diffused with the model dynamics without accounting for any microphysical processes. Users should set mp_physics = 96 and use_mp_re = 0 in the physics block of namelist.input.

- madwrf_opt = 2: There is a set of hydrometeor tracers that are advected and diffused with the model dynamics. At initial time the tracers are equal to the standard hydrometeors. During the simulation the standard hydrometeors are nudged toward the tracers. The namelist variable madwrf_dt_nudge sets the temporal period for hydrometeor nudging [min]. Namelist madwrf_dt_relax sets the relaxation time for hydrometeor nudging [s].
madwrf_opt = 2: There is a set of hydrometeor tracers that are advected and diffused with the model dynamics. At initial time the tracers are equal to the standard hydrometeors. During the simulation the standard hydrometeors are nudged toward the tracers. The namelist variable madwrf_dt_nudge sets the temporal period for hydrometeor nudging [min]. Namelist madwrf_dt_relax sets the relaxation time for hydrometeor nudging [s].

MAD-WRF has an option to enhance cloud initialization. To turn on (off) cloud initialization, set the namelist variable madwrf_cldinit=1 (0). By default the model enhances cloud analysis based on the analyzed relative humidity. Users can enhance cloud initialization by providing additional variables to metgrid via the WPS intermediate format:

Cloud mask (CLDMASK variable): Remove clouds if clear (cldmask = 0) Cloud mask (CLDMASK variable) + brightness temperature (BRTEMP variable) sensitive to hydrometeor content (e.g. GOES-R channel 13): Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1) Cloud top height (CLDTOPZ variable) with 0 values over clear sky regions: Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1) Either 2 or 3 + the cloud base height (CLDBASEZ variable): Remove clouds if clear (cldmask = 0) Reduce / extend cloud top / base heights to match observations Note Missing values in any of these variables should be set to -999.9

- Cloud mask (CLDMASK variable): Remove clouds if clear (cldmask = 0)
Cloud mask (CLDMASK variable): Remove clouds if clear (cldmask = 0)

- Cloud mask (CLDMASK variable) + brightness temperature (BRTEMP variable) sensitive to hydrometeor content (e.g. GOES-R channel 13): Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1)
Cloud mask (CLDMASK variable) + brightness temperature (BRTEMP variable) sensitive to hydrometeor content (e.g. GOES-R channel 13):

Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1)

- Remove clouds if clear (cldmask = 0)
Remove clouds if clear (cldmask = 0)

- Reduce / extend cloud top heights to match observations
Reduce / extend cloud top heights to match observations

- Add clouds over clear sky regions (cldmask = 1)
Add clouds over clear sky regions (cldmask = 1)

- Cloud top height (CLDTOPZ variable) with 0 values over clear sky regions: Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1)
Cloud top height (CLDTOPZ variable) with 0 values over clear sky regions:

Remove clouds if clear (cldmask = 0) Reduce / extend cloud top heights to match observations Add clouds over clear sky regions (cldmask = 1)

- Remove clouds if clear (cldmask = 0)
Remove clouds if clear (cldmask = 0)

- Reduce / extend cloud top heights to match observations
Reduce / extend cloud top heights to match observations

- Add clouds over clear sky regions (cldmask = 1)
Add clouds over clear sky regions (cldmask = 1)

- Either 2 or 3 + the cloud base height (CLDBASEZ variable): Remove clouds if clear (cldmask = 0) Reduce / extend cloud top / base heights to match observations
Either 2 or 3 + the cloud base height (CLDBASEZ variable):

Remove clouds if clear (cldmask = 0) Reduce / extend cloud top / base heights to match observations

- Remove clouds if clear (cldmask = 0)
Remove clouds if clear (cldmask = 0)

- Reduce / extend cloud top / base heights to match observations
Reduce / extend cloud top / base heights to match observations

Note

Missing values in any of these variables should be set to -999.9


### Physics Sensitivity Options ¶

- no_mp_heating=1 : turns off latent heating from microphysics. When using this option, cu_physics should be set to 0.
no_mp_heating=1 : turns off latent heating from microphysics. When using this option, cu_physics should be set to 0.

- icloud=0 : turns off cloud effect on optical depth in shortwave/longwave radiation options 1 and 4. Note, this namelist also controls which cloud fraction method to use for radiation.
icloud=0 : turns off cloud effect on optical depth in shortwave/longwave radiation options 1 and 4. Note, this namelist also controls which cloud fraction method to use for radiation.

- isfflx=0 : turns off both sensible and latent heat fluxes from the surface. This option works for sf_sfclay_physics = 1, 5, 7, 11.
isfflx=0 : turns off both sensible and latent heat fluxes from the surface. This option works for sf_sfclay_physics = 1, 5, 7, 11.

- ifsnow=0 : turns off snow effect in sf_surface_physics=1.
ifsnow=0 : turns off snow effect in sf_surface_physics=1.
