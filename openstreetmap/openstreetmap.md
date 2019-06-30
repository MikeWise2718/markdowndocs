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


# Python Overpass API
- Overview and Installation Page: (https://python-overpy.readthedocs.io/en/latest/introduction.html)


## Setup and Test
- conda create -n overpass python=3
- pip install overpy
- cd d:\transfer\overpy
- python testoverpy.py
testoverpy.py:
```
import overpy

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    way(50.746,7.154,50.748,7.157) ["highway"];
    (._;>;);
    out body;
    """)

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
```
output:
```
Name: Rhedenstraße
  Highway: residential
  Nodes:
    Lat: 50.746874, Lon: 7.156307
    Lat: 50.746598, Lon: 7.156237
    Lat: 50.746477, Lon: 7.156199
    Lat: 50.746360, Lon: 7.156124
    Lat: 50.746263, Lon: 7.156023
    Lat: 50.746194, Lon: 7.155926
    Lat: 50.746139, Lon: 7.155843
Name: Von-Ketteler-Straße
  Highway: residential
  Nodes:
    Lat: 50.746905, Lon: 7.155786
    Lat: 50.747222, Lon: 7.155621
Name: Mutter-Barat-Straße
  Highway: residential
  Nodes:
    Lat: 50.747989, Lon: 7.156302
    Lat: 50.747934, Lon: 7.156229
    Lat: 50.747695, Lon: 7.155421
    Lat: 50.747605, Lon: 7.155159
    Lat: 50.747241, Lon: 7.154310
    Lat: 50.746939, Lon: 7.153634
Name: Stegerwaldstraße
  Highway: residential
  Nodes:
    Lat: 50.747853, Lon: 7.153685
    Lat: 50.747666, Lon: 7.154022
    Lat: 50.747673, Lon: 7.154122
    Lat: 50.747939, Lon: 7.154603
    Lat: 50.748182, Lon: 7.155178
    Lat: 50.748318, Lon: 7.155590
    Lat: 50.748362, Lon: 7.155646
Name: Alte Schulstraße
  Highway: residential
  Nodes:
    Lat: 50.747537, Lon: 7.158000
    Lat: 50.747544, Lon: 7.157841
    Lat: 50.747554, Lon: 7.157667
    Lat: 50.747582, Lon: 7.157470
    Lat: 50.747620, Lon: 7.157314
    Lat: 50.747672, Lon: 7.157152
    Lat: 50.747732, Lon: 7.157026
    Lat: 50.747882, Lon: 7.156751
    Lat: 50.748061, Lon: 7.156421
    Lat: 50.748213, Lon: 7.156179
    Lat: 50.748263, Lon: 7.156042
    Lat: 50.748429, Lon: 7.155750
    Lat: 50.748831, Lon: 7.155019
    Lat: 50.749089, Lon: 7.154576
    Lat: 50.749207, Lon: 7.154365
    Lat: 50.749501, Lon: 7.153915
    Lat: 50.749608, Lon: 7.153750
    Lat: 50.749800, Lon: 7.153468
    Lat: 50.749847, Lon: 7.153398
    Lat: 50.750132, Lon: 7.152963
    Lat: 50.750224, Lon: 7.152842
Name: n/a
  Highway: service
  Nodes:
    Lat: 50.746079, Lon: 7.154944
    Lat: 50.745963, Lon: 7.154580
    Lat: 50.745662, Lon: 7.154815
    Lat: 50.745788, Lon: 7.155202
Name: Mutter-Barat-Straße
  Highway: footway
  Nodes:
    Lat: 50.748061, Lon: 7.156421
    Lat: 50.747989, Lon: 7.156302
Name: Von-Ketteler-Straße
  Highway: residential
  Nodes:
    Lat: 50.747335, Lon: 7.152963
    Lat: 50.746992, Lon: 7.153544
    Lat: 50.746939, Lon: 7.153634
    Lat: 50.746733, Lon: 7.154001
    Lat: 50.746657, Lon: 7.154135
    Lat: 50.746585, Lon: 7.154273
    Lat: 50.746562, Lon: 7.154380
    Lat: 50.746560, Lon: 7.154508
    Lat: 50.746581, Lon: 7.154655
    Lat: 50.746868, Lon: 7.155638
    Lat: 50.746905, Lon: 7.155786
    Lat: 50.746912, Lon: 7.155892
    Lat: 50.746902, Lon: 7.156003
    Lat: 50.746874, Lon: 7.156307
    Lat: 50.746809, Lon: 7.156921
    Lat: 50.746751, Lon: 7.157490
Name: Von-Ketteler-Straße
  Highway: service
  Nodes:
    Lat: 50.746562, Lon: 7.154380
    Lat: 50.746165, Lon: 7.154428
    Lat: 50.745963, Lon: 7.154580
    Lat: 50.745895, Lon: 7.154570
    Lat: 50.745810, Lon: 7.154439
Name: n/a
  Highway: footway
  Nodes:
    Lat: 50.746733, Lon: 7.154001
    Lat: 50.746488, Lon: 7.153662
```
