import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from main import publish_geo_data

class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEqual(publish_geo_data(), (52.132633, 5.291266))

if __name__ == '__main__':
    unittest.main()