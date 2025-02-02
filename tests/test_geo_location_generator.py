import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock, patch

from geo_location_generator import GeoLocationGenerator

class TestGeoLocationGenerator(unittest.TestCase):

    def test_generate_geo_location(self):

        latitude = 52.132633
        longitude = 5.291266
        height = 300

        MockLocation = MagicMock()
        MockLocation.generate_random_location.return_value = (latitude, longitude)
                                                          
        MockHeight = MagicMock()
        MockHeight.generate_random_height.return_value = height

        locationGenerator = GeoLocationGenerator(MockLocation, MockHeight)
        result = locationGenerator.generate_geo_location()
        self.assertEqual(result['latitude'], latitude)
        self.assertEqual(result['longitude'], longitude)
        self.assertEqual(result['height'], height)

        MockLocation.generate_random_location.assert_called_once()
        MockHeight.generate_random_height.assert_called_once()

if __name__ == "__main__":
    unittest.main()
