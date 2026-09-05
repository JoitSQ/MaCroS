import socket

from MemorySync import MemorySync
from UInit import UI
from tkinter import messagebox


class Networking:
    def __init__(self):
        # as proven, __init__ doesn't do shit :sob:
        self.PORT = 55485
        self.HOST = 'localhost'  # Fill out according to the H.O.S.T system
        self.target_host = ''

    # Deprecated function, I now invented a H.O.S.T. system
    #         |             This now means that we have THE SERVERRR!!!! My laptop will pose as such with it being
    #         V             a core to the messenger infrastructure, meaning: the IP will be fixed from now on
    def IPSetinit(self):
        with open(r"C:\MaCroS\P2PT\H-C\ipset.txt", 'r') as ipset:
            ippp = ipset.readlines()
            for i in range(len(ippp)):
                if i == 0:
                    self.host = ippp[i]
                else:
                    self.TARGET_HOST.append(ippp[i])
        for i in self.host:
            if i != '\n':
                self.HOST += i

    def SendNetworkTest(self):
        self.PORT = 55485
        self.HOST = 'localhost'  # Fill out according to the H.O.S.T system
        self.target_host = ''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(bytes(UI.message.get(), 'utf-8'))
            data = s.recv(1024)
            if data == 'Received':
                pass
            else:
                messagebox.showerror('Error!', 'Failed to send message! Server unreachable')

    def ReceiveNetworkTest(self):
        self.PORT = 55485
        self.HOST = 'localhost'  # Fill out according to the H.O.S.T system
        self.target_host = ''
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.HOST, self.PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = conn.recv(1024)
                    MemorySync.MemoryReceiver(data)
                    fuckass = b'Received'
                    conn.sendall(fuckass)
