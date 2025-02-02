from const import NL_LAT_LONG_BOUNDARY, HEIGHT_RANGE

class GeoLocationGenerator:
    def __init__(self, location_generator, height_generator):
        self.location_generator = location_generator
        self.height_generator = height_generator

    def generate_geo_location(self):
        random_lat_long = self.location_generator.generate_random_location(NL_LAT_LONG_BOUNDARY[0], NL_LAT_LONG_BOUNDARY[1])
        random_height = self.height_generator.generate_random_height(HEIGHT_RANGE[0], HEIGHT_RANGE[1])
        
        geo_location = {
            "latitude": random_lat_long[0],
            "longitude": random_lat_long[1],
            "height": random_height,
        }
        return geo_location
    