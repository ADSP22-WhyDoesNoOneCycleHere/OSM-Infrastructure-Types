

class Cycleway:

    default_out = "[out:json];"
    out = ";out;"

    default_sw = "44.490204027212016, 11.269648275756735"
    default_ne = "44.520311680337684, 11.433445623245943"

    def query_area(self, sw, ne):
        # could also be changed to use node rather than "way" if not only nodes are relevant
        return "[out:json]; way(" + sw + "," + ne + ")"

    # Highway - Independent Cycleway

    def cycleway(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway=cycleway]"

        return return_s + Cycleway.out

    # Cycleway - Shared Cycleway

    def lane(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=lane]"

        return return_s + Cycleway.out

    def right_lane(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway]['cycleway:right'=lane]"

        return return_s + Cycleway.out

    def opposite(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=opposite]"

        return return_s + Cycleway.out

    def opposite_lane(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=opposite_lane]"

        return return_s + Cycleway.out

    def track(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=track]"
        # "[highway]['cycleway:right'=track]"

        return return_s + Cycleway.out

    def right_track(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway]['cycleway:right'=track]"

        return return_s + Cycleway.out

    def opposite_track(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=opposite_track]"

        return return_s + Cycleway.out

    def share_busway(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=share_busway]"

        return return_s + Cycleway.out

    def share_busway_right(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway]['cycleway:right'=share_busway]"

        return return_s + Cycleway.out

    def opposite_share_busway(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=opposite_share_busway]"
        # "way['cycleway:opposite'=share_busway]"

        return return_s + Cycleway.out

    def shared_lane(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[cycleway=shared_lane]"

        return return_s + Cycleway.out

    # Residential streets that do not specifically disallow bikes and therefore have shared lanes
    def shared_lane_residential(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway=residential][bicycle!=no][!cycleway]"

        return return_s + Cycleway.out

    # Residential streets like above, but with possibility for parking (there might be overlap between the two!)
    def shared_residential_parking(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[highway=residential][bicycle!=no][~'^parking:.*$'~'.'][!cycleway]"

        return return_s + Cycleway.out

    # Busway

    def busway(self):
        return_s = Cycleway.query_area(self, Cycleway.default_sw, Cycleway.default_ne)

        return_s += "[busway=lane]"

        return return_s + Cycleway.out
