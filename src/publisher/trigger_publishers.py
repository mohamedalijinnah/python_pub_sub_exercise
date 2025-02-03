import multiprocessing
import uuid
from geo_location_generator import GeoLocationGenerator
from geo_location_height_randomizer import HeightRandomizer
from geo_location_packet_generator import GeoLocationPacketGenerator
from geo_location_randomizer import GeoLocationRandomizer
from publisher import GeoLocationPublisher
from time_randomizer import TimeRandomizer

def start_publisher(instance_id):
    publisher = GeoLocationPublisher(GeoLocationPacketGenerator(instance_id, GeoLocationGenerator(GeoLocationRandomizer(), HeightRandomizer())), TimeRandomizer())
    publisher.instance_publisher()

if __name__ == "__main__":

    instance_count = int(input("No of publisher instance:"))
    processes = []
    for _ in range(instance_count):
        process = multiprocessing.Process(target=start_publisher, args=(uuid.uuid4().hex,))
        process.start()
        processes.append(process)
    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()