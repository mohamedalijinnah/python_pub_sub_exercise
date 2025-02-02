import unittest

from src.const import HEIGHT_RANGE
from src.publisher.geo_location_height_randomizer import HeightRandomizer

class TestHeightRandomizer(unittest.TestCase):

    def test_random_height_inside_range(self):
        height_randomizer = HeightRandomizer()

        for _ in range(1000):
            self.assertGreaterEqual(height_randomizer.generate_random_height(HEIGHT_RANGE[0], HEIGHT_RANGE[1]), HEIGHT_RANGE[0], "height is above minimum range")
            self.assertLessEqual(height_randomizer.generate_random_height(HEIGHT_RANGE[0], HEIGHT_RANGE[1]), HEIGHT_RANGE[1], "height is below maximum range")


    def test_random_height_outside_range(self):
        height_randomizer = HeightRandomizer()

        for _ in range(1000):
            self.assertLessEqual(height_randomizer.generate_random_height(-10, 0), HEIGHT_RANGE[0], "height is below constant minimum range")
            self.assertGreaterEqual(height_randomizer.generate_random_height(500, 1000), HEIGHT_RANGE[1], "height is above constant maximum range")

if __name__ == '__main__':
    unittest.main()