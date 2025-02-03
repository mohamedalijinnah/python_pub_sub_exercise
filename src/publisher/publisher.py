import socket
import uuid
import json
import time

from const import BROADCAST_IP, BROADCAST_PORT, SECONDS_RANGE
from geo_location_generator import GeoLocationGenerator
from geo_location_height_randomizer import HeightRandomizer
from geo_location_packet_generator import GeoLocationPacketGenerator
from geo_location_randomizer import GeoLocationRandomizer
from time_randomizer import TimeRandomizer

class GeoLocationPublisher:
    def __init__(self,geo_location_packet_generator, time_randomizer):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.geo_location_packet_generator = geo_location_packet_generator
        self.time_randomizer = time_randomizer

    def instance_publisher(self, isTest=False):
        while True:
            packet = self.geo_location_packet_generator.generate_geo_location_packet()
            print(f"Sending packet: {packet}")  
            self.sock.sendto(json.dumps(packet).encode(), (BROADCAST_IP, BROADCAST_PORT))
            time.sleep(self.time_randomizer.generate_random_seconds(SECONDS_RANGE[0], SECONDS_RANGE[1]))
            if isTest:
                break
            

if __name__ == "__main__":
    publisher = GeoLocationPublisher(GeoLocationPacketGenerator(uuid.uuid4().hex, GeoLocationGenerator(GeoLocationRandomizer(), HeightRandomizer())), TimeRandomizer())
    publisher.instance_publisher()