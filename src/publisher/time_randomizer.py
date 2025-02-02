from random import uniform

class TimeRandomizer:
    def generate_random_seconds(self, min, max):
        return uniform(min, max)