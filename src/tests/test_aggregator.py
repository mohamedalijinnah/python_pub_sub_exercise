import unittest
from unittest.mock import patch, mock_open

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'consumer')))

from src.consumer.aggregator import Aggregator

class TestAggregator(unittest.TestCase):

    def setUp(self):
        self.test_records = {
            1700000000: [
                {"geo_location": {"latitude": 52.1, "longitude": 5.2, "height": 100}},
                {"geo_location": {"latitude": 52.3, "longitude": 5.4, "height": 200}},
            ],
            1700000001: []
        }
        self.test_file = "test_log.txt"
        self.aggregator = Aggregator(self.test_records, self.test_file)

    @patch("builtins.print")
    def test_aggregate_and_log_valid_data(self, mock_print):
        self.aggregator.aggregate_and_log(1700000000)

        expected_output = "Time: 1700000000, Avg Position: (52.2, 5.3, 150.0)"
        mock_print.assert_called_once_with(expected_output)

    @patch("builtins.open", new_callable=mock_open) 
    def test_aggregate_and_log_file_write(self, mock_file):
        self.aggregator.aggregate_and_log(1700000000)

        expected_output = "Time: 1700000000, Avg Position: (52.2, 5.3, 150.0)\n"
    
        mock_file.assert_called_once_with(self.test_file, "a")
        
        mock_file().write.assert_called_once_with(expected_output)

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_aggregate_and_log_empty_bucket(self, mock_file, mock_print):
        self.aggregator.aggregate_and_log(1700000001)

        mock_print.assert_not_called()
        mock_file().write.assert_not_called()

if __name__ == "__main__":
    unittest.main()
