import time

class GeoLocationPacketGenerator:

    def __init__(self, instanceId, geo_location_generator):
        self.instanceId = instanceId
        self.geo_location_generator = geo_location_generator

    def generate_geo_location_packet(self):
        geo_location = self.geo_location_generator.generate_geo_location()
        
        geo_location_packet = {
            "instance_id": self.instanceId, 
            "geo_location": geo_location,
            "timestamp": time.time()
        }
        return geo_location_packet