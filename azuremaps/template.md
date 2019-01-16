---
title: "Azure Maps"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- The other Microsoft Map service...


# Activating
- Home page <https://azure.microsoft.com/en-gb/services/azure-maps/>
- Not in portal by default, Found it in portal by searching in the Azure Mar
- There are currently two pricing levels, took the basic to ty out

# API
- Docs <https://docs.microsoft.com/en-gb/azure/azure-maps/>
- Using with postman: <https://docs.microsoft.com/en-gb/azure/azure-maps/how-to-search-for-address>
- Map Tiles: <https://docs.microsoft.com/en-us/rest/api/maps/render/getmaptile>


# Bing comparison:

## REST API
- Here: <https://docs.microsoft.com/en-us/bingmaps/rest-services/>
- Bing Maps Tile System: <https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system>
- Detailed article: <https://onedrive.live.com/view.aspx?resid=D35222484A76A01!367734&ithint=file%2cdocx&app=Word&authkey=!AG_vTkAxtCXFaNk>

## Misc Links
- Interesting notification: <https://social.msdn.microsoft.com/Forums/en-US/618e5f6c-7222-446f-b738-7f57a2e2b592/new-url-templates-for-bing-maps-tiles?forum=bingmapsservices>
- Slippy Maps: <https://build-failed.blogspot.com/2015/03/improve-tile-loading-at-browser.html>
- Pedro: <https://build-failed.blogspot.com/2015/03/improve-tile-loading-at-browser.html>
- Caching Tiles: <https://gis.stackexchange.com/questions/65618/cache-tiles-for-offline-use-of-google-bing-aerial-maps/114343>

- Bing Maps: <https://stackoverflow.com/questions/20005856/bing-map-ajaxtileusage-and-loadstandardmap>


## Docs
- Get a static map <https://docs.microsoft.com/en-us/bingmaps/rest-services/imagery/get-a-static-map>

# So far
- Online Map code
```
            new OnlineMapsProvider("azuremaps", "Azure Maps")
            {
                hasLanguage = true,
                _types = new []
                {
                    new MapType("Aerial")
                    {
                        //string key = "IdbTbLfVZWE6B5pnqB-ybmzk5KbM_lyQeLtt_YusYNc";
                        // See https://docs.microsoft.com/en-us/rest/api/maps/render/getmaptile;

                        //urlWithoutLabels = "https://t{rnd0-4}.ssl.ak.tiles.virtualearth.net/tiles/a{quad}.jpeg?mkt={lng}&g=1457&n=z",
                        //urlWithLabels = "https://t{rnd0-4}.ssl.ak.dynamic.tiles.virtualearth.net/comp/ch/{quad}?mkt={lng}&it=A,G,L,LA&og=30&n=z"
                        urlWithoutLabels = "https://atlas.microsoft.com/map/tile/basic?subscription-key=IdbTbLfVZWE6B5pnqB-ybmzk5KbM_lyQeLtt_YusYNc&api-version=1.0&layer=basic&style=main&zoom={zoom}&x={x}&y={y}",
                        urlWithLabels = "https://atlas.microsoft.com/map/tile/basic?subscription-key=IdbTbLfVZWE6B5pnqB-ybmzk5KbM_lyQeLtt_YusYNc&api-version=1.0&layer=basic&style=main&zoom={zoom}&x={x}&y={y}"
                     },
                    new MapType("Road")
                    {
                        urlWithLabels = "https://atlas.microsoft.com/map/tile/basic?subscription-key=IdbTbLfVZWE6B5pnqB-ybmzk5KbM_lyQeLtt_YusYNc&api-version=1.0&layer=basic&style=main&zoom={zoom}&x={x}&y={y}"
                        //urlWithLabels = "https://t{rnd0-4}.ssl.ak.dynamic.tiles.virtualearth.net/comp/ch/{quad}?mkt={lng}&it=G,VE,BX,L,LA&og=30&n=z"
                    }
                }
            },
 ```
