import unittest
from unittest.mock import patch
from datetime import datetime
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'consumer')))

from src.consumer.packet_processor import PacketProcessor
from src.consumer.aggregator import Aggregator
from src.consumer.packet_correction import PacketCorrection

class TestPacketProcessor(unittest.TestCase):
    def test_process_packet(self):
        packet = {
            "instance_id": "123",
            "geo_location": {"latitude": 52.1, "longitude": 5.2, "height": 100},
            "timestamp": 1700000000.0
        }

        processor = PacketProcessor()

        data = json.dumps(packet) 
        processor.process_packet(data)

        time_stamp = packet['timestamp']
        time_bucket = datetime.fromtimestamp(time_stamp).replace(microsecond=0)

        self.assertIn(time_bucket, processor.records)
        self.assertIn(packet, processor.records[time_bucket])


    @patch.object(Aggregator, 'aggregate_and_log') 
    @patch.object(PacketCorrection, 'correct_late_packets')
    def test_process_packet_empty(self, mock_correct_late_packets, mock_aggregate_and_log):
        processor = PacketProcessor()

        empty_packet = {}
        data = json.dumps(empty_packet)

        processor.process_packet(data)

        mock_aggregate_and_log.assert_not_called()
        mock_correct_late_packets.assert_not_called()


if __name__ == "__main__":
    unittest.main()
