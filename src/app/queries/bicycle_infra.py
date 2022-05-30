

class Cycleway:

    default_out = "[out:json];"
    out = ";out;"

    default_sw = "44.490204027212016, 11.269648275756735"
    default_ne = "44.520311680337684, 11.433445623245943"

    # This might not work as intended, if there is overlap -> Maybe put most specific types first??
    def get_types(sw, ne, infra_type):
        match infra_type:
            case "lane":
                Cycleway.query_area("[cycleway = lane]")
            case "right_lane":
                Cycleway.query_area("[highway]['cycleway:right'=lane]")
            case "both_lane":
                Cycleway.query_area("[cycleway = both_lane]")
            case "oppposite":
                Cycleway.query_area("[cycleway = oppposite]")
            case "opposite_lane":
                Cycleway.query_area("[cycleway = opposite_lane]")
            case "track":
                Cycleway.query_area("[cycleway = track]")
            case "right_track":
                Cycleway.query_area("[highway]['cycleway:right'=track]")
            case "opposite_track":
                Cycleway.query_area("[cycleway = opposite_track]")
            case "share_busway":
                Cycleway.query_area("[cycleway = share_busway]")
            case "share_busway_right":
                Cycleway.query_area("[highway]['cycleway:right'=share_busway]")
            case "share_busway_left":
                Cycleway.query_area("[highway]['cycleway:left'=share_busway]")
            case "opposite_share_busway":
                Cycleway.query_area("[cycleway = opposite_share_busway]")
            case "shared_lane":
                Cycleway.query_area("[cycleway = shared_lane]")
            case "shared_residential_parking":
                Cycleway.query_area("[highway=residential][bicycle!=no][~'^parking:.*$'~'.'][!cycleway]")
            case "shared_lane_residential":
                Cycleway.query_area("[highway=residential][bicycle!=no][!cycleway]")
            case "busway":
                Cycleway.query_area("[highway = busway]")
            case "cycleway":
                Cycleway.query_area("[highway = cycleway]")
            case _:
                return { "message": "Wrong infrastructure type!" }

    def query_area(sw, ne, infra_type):
        return "[out:json]; way(" + sw + "," + ne + ")"
                
    # Might be a bit to general
    def cycleway(way):
        return way["highway"] == "cycleway"

    def lane(way):
        if "cycleway" in way:
            return way["cycleway"] == "lane"

    def right_lane(way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "lane"

    def both_lane(way):
        if "cycleway:both" in way:
            return way["cycleway:both"] == "lane"

    def opposite(way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite"

    def opposite_lane(way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_lane"

    def track(way):
        if "cycleway" in way:
            return way["cycleway"] == "track"

    # Distinction with track might be unnecessary
    def right_track(way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "track"

    def opposite_track(way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_track"

    def share_busway(way):
        if "cycleway" in way:
            return way["cycleway"] == "share_busway"

    def share_busway_right(way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "share_busway"

    def share_busway_left(way):
        if "cycleway:left" in way:
            return way["cycleway:left"] == "share_busway"

    def opposite_share_busway(way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_share_busway"
        elif "cycleway:opposite" in way:
            return way["cycleway:opposite"] == "share_busway"

    def shared_lane(way):
        if "cycleway" in way:
            return way["cycleway"] == "shared_lane"

    # Residential streets that do not specifically disallow bikes and therefore have shared lanes
    def shared_lane_residential(way):
        if "highway" in way and "bicycle" in way:
            return way["highway"] == "residential" and way["bicycle"] != "no" and "cycleway" not in way
        # Disallowing cycleways might be unnecessary

        if "highway" in way:
            return way["highway"] == "residential" and "cycleway" not in way

    # Residential streets like above, but with possibility for parking (there might be overlap between the two!)
    def shared_residential_parking(way):
        parking = {True for k, v in way.items() if k.startswith('parking')}  # TODO: Check for this

        if "highway" in way and "bicycle" in way:
            return way["highway"] == "residential" and way["bicycle"] != "no" and "cycleway" not in way and parking

        if "highway" in way:
            return way["highway"] == "residential" and "cycleway" not in way and parking

        """
        return_s = Cycleway.query_area(, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway=residential][bicycle!=no][~'^parking:.*$'~'.'][!cycleway]"

        return return_s + Cycleway.out
        """

    # Busway
    def busway(way):
        if "busway" in way:
            return way["busway"] == "lane"
