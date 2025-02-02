import unittest
from unittest.mock import patch, MagicMock
import socket

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'consumer')))

from src.consumer.consumer import Consumer 

class TestConsumer(unittest.TestCase):

    @patch("socket.socket") 
    @patch("packet_processor.PacketProcessor")  
    def setUp(self, mock_packet_processor, mock_socket):
        self.mock_sock = MagicMock()
        mock_socket.return_value = self.mock_sock 

        self.mock_processor = MagicMock()
        mock_packet_processor.return_value = self.mock_processor 

        self.consumer = Consumer()

    def test_consumer_initialization(self):
        self.consumer.sock.bind.assert_called_once_with(("localhost", 3000))  
        self.assertIsInstance(self.consumer.packet_processor, MagicMock) 

    @patch("builtins.print")  # Mock print to verify output
    def test_consumer_listen(self, mock_print):
        test_data = b'{"instance_id": "123", "geo_location": {"latitude": 52.1, "longitude": 5.2, "height": 100}, "timestamp": 1700000000.0}'
        
        self.mock_sock.recvfrom.return_value = {test_data, ("localhost", 300)}
        
        self.consumer.listen(isTest=True)

        self.mock_processor.process_packet.assert_called_once_with(test_data) 

    def test_consumer_listen_no_data(self):
    
        self.mock_sock.recvfrom.return_value = {b"", ("localhost", 3000)}

        self.consumer.listen(isTest=True)

        self.mock_processor.process_packet.assert_called_once_with(b"")  # Ensure it tries to process empty data

if __name__ == "__main__":
    unittest.main()
