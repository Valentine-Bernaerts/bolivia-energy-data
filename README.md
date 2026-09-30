# Content

This repository builds the input data of the EnergyScope model of the Norte Amazónica region of the Bolivian Amazon: 21 municipalities of Pando, northern Beni and Ixiamas (La Paz), grouped into five clusters, C1 to C5. From the 2001, 2012 and 2024 censuses, the AETN 2024 electricity sales, RAMP load profiles, Renewables.ninja weather data and a GIS analysis of the medium-voltage network, it produces for each cluster the demand, technology, resource, time-series and exchange files that EnergyScope reads. It covers the 2025 scenarios (sufficiency, reality, reality_access) and the 2035 and 2050 projections (no_transition, late_access, early_access, early_access_brazil).

The model itself lives in the companion repository https://github.com/Valentine-Bernaerts/EnergyScope_BO_nord_amazonia. The chain is:

- RAMP (https://github.com/Valentine-Bernaerts/RAMP_Bolivia) simulates the minute-level load curves of each municipality. They are not committed here, see Prerequisites.
- This repository turns census, AETN, RAMP and GIS data into per-cluster EnergyScope inputs, written to the `output_energyscope*/` folders of `analyse data ramp/`.
- For 2025, these outputs are copied by hand into `EnergyScope_BO_nord_amazonia/Data/2025/`. For 2035 and 2050, a few notebooks write directly into `EnergyScope_BO_nord_amazonia/Data/` and `case_studies/` (see Warnings).
- EnergyScope solves the scenarios. `analyse data ramp/2050/cost_reconstruction.ipynb` reads the solved results back, and the analysis notebooks of the EnergyScope repository read some files of this one.

The `Data/2025/README.md` file of the EnergyScope repository documents which columns of its catalogue come from which notebook here, and which were maintained by hand.

This work supports the master's thesis "Energy Transition Pathways for Isolated Regions in the Global South: A Case Study of Bolivia's Northern Amazon", Master of Science in Energy Engineering, University of Liège, academic year 2025-2026.

Description of the repository:

- ./renewable ninja/ : Renewables.ninja weather, solar and wind data per municipality, and the notebooks that aggregate them.
- ./exctraction of data/ : INE census tables, AETN 2024 electricity sales, and the notebooks that extract them.
- ./Clustering/ : construction of the five clusters.
- ./projections/ : population, households, access trajectories and Source A demand projected to 2035 and 2050.
- ./analyse_GIS_projections/ : distance of each community to the MV network, and classification of communities into grid-connectable and dispersed (standalone solar) at each horizon.
- ./analyse data ramp/ : the EnergyScope input files, one folder per scenario (`sufficiency`, `reality`, `reality_access`) or horizon (`2035`, `2050`). `data/` holds the shared templates (`Layers_in_out.csv`, `Technologies.csv`, `Time_series.csv`).
- ./analyse_acces_demande/ : figures of household access and end-use demand.
- ./GeoJSon/ : municipal boundaries.
- ./LICENSE : license file
- ./README.md : this file

The notebooks display their figures inline and do not save them.

# License:

Copyright 2026 Valentine Bernaerts

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

The census, AETN, INE, Renewables.ninja and GIS source data keep the terms of their respective publishers.

# Prerequisites

1. Python. The notebooks were run with three environments:

- most notebooks: Python 3.10 with numpy 2.2, pandas 2.3, scipy 1.15, matplotlib 3.10, openpyxl 3.1, geopandas 1.1, shapely 2.1, scikit-learn 1.7, nbformat 5.10;
- `Clustering/Clustering_norte_Bolivia.ipynb` and `analyse_acces_demande/analyse_acces_demande.ipynb`: Python 3.13 with, in addition, geopy 2.4, kmedoids 0.5 and seaborn 0.13;
- the notebooks that call the EnergyScope package (`esmc`) and `analyse data ramp/2050/cost_reconstruction.ipynb`: the `energyscope` environment of the EnergyScope repository, see its `environment.yml`.

2. The EnergyScope repository, cloned next to this one as `EnergyScope_BO_nord_amazonia/`. Several notebooks read its `Data/2025/` catalogue through relative paths (`../../../EnergyScope_BO_nord_amazonia/`), and some write into it.

3. The RAMP load curves. The files `load_curve_energy_service_full_year_Norte_Amazonia.csv` and `load_curve_energy_service_full_year_Norte_Amazonia_reality.csv`, one per municipality, exceed GitHub's size limit and are excluded by `.gitignore`. They are produced by the RAMP_Bolivia repository and must be placed in `analyse data ramp/<scenario>/data ramp/<municipality>/`: the sufficiency run in `sufficiency/data ramp/`, the reality run in `reality/`, `2035/` and `2050/data ramp/`. `exctraction of data/source_A_grid_consumption.ipynb` also reads `RAMP_Bolivia/data/thermal_comfort_lookup.csv`, so RAMP_Bolivia must be cloned next to this repository.

# Execution order

Each notebook runs from its own folder. They are listed in the order in which they depend on each other. "Reads" gives the inputs produced elsewhere in the chain; "writes" gives the files it produces.

1. `renewable ninja/temperature/temp.ipynb` - reads the hourly weather files in `data/`; writes the seasonal temperatures, the fan-use lookup (`thermal_comfort_lookup.csv`) and the hot-water power profiles in `output/`.
2. `renewable ninja/solar and wind/extraction_solar_wind.ipynb` - reads the PV and wind files; writes `output/renewables_C{k}.csv` (PV, SOLAR, WIND_ONSHORE per cluster).
3. `exctraction of data/extraction.ipynb` - reads the INE census tables in `data/`; writes `output/CSV_final.csv` and `output/CSV_final_in_excel.xlsx`, the census base used by almost every later notebook.
4. `exctraction of data/municipality_count.ipynb` - reads `CSV_final.csv` and `data/northern_amazon_education_health.csv`; writes `output/municipalities_counts*.csv`, the number of schools, health centres, shops and other RAMP users per municipality.
5. `exctraction of data/source_A_grid_consumption.ipynb` - reads the AETN 2024 sales, `CSV_final.csv` and `RAMP_Bolivia/data/thermal_comfort_lookup.csv`; writes `output/source_A_grid_consumption_by_municipality.csv` and `output/source_A_all_sectors_end_uses.csv` (grid demand, Source A, by sector and end use).
6. `Clustering/Clustering_csv.ipynb` - reads `CSV_final.csv`, `municipalities_counts.csv`, `municipality_temperatures.csv` and `data/municipalities_database_Bolivia.csv`; writes `output/Clustering.csv`.
7. `Clustering/Clustering_norte_Bolivia.ipynb` - reads `Clustering.csv` and the GeoJSON; writes `output/clustering_results.csv` and `output/optimal_clusters_metrics.csv`.
8. `projections/01_base_municipale.ipynb` - reads `CSV_final.csv`; checks the municipal base, writes nothing.
9. `projections/02_population_2035_2050.ipynb` - reads `CSV_final.csv`, the INE projections in `data_ine/` and `clustering_results.csv`; writes `output/menages_projetes.csv` and `output/backtest_clusters_2024.csv`.
10. `analyse data ramp/sufficiency/time_series.ipynb` - reads the sufficiency RAMP curves, `renewables_C{k}.csv` and `../data/Time_series.csv`; writes `output_energyscope/C{k}/Time_series.csv`.
11. `analyse_GIS_projections/gis_analysis.ipynb` - reads the community, generation and MV-line layers in `data/` and `municipalities_counts.csv`; writes `output/task1_community_distances_lines.csv`, `output/task3_cluster_band*.csv` and `output/task4_generation_inventory.csv`.
12. `analyse_GIS_projections/share_dispersion.ipynb` - reads `CSV_final.csv`, the sufficiency RAMP curves, the sufficiency `Time_series.csv`, `task1_community_distances_lines.csv`, `menages_projetes.csv` and the GIS layers; writes `output/<year>/cluster_summary.csv`, `output/<year>/community_detail.csv`, `output/community_breakeven_detail_BC.csv` and `output/share_dispersion_final_BC.csv`.
13. `projections/03_split_abc_projete.ipynb` - reads the GIS outputs, `CSV_final.csv` and `menages_projetes.csv`; writes `output/split_abc_projete.csv` (households on the grid, off-grid and without access, per trajectory and horizon).
14. `projections/04_source_A_taux_possession.ipynb` - reads `CSV_final.csv` and `split_abc_projete.csv`; writes `output/taux_possession_projetes.csv`.
15. `projections/05_source_A_demande_projetee.ipynb` - re-executes the code cells of `source_A_grid_consumption.ipynb`, then reads `split_abc_projete.csv` and `taux_possession_projetes.csv`; writes `output/demande_source_A_projetee.csv` and `output/c1_avail_exterior.csv`.
16. `projections/06_household_years_acces.ipynb` - reads `split_abc_projete.csv`; writes `output/household_years_acces.csv`.
17. `analyse data ramp/sufficiency/`: `demande.ipynb` (RAMP curves, cooking households) writes `Demands.csv`; `exchanges.ipynb` writes `Dist.csv` and `Network_exchanges.csv`; `misc_json.ipynb` (`CSV_final.csv`) writes `Misc.json`; `resources.ipynb` (`CSV_final_in_excel.xlsx`) writes `Resources.csv`; `technologies.ipynb` (`../data/Technologies.csv`, `CSV_final.csv`, the GIS outputs) writes `Technologies.csv`, all in `output_energyscope/`. `analyse ramp.ipynb` plots the RAMP profiles and writes nothing.
18. `analyse data ramp/reality/`: `time_series.ipynb` (reality RAMP curves) writes `Time_series.csv`; `home_systems.ipynb` (`CSV_final.csv`, Source A, `data ramp/ramp_reality_annual_summary.csv`) writes `source_B_home_systems_reality.csv`; `demande.ipynb` (Source A, `CSV_final.csv`, RAMP reality summary) writes `Demands.csv`; `technologies.ipynb` (sufficiency `Technologies.csv`, `source_B_home_systems_reality.csv`, reality `Time_series.csv`) writes `Technologies.csv`, all in `output_energyscope/`.
19. `analyse data ramp/reality_access/`: `demande_access.ipynb` (reality `Demands.csv`, sufficiency RAMP curves, `CSV_final.csv`, Source A) writes `Demands.csv` and `demands_access_by_provenance.csv`; `time_series_access.ipynb` (runs `demande_access.ipynb`, reads the reality and sufficiency `Time_series.csv`) writes `Time_series.csv`; `technologies.ipynb` (reality `Technologies.csv`, GIS outputs) writes `Technologies.csv`.
20. `analyse data ramp/2035/` and `analyse data ramp/2050/`, same order in both: `demande.ipynb` (`demande_source_A_projetee.csv`, `split_abc_projete.csv`, `menages_projetes.csv`, sufficiency RAMP curves) writes `output_energyscope_<year>/{no_transition_late_access,early_access}/C{k}/Demands.csv`; `home_systems.ipynb` writes a diagnostic `source_B_home_systems_diagnostic.csv`; `time_series.ipynb` writes `output_energyscope_<year>/C{k}/Time_series.csv`; then `technologies.ipynb`, which writes `Technologies.csv` in `output_energyscope_<year>/` and into EnergyScope (see Warnings). In 2050 it also writes `output_energyscope_2050/vintage_registry.csv`.
21. `analyse data ramp/2050/`, after the 2050 solves: `resources.ipynb`, `share_dispersion.ipynb`, `share_dispersion_recal2.ipynb`, `share_dispersion_brazil.ipynb`, `early_access_brazil_import.ipynb` (all write into EnergyScope, see Warnings), and `cost_reconstruction.ipynb`, which reads the solved case studies and `vintage_registry.csv`, and writes `output_energyscope_2050/cost_reconstruction_table.csv`.
22. `analyse_acces_demande/analyse_acces_demande.ipynb` - reads `CSV_final.csv` and `EnergyScope_BO_nord_amazonia/Data/2025/{sufficiency,reality}/C*/Demands.csv`; plots access by municipality and demand by end use.

# Warnings

**Notebooks that write into EnergyScope. Do not re-run them.** These seven notebooks deploy files into `EnergyScope_BO_nord_amazonia/Data/2035/`, `Data/2050/` and `case_studies/C1_C2_C3_C4_C5/`. Running one is a deployment, not a dry run: it overwrites the catalogue that produced the published results.

- `analyse data ramp/2035/technologies.ipynb` : `Data/2035/*/` (`Technologies.csv`, `Layers_in_out.csv`, `02_REF_REGION/Technologies.csv`, `Misc.json`).
- `analyse data ramp/2050/technologies.ipynb` : `Data/2050/*/` and the `reg_*.dat` files of the 2050 case studies.
- `analyse data ramp/2050/resources.ipynb` : `Data/2050/*/C{k}/Resources.csv` and `reg_*.dat`.
- `analyse data ramp/2050/share_dispersion.ipynb`, `share_dispersion_recal2.ipynb`, `share_dispersion_brazil.ipynb` : `Data/2050/*/C{k}/Misc.json` and `reg_*.dat`.
- `analyse data ramp/2050/early_access_brazil_import.ipynb` : `Data/2050/early_access_brazil/{C3,C5}/Resources.csv` and `reg_*.dat`.

Their stored outputs are those of their last run and are left as they are.

**The `share_dispersion` values computed in these notebooks are out of date.** The published values in `EnergyScope_BO_nord_amazonia/Data/**/Misc.json` were calibrated by `scripts/calibrate_share_dispersion.py` in the EnergyScope repository, which documents why that calibration cannot be repeated. Re-running the 2050 notebooks would replace them with values 5 to 10 times larger, because they still use the dispersed-demand targets of the superseded classification (C1 2.079, C2 0.132, C3 0.648, C4 1.543 GWh/y). The calibration section of `2035/technologies.ipynb` reproduces the published 2035 values only to within 1.5 %.

**Four notebooks whose published CSVs are authoritative.** The CSVs written by these notebooks were fixed by hand, and that version produced the results of the thesis. The notebook code evolved afterwards, so running them today gives different files. They are not to be re-run, and each carries a note at its top saying so.

- `analyse data ramp/reality/technologies.ipynb` : `output_energyscope/C{k}/Technologies.csv`.
- `analyse data ramp/reality/time_series.ipynb` : `output_energyscope/C{k}/Time_series.csv`.
- `analyse data ramp/reality_access/time_series_access.ipynb` : `output_energyscope/C{k}/Time_series.csv`.
- `exctraction of data/municipality_count.ipynb` : `output/municipalities_counts*`.

This is the same situation as the one documented in `Data/2025/README.md` of the EnergyScope repository.

# Previous versions and Authors:

- EnergyScope Multi-Cell model of Bolivia's Northern Amazon, companion repository: https://github.com/Valentine-Bernaerts/EnergyScope_BO_nord_amazonia
- RAMP load profiles for Bolivia: https://github.com/Valentine-Bernaerts/RAMP_Bolivia

Author:

- Valentine Bernaerts, University of Liège (Belgium)
