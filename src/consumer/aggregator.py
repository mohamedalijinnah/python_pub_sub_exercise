class Aggregator:
     
     def __init__(self, records, file_name):
         self.records = records
         self.log_file = file_name

     def aggregate_and_log(self, bucket):
        packets = self.records[bucket]
        if not packets:
            return
        
        avg_lat = round(sum(p["geo_location"]["latitude"] for p in packets) / len(packets), 2)
        avg_lon = round(sum(p["geo_location"]["longitude"] for p in packets) / len(packets), 2)
        avg_height = round(sum(p["geo_location"]["height"] for p in packets) / len(packets), 2)
        
        result = f"Time: {bucket}, Avg Position: ({avg_lat}, {avg_lon}, {avg_height})"
        print(result)
        with open(self.log_file, "a") as log:
            log.write(result + "\n")