from collections import defaultdict
from datetime import datetime
import json
import threading

from aggregator import Aggregator
from packet_correction import PacketCorrection

class PacketProcessor:
    def __init__(self):
        self.records = defaultdict(list)
        self.lock = threading.Lock()
        self.aggregator = Aggregator(self.records, "aggregated_geo_data.log")
        self.packet_correction = PacketCorrection(self.records, "aggregated_geo_data.log")

    def process_packet(self, data):
        packet = json.loads(data)
        print(packet)
        if not packet:
         return None
        time_stamp = packet['timestamp']
        time_bucket = datetime.fromtimestamp(time_stamp).replace(microsecond=0)
        self.records[time_bucket].append(packet)
        
        with self.lock:
            self.records[time_bucket].append(packet)
            self.aggregator.aggregate_and_log(time_bucket)
            self.packet_correction.correct_late_packets(time_bucket, packet)
        
            