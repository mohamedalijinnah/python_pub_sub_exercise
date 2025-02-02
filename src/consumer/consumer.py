import socket

from const import BROADCAST_PORT
from packet_processor import PacketProcessor

class Consumer:
    def __init__(self, packet_processor):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", BROADCAST_PORT))
        self.packet_processor = packet_processor

    def listen(self, isTest=False):
        while True:
            data, _ = self.sock.recvfrom(1024)
            self.packet_processor.process_packet(data)
            if isTest:
                break

if __name__ == "__main__":
    packetProcessor = PacketProcessor()
    consumer = Consumer(packetProcessor)
    consumer.listen()
