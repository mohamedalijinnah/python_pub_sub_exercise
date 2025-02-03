import unittest


from src.const import NL_LAT_LONG_BOUNDARY

class TestMain(unittest.TestCase):

    def test_main(self):
        pass
    def test_nl_geo_data_boundary(self):
        self.assertEqual(NL_LAT_LONG_BOUNDARY, ((50.77083, 53.35917), (3.57361, 7.10833)))

    def test_nl_geo_data_boundary_latitude(self):
        self.assertEqual(NL_LAT_LONG_BOUNDARY[0], ((50.77083, 53.35917)))

    def test_nl_geo_data_boundary_longitude(self):
        self.assertEqual(NL_LAT_LONG_BOUNDARY[1], ((3.57361, 7.10833)))       

if __name__ == '__main__':
    unittest.main()