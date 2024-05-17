import socket
import time
from ping3 import ping, verbose_ping

class KLE:
    def __init__(self):
        self.response_messages = []
    def attack_algo(self, interval, max_time):
        start_time = time.time()
        initial_interval = interval

        while time.time() - start_time < max_time:
            if verbose_ping(self.hst_port, timeout=1, count=1):
                print(f"[+] {self.hst_port} successfully send response")

            time.sleep(initial_interval)

            initial_interval /= 2
        
    