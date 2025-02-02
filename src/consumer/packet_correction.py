from datetime import timedelta


class PacketCorrection:
    def __init__(self, records, file_name):
        self.records = records
        self.log_file = file_name
    
    def correct_late_packets(self, bucket, new_packet):
        for past_bucket in list(self.records.keys()):
            if past_bucket < bucket - timedelta(seconds=1):
                continue
            
            packets = self.records[past_bucket]
            updated_packets = packets + [new_packet]
            avg_lat = sum(p["geo_location"]["latitude"] for p in updated_packets) / len(updated_packets)
            avg_lon = sum(p["geo_location"]["longitude"] for p in updated_packets) / len(updated_packets)
            avg_height = sum(p["geo_location"]["height"] for p in updated_packets) / len(updated_packets)
            
            correction = f"Correction: Time: {past_bucket}, New Avg Position: ({avg_lat}, {avg_lon}, {avg_height})"
            print(correction)
            with open(self.log_file, "a") as log:
                log.write(correction + "\n")