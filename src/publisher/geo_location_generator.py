
from publisher.utils.const import HEIGHT_RANGE, NL_LAT_LONG_BOUNDARY

class GeoLocationGenerator:
    def __init__(self, location_randomizer, height_randomizer):
        self.location_randomizer = location_randomizer
        self.height_randomizer = height_randomizer

    def generate_geo_location(self):
        random_lat_long = self.location_randomizer.generate_random_location(NL_LAT_LONG_BOUNDARY[0], NL_LAT_LONG_BOUNDARY[1])
        random_height = self.height_randomizer.generate_random_height(HEIGHT_RANGE[0], HEIGHT_RANGE[1])
        
        geo_location = {
            "latitude": random_lat_long[0],
            "longitude": random_lat_long[1],
            "height": random_height,
        }
        return geo_location
    