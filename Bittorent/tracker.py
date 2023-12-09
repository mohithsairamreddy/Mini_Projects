import rpyc
from rpyc.utils.server import ThreadedServer

class TrackerService(rpyc.Service):
    self.files ={}
    self.peers={}
     

    def exposed_register(self, peer_ip, file_list):
        if peer_ip in self.peers:
            return False

        self.peers[peer_ip] = file_list
        print(self.peers)

        for file_name in file_list:
            if file_name not in self.files:
                self.files[file_name] = []

            self.files[file_name].append(peer_ip)

        return True
    
    def exposed_find_peers(self, file_name):
        if file_name not in self.files:
            return None

        return self.files[file_name]
    def exposed_send(self):
        return "hi"
    def exposed_sen(self):
        print
        return [self.files,self.peers]
    
    
if __name__ == '__main__':
    print("Tracker is running")
    tracker = ThreadedServer(TrackerService, port=8000)
    tracker.start()
    