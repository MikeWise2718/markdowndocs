---
title: "Open Street Map"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Open Street Map (OSM)  - main page: (https://www.openstreetmap.org/#map=6/51.337/10.459)
- Query Service - Overpass Turbo (https://overpass-turbo.eu/)

# Overpass API
- Explained here: https://wiki.openstreetmap.org/wiki/Overpass_API 
- Uses Overpass QL 
- Python API: (https://github.com/mocnik-science/osm-python-tools/blob/master/docs/overpass.md)

# Overpass Turbo
- Overpass turbo is a web based data mining toolf for OSM (https://overpass-turbo.eu/)
- Wiki page: (https://wiki.openstreetmap.org/wiki/Overpass_turbo)

- A query that output all the data in the current bounding box:
```
(
  node({{bbox}});
   <;
);
out meta;
```
- The bbox value can be found under `Export/Map/Current Map View`