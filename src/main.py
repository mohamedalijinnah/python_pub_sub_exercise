# Sample program to demonstrate multiple publishers

import threading
import uuid
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from consumer.consumer import Consumer
from consumer.packet_processor import PacketProcessor
from publisher.geo_location_generator import GeoLocationGenerator
from publisher.geo_location_height_randomizer import HeightRandomizer
from publisher.geo_location_packet_generator import GeoLocationPacketGenerator
from publisher.geo_location_randomizer import GeoLocationRandomizer
from publisher.publisher import GeoLocationPublisher
from publisher.time_randomizer import TimeRandomizer

if __name__ == '__main__':
    print("Simulate consumer")
    packetProcessor = PacketProcessor()
    consumer = Consumer(packetProcessor)
    consumer.listen()

    print("Simulate a geo data publishers")
    instance_count = 5 
    for i in range(instance_count):
        publisher = GeoLocationPublisher(uuid.uuid4().hex, GeoLocationPacketGenerator(uuid.uuid4().hex, 
                                                                                      GeoLocationGenerator(GeoLocationRandomizer(), HeightRandomizer())), TimeRandomizer())
      
        threading.Thread(target=publisher.instance_publisher(), args=(i,), daemon=True).start()

