import threading
from rpyc import ClassicService
import rpyc
tracker_thread = threading.Thread(target=rpyc.ClassicServer(TrackerService).start)
tracker_thread.start()

tracker_ip = 'localhost'

peer1 = peer('192.168.68.199', tracker_ip)
peer2 = peer('192.168.68.156', tracker_ip)

peer1.register({'file1.txt', 'file2.txt'})
peer2.register({'file2.txt', 'file3.txt'})

download_threads = []
for file_name in peer1.file_list:
    thread = threading.Thread(target=peer1.download, args=(file_name,))
    thread.start()
    download_threads.append(thread)

for thread in download_threads:
    thread.join()

tracker_thread.join()