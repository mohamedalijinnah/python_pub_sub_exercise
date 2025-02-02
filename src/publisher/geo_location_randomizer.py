from random import uniform

class GeoLocationRandomizer:
    def generate_random_location(self, latitude_range, longitude_range):
        lat = uniform(latitude_range[0], latitude_range[1])
        lon = uniform(longitude_range[0], longitude_range[1])
        return lat, lon