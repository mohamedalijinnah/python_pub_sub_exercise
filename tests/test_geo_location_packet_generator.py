import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock

from geo_location_packet_generator import GeoLocationPacketGenerator

class TestGeoLocationPacketGenerator(unittest.TestCase):
    def test_generate_geo_location_packet_generator(self):
        
        latitude = 52.132633
        longitude = 5.291266
        height = 300

        instance_id = 1
        MockGeoLocationGenerator = MagicMock()
        MockGeoLocationGenerator.generate_geo_location.return_value = {
            "latitude": latitude,
            "longitude": longitude,
            "height": height
        }
        generator = GeoLocationPacketGenerator(instance_id, MockGeoLocationGenerator)
        result = generator.generate_geo_location_packet()
        self.assertEqual(result['instance_id'], instance_id)
        self.assertEqual(result['geo_location']['latitude'], latitude)
        self.assertEqual(result['geo_location']['longitude'], longitude)
        self.assertEqual(result['geo_location']['height'], height)
        self.assertIsNotNone(result['timestamp'])

        MockGeoLocationGenerator.generate_geo_location.assert_called_once()


