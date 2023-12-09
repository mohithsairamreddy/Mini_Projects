import rpyc
from rpyc.utils.server import ThreadedServer

class Peer:
    def __init__(self, ip, tracker_ip):
        self.ip = ip
        self.tracker = rpyc.connect(tracker_ip, port=8000, service=TrackerService)
        self.file_list = {}
        self.chunk_list = {}

    def register(self, file_list):
        self.file_list = file_list
        self.tracker.root.register(self.ip, self.file_list)

    def download(self, file_name):
        peer_ips = self.tracker.root.find_peers(file_name)

        for peer_ip in peer_ips:
            if peer_ip == self.ip:
                continue

            peer = rpyc.connect(peer_ip, port=8000)
            chunks = peer.root.get_chunks(file_name)

            for chunk_index, chunk_data in chunks.items():
                if chunk_index not in self.chunk_list:
                    self.chunk_list[chunk_index] = chunk_data
                    print(f"Downloaded chunk {chunk_index} of {file_name} from {peer_ip}")

    def get_chunks(self, file_name):
        chunks = {}

        with open(file_name, "rb") as f:
            while True:
                chunk_data = f.read(1024)

                if not chunk_data:
                    break

                chunk_index = len(chunks)
                chunks[chunk_index] = chunk_data

        return chunks

if __name__ == '__main__':
    conn = rpyc.connect('192.168.208.21',8000)
    print(conn.root.exposed_sen())
    conn.root.exposed_register('192.168.208.199',['file2.txt','file3.txt'])