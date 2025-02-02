import socket
import uuid
import json
import time

from geo_location_packet_generator import GeoLocationPacketGenerator
from geo_location_randomizer import GeoLocationRandomizer
from geo_location_generator import GeoLocationGenerator
from geo_location_height_randomizer import HeightRandomizer
from publisher.utils.const import BROADCAST_IP, BROADCAST_PORT, SECONDS_RANGE
from publisher.utils.time_randomizer import TimeRandomizer


def instance_publisher():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    instance_id = uuid.uuid4().hex

    geo_location_randomizer = GeoLocationRandomizer()
    geo_location_height_randomzier = HeightRandomizer()

    geo_location_generator = GeoLocationGenerator(geo_location_randomizer, geo_location_height_randomzier)
    
    geo_location_packet_generator = GeoLocationPacketGenerator(instance_id, geo_location_generator)
    
    time_randomizer = TimeRandomizer()

    while True:
        packet = geo_location_packet_generator.generate_geo_location_packet()
        print(f"Sending packet: {packet}")  
        sock.sendto(json.dumps(packet).encode(), (BROADCAST_IP, BROADCAST_PORT))
        time.sleep(time_randomizer.generate_random_seconds(SECONDS_RANGE[0], SECONDS_RANGE[1])) 

if __name__ == "__main__":
    instance_publisher()