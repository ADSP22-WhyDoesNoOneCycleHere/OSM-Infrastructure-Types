import overpass

api = overpass.API()


class Highway:

    def query_area(sw, ne, infra_type):
        s = ""
        for i in infra_type:
            s += "way" + i + "(" + sw + "," + ne + ");"
        return api.get(s, responseformat="json")

    def get_types(sw="52.526517, 13.407287", ne="52.538004, 13.440933", infra_type="track"):
        match infra_type:
            case "primary":
                return Highway.query_area(sw, ne, ["[highway = primary]"])
            case "secondary":
                return Highway.query_area(sw, ne, ["[highway = secondary]"])
            case "tertiary":
                return Highway.query_area(sw, ne, ["[highway = tertiary]"])
            case "unclassified":
                return Highway.query_area(sw, ne, ["[highway = unclassified]"])
            case "residential":
                return Highway.query_area(sw, ne, ["[highway = residential]"])
            case "residential_parking":
                return Highway.query_area(sw, ne, ["[highway = residential][~'^parking:.*$'~'.'][!cycleway]"])
            case "motorway_link":
                return Highway.query_area(sw, ne, ["[highway = motorway_link]"])
            case "trunk_link":
                return Highway.query_area(sw, ne, ["[highway = trunk_link]"])
            case "primary_link":
                return Highway.query_area(sw, ne, ["[highway = primary_link]"])
            case "secondary_link":
                return Highway.query_area(sw, ne, ["[highway = secondary_link]"])
            case "tertiary_link":
                return Highway.query_area(sw, ne, ["[highway = tertiary_link]"])
            case "living_street":
                return Highway.query_area(sw, ne, ["[highway = living_street]"])
            case "service":
                return Highway.query_area(sw, ne, ["[highway = service]"])
            case "pedestrian":
                return Highway.query_area(sw, ne, ["[highway = pedestrian]"])
            case "track":
                return Highway.query_area(sw, ne, ["[highway][cycleway=track]", "[highway]['cycleway:right'=track]"])
            case "highway_track":
                return Highway.query_area(sw, ne, ["[highway = track]"])
            case "bus_guideway":
                return Highway.query_area(sw, ne, ["[highway = bus_guideway]"])
            case "escape":
                return Highway.query_area(sw, ne, ["[highway = escape]"])
            case "road":
                return Highway.query_area(sw, ne, ["[highway = road]"])
            case "busway":
                return Highway.query_area(sw, ne, ["[highway = busway]"])
            case "footway":
                return Highway.query_area(sw, ne, ["[highway = footway]"])
            case "bridleway":
                return Highway.query_area(sw, ne, ["[highway = bridleway]"])
            case "corridor":
                return Highway.query_area(sw, ne, ["[highway = corridor]"])
            case "path":
                return Highway.query_area(sw, ne, ["[highway = path]"])
            case "sidewalk":
                return Highway.query_area(sw, ne, ["[footway = sidewalk]"])
            case "crossing":
                return Highway.query_area(sw, ne, ["[footway = crossing]"])
            case "cycleway":
                return Highway.query_area(sw, ne, ["[highway = cycleway]"])
            case "lane":
                return Highway.query_area(sw, ne, ["[cycleway = lane]",  "[highway]['cycleway:right'=lane]"])
            case "oppposite":
                return Highway.query_area(sw, ne, ["[cycleway = oppposite]"])
            case "opposite_lane":
                return Highway.query_area(sw, ne, ["[cycleway = opposite_lane]"])
            case "opposite_track":
                return Highway.query_area(sw, ne, ["[cycleway = opposite_track]"])
            case "share_busway":
                return Highway.query_area(sw, ne, ["[cycleway = share_busway]", "[highway]['cycleway:right'=share_busway]", "[highway]['cycleway:left'=share_busway]"])
            case "opposite_share_busway":
                return Highway.query_area(sw, ne, ["[cycleway = opposite_share_busway]"])
            case "shared_lane":
                return Highway.query_area(sw, ne, ["[cycleway = shared_lane]"])
            case "busway_lane":
                return Highway.query_area(sw, ne, ["[busway = lane]"])
            case _:
                return None