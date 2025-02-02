import sys
import os

from publisher.geo_location_randomizer import GeoLocationRandomizer
from const import NL_LAT_LONG_BOUNDARY 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest


class TestGeoLocationRandomizer(unittest.TestCase):
    repeat_count = 1000
    def setUp(self):
        self.LATITUDE_RANGE = NL_LAT_LONG_BOUNDARY[0]
        self.LONGITUDE_RANGE = NL_LAT_LONG_BOUNDARY[1]

    def test_location_within_range(self):
        location_randomizer = GeoLocationRandomizer()
        for _ in range(self.repeat_count):
            lat, lon = location_randomizer.generate_random_location(NL_LAT_LONG_BOUNDARY[0], NL_LAT_LONG_BOUNDARY[1])
            self.assertGreaterEqual(lat, self.LATITUDE_RANGE[0], "Latitude is below minimum range")
            self.assertLessEqual(lat, self.LATITUDE_RANGE[1], "Latitude exceeds maximum range")
            self.assertGreaterEqual(lon, self.LONGITUDE_RANGE[0], "Longitude is below minimum range")
            self.assertLessEqual(lon, self.LONGITUDE_RANGE[1], "Longitude exceeds maximum range")

    def test_location_outside_range_of_nl(self):
        location_randomizer = GeoLocationRandomizer()
        for _ in range(self.repeat_count):
            lat, lon =  location_randomizer.generate_random_location((8.09008, 34.55765), (68.82655, 96.12882))
            self.assertLessEqual(lat, self.LATITUDE_RANGE[0], "Latitude is below minimum range")
            self.assertLessEqual(lat, self.LATITUDE_RANGE[1], "Latitude exceeds maximum range")
            self.assertGreaterEqual(lon, self.LONGITUDE_RANGE[0], "Longitude is below minimum range")
            self.assertGreaterEqual(lon, self.LONGITUDE_RANGE[1], "Longitude exceeds maximum range")


if __name__ == "__main__":
    unittest.main()
