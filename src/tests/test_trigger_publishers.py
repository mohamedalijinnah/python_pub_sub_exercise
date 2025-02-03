
import unittest
import multiprocessing
import uuid
from unittest.mock import patch, MagicMock

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'publisher')))

from src.publisher.trigger_publishers import start_publisher

class TestPublisherMultiprocessing(unittest.TestCase):

    @patch("publisher.GeoLocationPublisher") 
    def test_start_multiple_publishers(self, MockGeoLocationPublisher):
        mock_publisher_instance = MockGeoLocationPublisher.return_value
        mock_publisher_instance.instance_publisher = MagicMock()

        instance_count = 10
        processes = []

        try:
            for _ in range(instance_count):
                process = multiprocessing.Process(target=start_publisher, args=(uuid.uuid4().hex,))
                process.start()
                processes.append(process)

            self.assertEqual(len(processes), instance_count)

        finally:
            for process in processes:
                process.terminate()
                process.join()

    def test_multiprocessing_import(self):
        try:
            import multiprocessing
            self.assertTrue(hasattr(multiprocessing, "Process"))
        except ImportError:
            self.fail("multiprocessing module could not be imported!")

if __name__ == "__main__":
    unittest.main()
