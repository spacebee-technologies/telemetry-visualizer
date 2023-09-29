import socket
import network_parameters as np
from message_manager import MessageManager

class UdpHandler:

    def __init__(self,ip,port):
        self.ip = ip
        self.port =port



    def receive(self):
        print("Listen to port...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip,self.port))

        data, addr = sock.recvfrom(1024)

        print(f"Recibido mensaje de {addr}: {data.hex()}")
        return data

       
       

class Communication:
    def __init__(self):
        self.udp=UdpHandler(np.IP,np.PORT)

    
    def receive(self):
        return self.udp.receive()
    

