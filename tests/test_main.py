import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from main import publish_geo_data, get_geo_data_boundary

class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEqual(publish_geo_data(), (52.132633, 5.291266))
    
    def test_nl_geo_data_boundary(self):
        self.assertEqual(get_geo_data_boundary(), ((50.77083, 53.35917), (3.57361, 7.10833)))

if __name__ == '__main__':
    unittest.main()