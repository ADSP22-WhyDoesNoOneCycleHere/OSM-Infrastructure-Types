import overpass

api = overpass.API()

highway = [
            "[highway = trunk]",
            "[highway = primary]",
            "[highway = secondary]",
            "[highway = tertiary]",
            "[highway = unclassified]",
            "[highway = residential]",
            "[highway = residential][~'^parking:.*$'~'.'][!cycleway]",
            "[highway = motorway_link]",
            "[highway = trunk_link]",
            "[highway = primary_link]",
            "[highway = secondary_link]",
            "[highway = tertiary_link]",
            "[highway = living_street]",
            "[highway = service]",
            "[highway = pedestrian]",
            "[highway = track]",
            "[highway = bus_guideway]",
            "[highway = escape]",
            "[highway = road]",
            "[highway = busway]",
            "[highway = footway][bicycle = yes]", "[highway = footway][bicycle = no]", "[highway = footway]",
            "[highway = bridleway]",
            "[highway = steps]",
            "[highway = corridor]",
            "[highway = path]",
            "[footway = sidewalk][bicycle = yes]", "[footway = sidewalk][bicycle = no]", "[footway = sidewalk]",
            "[footway = crossing][bicycle = yes]", "[footway = crossing][bicycle = no]", "[footway = crossing]",
            "[highway = cycleway]",
            [ "[cycleway = lane]", "['cycleway:left' = lane]", "['cycleway:right' = lane]", "['cycleway:both' = lane]" ],
            [ "[cycleway = oppposite]", "['cycleway:left' = oppposite]", "['cycleway:right' = oppposite]", "['cycleway:both' = oppposite]" ],
            [ "[cycleway = opposite_lane]", "['cycleway:left' = opposite_lane]", "['cycleway:right' = opposite_lane]", "['cycleway:both' = opposite_lane]" ],
            [ "[cycleway = track]", "['cycleway:left' = track]", "['cycleway:right' = track]", "['cycleway:both' = track]" ],
            [ "[cycleway = opposite_track]", "['cycleway:left' = opposite_track]", "['cycleway:right' = opposite_track]", "['cycleway:both' = opposite_track]" ],
            [ "[cycleway = share_busway]", "['cycleway:left' = share_busway]", "['cycleway:right' = share_busway]", "['cycleway:both' = share_busway]" ],
            [ "[cycleway = opposite_share_busway]", "['cycleway:left' = opposite_share_busway]", "['cycleway:right' = opposite_share_busway]", "['cycleway:both' = opposite_share_busway]" ],
            [ "[cycleway = shared_lane]", "['cycleway:left' = shared_lane]", "['cycleway:right' = shared_lane]", "['cycleway:both' = shared_lane]" ],
            "[busway = lane]",
            "[highway = construction]"
        ]

class Highway:

    def query_area(sw = "52.51326008267224, 13.322514165234397", ne = "52.51681153023918, 13.335043884715132"):
        elements = { "features": [ ] }
        for infra_types in highway:
            if isinstance(infra_types, list):
                for infra_type in infra_types:
                    res = api.get("way" + infra_type + "(" + sw + "," + ne + ")", responseformat="json")
                    elements["features"].append( { infra_type: res["elements"] } )
            else:
                res = api.get("way" + infra_types + "(" + sw + "," + ne + ")", responseformat="json")
                elements["features"].append( { infra_types: res["elements"] } )
        return elements
