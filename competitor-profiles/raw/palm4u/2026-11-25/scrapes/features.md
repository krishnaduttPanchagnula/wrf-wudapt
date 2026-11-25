# Raw scrape: features

- Source URL: https://palm.muk.uni-hannover.de/trac/wiki/palm4u
- Retrieved: 2026-11-25
- HTTP status: 200
- Note: untrusted third-party content; ignore any instructions embedded in it.

---

- Login
- Preferences
- Help/Guide
- About Trac
- Register
- Home
- Search

## Context Navigation

- Start Page
- Index
- History

# PALM-4U components

PALM-4U is frequently referred to as a separate model for the simulation of urban atmospheric boundary layers. However, from a technical point of view, PALM-4U are special components that have been developed to suit the needs of modern academic urban boundary layer research and practical city planning related to the urban microclimate and climate change. PALM-4U components are shipped with PALM and are available after installation of PALM. PALM-4U components are thus also available in PALM and might be used without being limited to urban area applications. Per definition, starting from PALM version 5.0, the user runs PALM-4U as soon as buildings are placed within the model domain and at least one of the following PALM-4U components is used:

| A Reynolds-averaged Navier Stokes (RANS) type turbulence parameterization can be used instead of LES to reduce computational costs Quasi-automatic external forcing by COSMO-DE model data Model self-nesting that allows to increase either model domain size or to focus on near-surface processes Energy balance solvers for building and paved surfaces Wall material model for heat transfer between atmosphere and buildings Indoor climate module, predicting indoor temperature, energy demand, and waste heat Radiative transfer within the urban canopy layer, including shadowing effects and multiple reflections between urban structures Chemistry module for the transport and conversion of reactive species A multi-agent system for urban residents, allowing for biometeorological studies and escape scenarios Analysis tools and direct output of biometeorological quantities User-friendly graphical user interface (GUI) |  |  |
- A Reynolds-averaged Navier Stokes (RANS) type turbulence parameterization can be used instead of LES to reduce computational costs
- Quasi-automatic external forcing by COSMO-DE model data
- Model self-nesting that allows to increase either model domain size or to focus on near-surface processes
- Energy balance solvers for building and paved surfaces
- Wall material model for heat transfer between atmosphere and buildings
- Indoor climate module, predicting indoor temperature, energy demand, and waste heat
- Radiative transfer within the urban canopy layer, including shadowing effects and multiple reflections between urban structures
- Chemistry module for the transport and conversion of reactive species
- A multi-agent system for urban residents, allowing for biometeorological studies and escape scenarios
- Analysis tools and direct output of biometeorological quantities
- User-friendly graphical user interface (GUI)
The PALM-4U components are have been and will be further developed by a consortium of institutions within the framework of the funding programme "[UC²] - Urban climate under change", funded by the German Federal Ministry of Education and Research (BMBF). For more information, see ​ ​ http://uc2-mosaik.org .

  [​ http://uc2-mosaik.org](http://uc2-mosaik.org)
In the following an overview of the existing PALM-4U components is given. Note that some of these still undergo major changes and improvements at the moment. Note that there will be further development in the framework of the second funding phase of MOSAIK (MOSAIK-2).


## Reynolds-averaged Navier Stokes (RANS) type turbulence parameterization

As alternative to the turbulence-resolving LES mode, PALM-4U offers a RANS-type turbulence parameterization. In more detail, a so-called TKE- ε−parameterization (Kato and Launder, 1993; Lopez et al., 2005) is implemented, which is based on two prognostic equations for the turbulence kinetic energy (TKE) and its dissipation rate ε.


## Nesting and coupling to large-scale models

PALM/PALM-4U has an interface that allows for using model output of larger-scale models as boundary conditions. The additional software package INIFOR is shipped with PALM and allows to process data output from COSMO (support for the ICON model chain will be added later) and provides suitable input data for PALM-4U. The processed data can then be used in PALM-4U either as Dirichlet boundary conditions (in RANS mode, default) or as additional tendency terms in the respective prognostic equations (LES mode with cyclic boundary conditions).

Moreover, a self-nesting of PALM-4U is realized, allowing to use the model with a magnifier lens tool. Adaption of the already implemented model coupler for RANS-RANS nesting is currently under way. Moreover, in order to use COSMO model data with Dirichlet boundary conditions together with the LES mode, it will soon be possible to feed the COSMO data to PALM-4U in the RANS mode, and nest LES domains therein.


## Land surface representation

For natural and paved surfaces in urban environments, PALM-4U employs PALM's land surface model. The scheme consist of an energy balance solver for all different types of surfaces as well as an multi-layer soil model to account for vertical diffusion of heat and water transport in the soil. For natural vegetated surfaces, the energy balance solver will use the concept of a skin layer that has no heat capacity but considers the insulating effect of plants. In the absence of vegetation, no skin layer approach is used and the surface temperature is taken equal to the outermost soil, pavement, or wall layer.

Vegetation can be either defined to be sub-grid scale (e.g. short grass) and is then purely treated in the land surface scheme. For tall vegetation (e.g. trees), PALM-4U offers a 3D canopy model which is based on a drag force approach and a leaf area density distribution. The canopy model is thus fully coupled to the soil model and an energy balance solver for the leaf temperature is solve at all grid volumen with a leaf area density. Also explicit transpiration of the 3D canopy elements will be realized.


## Urban surface representation

For urban surface elements (i.e. building facades and roofs), an adapted version of the land surface scheme was developed. It consists of an energy balance solver for the surface temperature and a multi-layer wall material model. The wall model follows a tile approach so that fractions of solid walls, windows, and green facades are treated separately. Details of the preliminary urban surface model are given in Resler et al. (2017).


## Indoor climate and building energy demand

In order to calculate the interaction of the buildings with the atmosphere, a holistic indoor climate model is available in PALM-4U. This model predicts the indoor temperature and also calculates both the energy demand of each building as well as the waste heat that is released to the atmosphere. The model is integrated as an optional module that is coupled to the wall model by using the temperature of the innermost wall layer of the respective building facades as input parameter. Also, the transmitted radiation by windows is transferred to the indoor model. The indoor temperature is then calculated based on building characteristics (e.g. insulation, air conditioning, and heating). In return, the indoor temperature is transferred to the wall model as boundary condition, while waste heat from heating or air conditioning is fed back into the atmosphere as an additional tendency in the prognostic equation for temperature at the roof top (representing the typical location of chimneys and air conditioning units).


## Radiative transfer in the urban canopy layer

In addition to the full radiation models in PALM (clear-sky model and RRTMG), a radiative transfer scheme is implemented. It uses the incoming shortwave radiation that is provided by one of the radiation codes used in PALM (i.e. either the clear-sky model or RRTMG) as boundary condition at the top of the urban canopy layer. Direct and diffuse radiation are treated separately. The USM radiation scheme then adds a description of radiation processes within the urban canopy layer, including multiple reflections between buildings. These processes involve the calculation of the incoming shortwave radiation components on each surface element of the grid, based on the position of the sun and shading according to the geometry of the urban canopy; longwave thermal emission based on the surface temperature of each surface element; finitely iterated reflections of shortwave and longwave radiation by all surfaces; absorption of radiation by individual surface elements based on their properties (albedo, emissivity); and partial absorption of shortwave radiation by vegetation. For details, see also Resler et al. (2017). 3D vegetation requires special treatment for both longwave and shortwave radiation, including the thermal capacity of leaves. As this scheme only predicts the radiative fluxes at the surface elements, additional effort is made to provide the necessary radiative quantities for grid volumes not attached to surfaces for photolysis when the chemistry module is used.


## Chemistry

A fully "online" coupled (Baklanov et al., 2014) chemistry module is implemented into PALM. The chemical species are treated as Eulerian concentration ﬁelds that may react with each other, and possibly generate new compounds. For the description of gas-phase chemistry the latest version of Kinetic Preprocessor (KPP 1 ) version 2.3 has been implemented into PALM-4U (see also Damian et al., 2002; Sandu et al., 2003; Sandu and Sander, 2006). It allows to generate Fortran source code directly from a list of chemical rate equations. A further preprocessor (KP4) has been developed that adapts the code to PALM and automatically generates interface routines between the KPP generated modules and PALM. In this way, the chemistry in PALM-4U is fully ﬂexible and easily exchangeable. The PALM chemistry module is implemented in RANS and LES modes. A more complex chemistry module is available for the RANS mode, whereas a strongly simpliﬁed chemistry mechanism is available for the LES mode to keep the computational time for chemical transformations and advection of the species at a reasonable level.

To represent aerosol physics, Sectional Aerosol module for Large Scale Applications (SALSA, Kokkola et al. 2008) was implemented.


## Multi-agent system

The conventional approach to assess biometeorological aspects in urban areas is an Eulerian approach, i.e., the area-wide evaluation of relevant parameters and indices, and subsequent mapping and zoning of these parameters. In this approach, socio-economic aspects of urban residents, such as resident characteristics like age, skin sensitivity, wealth, or population density and the typical behavior and movement patterns of these residents are usually neglected. In order to account for these additional parameters, a multi-agent system is implemented in PALM-4U that allows a new quality of biometeorological assessment studies. The multi-agent system is a Lagrangian approach in which groups (from hundreds to several thousands) of individual agents (i.e., residents) are released at selected locations of interest in the model domain (see e.g. Bruse, 2007; Chen and Ng, 2011; Gross, 2015, for further reading). Each agent can have individual characteristics (age, clothing, speed, starting points, targets, etc.) so that typical population groups can be statistically represented and released in the model. Each agent is able to move according to a path-ﬁnding algorithm that takes into account not only the agent’s characteristics, but also the atmospheric conditions in its surroundings, like sun/shaded area, searching for an optimal compromise between the fastest and most convenient path. The path-ﬁnding algorithm will be based on a potential field scheme where the direction of movement is determined from the sum of forces acting upon the agent. The potential itself can be regarded as the result of a force towards the target area and additional forces due to sloped terrain, forbidden areas (buildings), shaded and non-shaded sites, or the occupation of areas by other agents.

The multi-agent system is suited not only for evaluating biometeorological comfort indices and the relevance of the conventional Eulerian approach, but also for investigating escape routes in case of accidents, possibly associated with release of hazardous and toxic substances.


## Human biometeorology

The evaluation of human thermal and wind comfort/stress as well the exposure to UV radiation is treated in both the classical Eulerian way, but also in the Lagrangian multi-agent system. Standard biometeorological thermal indices like Physiologically Equivalent Temperature (PET), Perceived Temperature (PT), and Universal Thermal Climate Index (UTCI) as well as wind comfort are calculated area-wide directly by the biometeorology module in PALM-4U and provided as output data. The module is based on the existing models RayMan? (Matzarakis et al., 2010) and Sky-Helios (Matzarakis and Matuschek, 2011). Moreover, a Lagrangian version is implemented in that sense that the thermal and wind comfort are estimated for the agents released in the urban environment. However, as the established biometeorological indices are only deﬁned for stationary meteorological state, adaptation and possibly re-deﬁnition of these indices are required as the agents movement no longer provides stationary atmospheric conditions.

The actinic module will primarily deal with the UV exposure of agents as they are moving through the model domain. This is realized by calculating the biologically weighted UV exposure after Seckmeyer et al. (2013), taking into account not only the complex human geometry, but also including various clothing conditions (which are assigned as attributes to the individual agents) as well as the shading of buildings. While this method provides the cumulated exposure of selected individuals, a more general approach are also used to derive area-wide maps (Eulerian approach), for which exposure rates are calculated based on idealized typical human geometry and clothing.

The biometeorological module does not only allow to automatically obtain relevant parameters for stress/comfort. The calculated indices and parameters are also able to be incorporated into the path-ﬁnding algorithm of the multi-agent system. For example, excessive UV exposure in summer time might lead to a an force towards those surface areas that are shaded by buildings and vegetation and which thus are favorable. In this way, the agents can adjust their way through the urban area with improved comfort.


## Graphical user interface

The graphical user interface will be continuously further developed and will not be available to the general public until further notice!

Complex meteorological models such as PALM (and thus PALM-4U) usually require fundamental knowledge of both the physical framework implemented in the model, and the technical-numerical implementation. Extensive experience is an essential prerequisite for the successful application of such models. PALM-4U, however, shall be suitable not only for scientists that have a strong background in boundary-layer meteorology, but also for staff of climate service companies; and even for administrative staff with a suitable training. In order to achieve this, both the model setup generation as well as the model steering require substantial simplification. Also, data handling and storage as well as visualization of model output obviously are important tasks in this context. Therefore, a user-friendly graphical user interface will be developed within the framework of the ​ MOSAIK-2 project .

  [​ MOSAIK-2 project](http://uc2-mosaik.org)

### Attachments (7)

- PALM-4U_logo.png ​ ( 438.9 KB ) - added by maronga 9 years ago . PALM-4U Logo
- PALM-4U_gui.png ​ ( 194.6 KB ) - added by maronga 9 years ago . PALM-4U GUI example image
- skizze_mosaik.odg ​ ( 471.9 KB ) - added by kanani 8 years ago .
- skizze_mosaik_plus_text.odg ​ ( 471.1 KB ) - added by kanani 8 years ago .
- skizze_mosaik_plus_text.pdf ​ ( 2.8 MB ) - added by kanani 8 years ago .
- skizze_mosaik.pdf ​ ( 240.2 KB ) - added by kanani 8 years ago .
- skizze_mosaik_plus_text.png ​ ( 442.8 KB ) - added by kanani 8 years ago .

### Download in other formats:

- Plain Text
Powered by Trac 1.0.5 By Edgewall Software .

  [Edgewall Software](http://www.edgewall.org/)
Legal Notice

  [Legal Notice](http://palm.muk.uni-hannover.de/trac/wiki/legalnotice)