import socket
import json

from const import BROADCAST_PORT
from packet_processor import PacketProcessor

class Consumer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", BROADCAST_PORT))
        self.packet_processor = PacketProcessor()

    def listen(self, isTest=False):
        while True:
            data, _ = self.sock.recvfrom(1024)
            self.packet_processor.process_packet(data)
            if isTest:
                break

if __name__ == "__main__":
    consumer = Consumer()
    consumer.listen()
