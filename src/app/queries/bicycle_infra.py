

class Cycleway:

    default_sw = "(44.490204027212016, 11.269648275756735"
    default_ne = "44.520311680337684, 11.433445623245943)"

    # Highway - Independent Cycleway

    def cycleway():
        return_s = "[out:json];"

        return_s += "way[highway=cycleway]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"


    # Cycleway - Shared Cycleway

    def lane():
        return_s = "[out:json];"

        return_s += "way[cycleway=lane]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def opposite():
        return_s = "[out:json];"

        return_s += "way[cycleway=opposite]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def opposite_lane():
        return_s = "[out:json];"

        return_s += "way[cycleway=opposite_lane]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def track():
        return_s = "[out:json];"

        return_s += "way[cycleway=track]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def opposite_track():
        return_s = "[out:json];"

        return_s += "way[cycleway=opposite_track]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def share_busway():
        return_s = "[out:json];"

        return_s += "way[cycleway=share_busway]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def opposite_share_busway():
        return_s = "[out:json];"

        return_s += "way[cycleway=opposite_share_busway]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    def shared_lane():
        return_s = "[out:json];"

        return_s += "way[cycleway=shared_lane]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"

    # Busway

    def lane():
        return_s = "[out:json];"

        return_s += "way[busway=lane]"
        
        return_s += Cycleway.default_sw + ","
        
        return_s += Cycleway.default_ne + ";"

        return return_s + "out;"
