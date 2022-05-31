# OSM-Infrastructure-Types

This service provides data about OpenStreetMaps infrastructure types for specified routes and areas.

## Startup

 `docker-compose up`

 ## API

 ### GET /

 - for testing purposes

 ### POST /area

#### Returns:

- OSM JSON

#### Request Body:

sw: str

- south-west coordinate of area

ne: str

- north-west coordinate of area

infra_type: str

- infrastructure type of way of area

## Resources

### Overpass API (Python wrapper)

https://github.com/gappleto97/overpassify

https://github.com/mvexel/overpass-api-python-wrapper

https://python-overpy.readthedocs.io/en/latest/introduction.html

https://mateuszwiza.medium.com/how-to-count-the-number-of-buildings-in-an-area-by-category-using-openstreetmap-api-7163d77289e9

### Overpass QL

https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL

https://osm-queries.ldodds.com/tutorial/index.html
