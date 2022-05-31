import overpass

api = overpass.API()

class Highway:

    def query_area(sw, ne, infra_type):
        return api.get("way" + infra_type + "(" + sw + "," + ne + ")", responseformat="json")

    def get_types(sw="44.490204027212016, 11.269648275756735", ne="44.520311680337684, 11.433445623245943", infra_type="cycleway"):
        match infra_type:
            case "motorway":
                return Highway.query_area(sw, ne, "[highway = motorway]")
            case "trunk":
                return Highway.query_area(sw, ne, "[highway = trunk]")
            case "primary":
                return Highway.query_area(sw, ne, "[highway = primary]")
            case "secondary":
                return Highway.query_area(sw, ne, "[highway = secondary]")
            case "tertiary":
                return Highway.query_area(sw, ne, "[highway = tertiary]")
            case "unclassified":
                return Highway.query_area(sw, ne, "[highway = unclassified]")
            case "residential":
                return Highway.query_area(sw, ne, "[highway = residential]")
            case "motorway_link":
                return Highway.query_area(sw, ne, "[highway = motorway_link]")
            case "trunk_link":
                return Highway.query_area(sw, ne, "[highway = trunk_link]")
            case "primary_link":
                return Highway.query_area(sw, ne, "[highway = primary_link]")
            case "secondary_link":
                return Highway.query_area(sw, ne, "[highway = secondary_link]")
            case "tertiary_link":
                return Highway.query_area(sw, ne, "[highway = tertiary_link]")
            case "living_street":
                return Highway.query_area(sw, ne, "[highway = living_street]")
            case "service":
                return Highway.query_area(sw, ne, "[highway = service]")
            case "pedestrian":
                return Highway.query_area(sw, ne, "[highway = pedestrian]")
            case "track":
                return Highway.query_area(sw, ne, "[highway = track]")
            case "bus_guideway":
                return Highway.query_area(sw, ne, "[highway = bus_guideway]")
            case "escape":
                return Highway.query_area(sw, ne, "[highway = escape]")
            case "raceway":
                return Highway.query_area(sw, ne, "[highway = raceway]")
            case "road":
                return Highway.query_area(sw, ne, "[highway = road]")
            case "busway":
                return Highway.query_area(sw, ne, "[highway = busway]")
            case "footway":
                return Highway.query_area(sw, ne, "[highway = footway]")
            case "bridleway":
                return Highway.query_area(sw, ne, "[highway = bridleway]")
            case "steps":
                return Highway.query_area(sw, ne, "[highway = steps]")
            case "corridor":
                return Highway.query_area(sw, ne, "[highway = corridor]")
            case "path":
                return Highway.query_area(sw, ne, "[highway = path]")
            case "sidewalk":
                return Highway.query_area(sw, ne, "[footway = sidewalk]")
            case "crossing":
                return Highway.query_area(sw, ne, "[footway = crossing]")
            case "cycleway":
                return Highway.query_area(sw, ne, "[highway = cycleway]")
            case "lane":
                return Highway.query_area(sw, ne, "[cycleway = lane]")
            case "oppposite":
                return Highway.query_area(sw, ne, "[cycleway = oppposite]")
            case "opposite_lane":
                return Highway.query_area(sw, ne, "[cycleway = opposite_lane]")
            case "track":
                return Highway.query_area(sw, ne, "[cycleway = track]")
            case "opposite_track":
                return Highway.query_area(sw, ne, "[cycleway = opposite_track]")
            case "share_busway":
                return Highway.query_area(sw, ne, "[cycleway = share_busway]")
            case "opposite_share_busway":
                return Highway.query_area(sw, ne, "[cycleway = opposite_share_busway]")
            case "shared_lane":
                return Highway.query_area(sw, ne, "[cycleway = shared_lane]")
            case "busway_lane":
                return Highway.query_area(sw, ne, "[busway = lane]")
            case "proposed":
                return Highway.query_area(sw, ne, "[highway = proposed]")
            case "construction":
                return Highway.query_area(sw, ne, "[highway = construction]")
            case _:
                return None
