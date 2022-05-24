

class Cycleway:

    default_out = "[out:json];"
    out = ";out;"

    default_sw = "44.490204027212016, 11.269648275756735"
    default_ne = "44.520311680337684, 11.433445623245943"

    def query_area(self, sw, ne):
        # could also be changed to use node rather than "way" if not only nodes are relevant
        return "[out:json]; way(" + sw + "," + ne + ")"

    # This might not work as intended, if there is overlap -> Maybe put most specific types first??
    def get_types(self, way):
        if self.lane(way):
            return "Lane"
        elif self.right_lane(way):
            return "Right Lane"
        elif self.both_lane(way):
            return "Both Lane"
        elif self.opposite(way):
            return "Opposite"
        elif self.opposite_lane(way):
            return "Opposite Lane"
        elif self.track(way):
            return "Track"
        elif self.right_track(way):
            return "Right Track"
        elif self.opposite_track(way):
            return "Opposite Track"
        elif self.share_busway(way):
            return "Share Busway"
        elif self.share_busway_right(way):
            return "Share Busway Right"
        elif self.share_busway_left(way):
            return "Share Busway Left"
        elif self.opposite_share_busway(way):
            return "Opposite Share Busway"
        elif self.shared_lane(way):
            return "Shared Lane"
        elif self.shared_residential_parking(way):
            return "Shared Residential Parking"
        elif self.shared_lane_residential(way):
            return "Shared Lane Residential"
        elif self.busway(way):
            return "Busway"
        elif self.cycleway(way):
            return "Cycleway"

    # Might be a bit to general
    def cycleway(self, way):
        return way["highway"] == "cycleway"

    def lane(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "lane"

    def right_lane(self, way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "lane"

    def both_lane(self, way):
        if "cycleway:both" in way:
            return way["cycleway:both"] == "lane"

    def opposite(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite"

    def opposite_lane(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_lane"

    def track(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "track"

    # Distinction with track might be unnecessary
    def right_track(self, way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "track"

    def opposite_track(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_track"

    def share_busway(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "share_busway"

    def share_busway_right(self, way):
        if "cycleway:right" in way:
            return way["cycleway:right"] == "share_busway"

    def share_busway_left(self, way):
        if "cycleway:left" in way:
            return way["cycleway:left"] == "share_busway"

    def opposite_share_busway(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "opposite_share_busway"
        elif "cycleway:opposite" in way:
            return way["cycleway:opposite"] == "share_busway"

    def shared_lane(self, way):
        if "cycleway" in way:
            return way["cycleway"] == "shared_lane"

    # Residential streets that do not specifically disallow bikes and therefore have shared lanes
    def shared_lane_residential(self, way):
        if "highway" in way and "bicycle" in way:
            return way["highway"] == "residential" and way["bicycle"] != "no" and "cycleway" not in way
        # Disallowing cycleways might be unnecessary

        if "highway" in way:
            return way["highway"] == "residential" and "cycleway" not in way

    # Residential streets like above, but with possibility for parking (there might be overlap between the two!)
    def shared_residential_parking(self, way):
        parking = {True for k, v in way.items() if k.startswith('parking')}  # TODO: Check for this

        if "highway" in way and "bicycle" in way:
            return way["highway"] == "residential" and way["bicycle"] != "no" and "cycleway" not in way and parking

        if "highway" in way:
            return way["highway"] == "residential" and "cycleway" not in way and parking

        """
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway=residential][bicycle!=no][~'^parking:.*$'~'.'][!cycleway]"

        return return_s + Cycleway.out
        """

    # Busway
    def busway(self, way):
        if "busway" in way:
            return way["busway"] == "lane"
