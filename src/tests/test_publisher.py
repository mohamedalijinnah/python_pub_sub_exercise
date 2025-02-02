import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'publisher')))
import unittest
from unittest.mock import patch, MagicMock
import json
import socket

from src.publisher.publisher import GeoLocationPublisher

class TestInstancePublisher(unittest.TestCase):
    @patch("socket.socket")
    @patch("geo_location_packet_generator.GeoLocationPacketGenerator")
    @patch("geo_location_generator.GeoLocationGenerator")
    @patch("geo_location_randomizer.GeoLocationRandomizer")
    @patch("geo_location_height_randomizer.HeightRandomizer")
    @patch("time_randomizer.TimeRandomizer")
    @patch("time.sleep")
    def test_instance_publisher(self, mock_sleep, mock_time_randomizer, mock_height_gen,
                                 mock_location_randomizer, mock_location_gen, mock_packet_gen, mock_socket):
        
        latitude = 52.132633
        longitude = 5.291266
        height = 300

        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock

        mock_packet_generator_instance = MagicMock()
        mock_packet_generator_instance.generate_geo_location_packet.return_value = {
                "instance_id": "test-instance-123",
                "geo_location": {"latitude": latitude, "longitude": longitude, "height": height},
                "timestamp": 1700000000.0,
            }
        
        mock_packet_gen.return_value = mock_packet_generator_instance

        mock_location_gen_instance = MagicMock()
        mock_location_gen.return_value = mock_location_gen_instance

        mock_location_randomizer_instance = MagicMock()
        mock_location_randomizer.return_value = mock_location_randomizer_instance

        mock_height_gen_instance = MagicMock()
        mock_height_gen.return_value = mock_height_gen_instance

        mock_time_randomizer_instance = MagicMock()
        mock_time_randomizer.return_value = mock_time_randomizer_instance
 
        mock_sleep.return_value = None

        GeoLocationPublisher("test-instance-123", mock_packet_generator_instance, mock_time_randomizer_instance).instance_publisher(isTest=True) 
        
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  
        mock_sock.setsockopt.assert_called_once_with(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        mock_sock.sendto.assert_called_once()

        sent_data, sent_address = mock_sock.sendto.call_args[0]

        self.assertEqual(sent_address, ("localhost", 3000))

        print(sent_data.decode())
        sent_packet = json.loads(sent_data.decode()) 
        expected_packet = {
            "instance_id": "test-instance-123",
            "geo_location": {"latitude": latitude, "longitude": longitude, "height": height},
            "timestamp": 1700000000.0,
        }
        self.assertEqual(sent_packet, expected_packet)


if __name__ == "__main__":
    unittest.main()
