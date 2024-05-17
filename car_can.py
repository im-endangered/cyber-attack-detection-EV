import socket
import time

class CarCan:
    def __init__(self):
        self.car_status = "Not Attacked"
        self.attack_threshold = 0.5
        self.last_request_time = time.time()
        self.server_messages = []
    def get_car_status(self):
        print(self.car_status)


    def start_dst(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 8080))
        serversocket.listen(5)
        attack_flag = False
        while True:
            (receiving_socket, address) = serversocket.accept()
            data = receiving_socket.recv(1024)

            elapsed_time = time.time() - self.last_request_time

            if elapsed_time < self.attack_threshold:
                self.server_messages.append("[!] Upper Bound Crossed! Shutting down system.")
                self.car_status = "Attack attempted"
                attack_flag = True
                break
            else:
                self.server_messages.append("[!] Possible connection request")
                
            self.last_request_time = time.time()

            receiving_socket.send('')

            receiving_socket.close()
        if attack_flag:
            self.car_status = "Attacked"