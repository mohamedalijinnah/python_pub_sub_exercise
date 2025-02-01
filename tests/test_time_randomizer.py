import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest

from time_randomizer import generate_random_seconds
from const import SECONDS_RANGE

class TestTimeRandomizer(unittest.TestCase):

    def test_random_seconds_inside_range(self):
        for _ in range(1000):
            self.assertGreaterEqual(generate_random_seconds(SECONDS_RANGE[0], SECONDS_RANGE[1]), SECONDS_RANGE[0], "Seconds is above minimum range")
            self.assertLessEqual(generate_random_seconds(SECONDS_RANGE[0], SECONDS_RANGE[1]), SECONDS_RANGE[1], "Seconds is below maximum range")


    def test_random_seconds_outside_range(self):
        for _ in range(1000):
            self.assertLessEqual(generate_random_seconds(0, 1), SECONDS_RANGE[0], "Seconds is below constant minimum range")
            self.assertGreaterEqual(generate_random_seconds(6, 10), SECONDS_RANGE[1], "Seconds is above constant maximum range")

if __name__ == '__main__':
    unittest.main()