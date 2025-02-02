import socket
import json

from const import BROADCAST_PORT
class Consumer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", BROADCAST_PORT))

    def process_packet(self, data):
        packet = json.loads(data)
        print(packet)


    def listen(self, isTest=False):
        while True:
            data, _ = self.sock.recvfrom(1024)
            self.process_packet(data)
            if isTest:
                break

if __name__ == "__main__":
    consumer = Consumer()
    consumer.listen()
