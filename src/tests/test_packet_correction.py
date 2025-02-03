import unittest
from unittest.mock import patch, mock_open
from datetime import datetime

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'consumer')))

from src.consumer.packet_correction import PacketCorrection 
class TestPacketCorrection(unittest.TestCase):

    def setUp(self):
        self.records = {
            datetime(2025, 2, 3, 12, 0, 0): [
                {"geo_location": {"latitude": 52.1, "longitude": 5.2, "height": 100}},
                {"geo_location": {"latitude": 52.3, "longitude": 5.4, "height": 200}},
            ],
            datetime(2025, 2, 3, 12, 0, 1): [
                {"geo_location": {"latitude": 52.2, "longitude": 5.3, "height": 150}},
            ],
        }
        self.test_file = "test_corrections.log"
        self.packet_correction = PacketCorrection(self.records, self.test_file)

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_correct_late_packets(self, mock_file, mock_print):
        new_packet = {"geo_location": {"latitude": 52.4, "longitude": 5.5, "height": 250}}
        bucket_time = datetime(2025, 2, 3, 12, 0, 1) 

        self.packet_correction.correct_late_packets(bucket_time, new_packet)

        expected_correction = "Correction: Time: 2025-02-03 12:00:01, New Avg Position: (52.3, 5.4, 200.0)"
        
        mock_print.assert_any_call(expected_correction)

        mock_file.assert_called_with(self.test_file, "a")
        mock_file().write.assert_called_with(expected_correction + "\n")

    @patch("builtins.print")
    def test_no_correction_needed(self, mock_print):
        new_packet = {"geo_location": {"latitude": 52.5, "longitude": 5.6, "height": 300}}
        bucket_time = datetime(2025, 2, 3, 12, 0, 3)

        self.packet_correction.correct_late_packets(bucket_time, new_packet)
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_empty_bucket(self, mock_print):
        new_packet = {"geo_location": {"latitude": 52.6, "longitude": 5.7, "height": 350}}
        bucket_time = datetime(2025, 2, 3, 18, 0, 2)
        self.packet_correction.correct_late_packets(bucket_time, new_packet)
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
