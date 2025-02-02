import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from unittest.mock import patch, MagicMock
import json
import socket

from consumer.consumer import Consumer

class TestConsumer(unittest.TestCase):
    @patch("socket.socket")
    def test_consumer_listen(self, mock_socket):
        mock_packet = {'instance_id': '6c95afc8e1954caf936a453b92bd794c', 'geo_location': {'latitude': 52.159438360057834, 'longitude': 4.964435361392081, 'height': 374.62729631245577}, 'timestamp': 1738513453.6593053}
        encoded_mock_packet = json.dumps(mock_packet).encode()
        
        mock_sock_instance = MagicMock()
        mock_sock_instance.recvfrom.return_value = (encoded_mock_packet, ('localhost', 3000))
        mock_socket.return_value = mock_sock_instance

        consumer = Consumer()
        with patch.object(consumer, 'process_packet') as mock_process_packet:
            consumer.listen(isTest=True)
            mock_process_packet.assert_called_once_with(encoded_mock_packet)

        mock_sock_instance.bind.assert_called_once_with(("", 3000))

    def test_process_packet(self):
        
        consumer = Consumer()

        mock_packet = {'instance_id': '6c95afc8e1954caf936a453b92bd794c', 'geo_location': {'latitude': 52.159438360057834, 'longitude': 4.964435361392081, 'height': 374.62729631245577}, 'timestamp': 1738513453.6593053}
        encoded_mock_packet = json.dumps(mock_packet)

        with patch("builtins.print") as mock_print:
            consumer.process_packet(encoded_mock_packet)
            mock_print.assert_called_once_with(mock_packet)  # Ensure the correct JSON is printed


if __name__ == "__main__":
    unittest.main()
