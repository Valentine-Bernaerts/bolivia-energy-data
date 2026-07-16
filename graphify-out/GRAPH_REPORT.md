# Graph Report - bolivia-energy-data  (2026-06-08)

## Corpus Check
- 9 files · ~56,404 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 160 nodes · 158 edges · 12 communities (9 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b9f34c05`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]

## God Nodes (most connected - your core abstractions)
1. `share_ned` - 4 edges
2. `share_ned` - 4 edges
3. `share_ned` - 4 edges
4. `share_ned` - 4 edges
5. `share_ned` - 4 edges
6. `Instructions pour Claude Code` - 3 edges
7. `re_share_primary` - 1 edges
8. `gwp_limit` - 1 edges
9. `import_capacity` - 1 edges
10. `solar_area_rooftop` - 1 edges

## Surprising Connections (you probably didn't know these)
- `Clustering_norte_Bolivia.ipynb` --writes--> `out: Clustering results`  [EXTRACTED]
   →   _Bridges community 6 → community 5_

## Import Cycles
- None detected.

## Communities (12 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (23): gwp_limit, import_capacity, re_share_primary, share_dispersion, share_freight_boat_max, share_freight_boat_min, share_freight_road_max, share_freight_road_min (+15 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (23): gwp_limit, import_capacity, re_share_primary, share_dispersion, share_freight_boat_max, share_freight_boat_min, share_freight_road_max, share_freight_road_min (+15 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (23): gwp_limit, import_capacity, re_share_primary, share_dispersion, share_freight_boat_max, share_freight_boat_min, share_freight_road_max, share_freight_road_min (+15 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (23): gwp_limit, import_capacity, re_share_primary, share_dispersion, share_freight_boat_max, share_freight_boat_min, share_freight_road_max, share_freight_road_min (+15 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (23): gwp_limit, import_capacity, re_share_primary, share_dispersion, share_freight_boat_max, share_freight_boat_min, share_freight_road_max, share_freight_road_min (+15 more)

### Community 5 - "Community 5"
Cohesion: 0.15
Nodes (18): analyse ramp.ipynb, Load curves (5 files × 21 municipalities), Reference tables (Layers, Tech, TS), Solar data (ninja_pv_*.csv × 21), Weather data (ninja_weather_*.csv × 21), Wind data (ninja_wind_*.csv × 21), demande.ipynb, exchanges.ipynb (+10 more)

### Community 6 - "Community 6"
Cohesion: 0.22
Nodes (11): Clustering_csv.ipynb, Clustering_norte_Bolivia.ipynb, Census data (INE), municipalities_database_Bolivia.csv, municipios_339_pob2012_ed.geojson, extraction.ipynb, GeoJSon_municipality_bolivia.py, municipality_count.ipynb (+3 more)

### Community 7 - "Community 7"
Cohesion: 0.50
Nodes (3): Gestion du contexte projet, Instructions pour Claude Code, Règles générales

## Knowledge Gaps
- **114 isolated node(s):** `re_share_primary`, `gwp_limit`, `import_capacity`, `solar_area_rooftop`, `solar_area_ground` (+109 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `re_share_primary`, `gwp_limit`, `import_capacity` to the rest of the system?**
  _114 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._