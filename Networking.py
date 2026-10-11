import socket
from tkinter import messagebox


class Networking:
    def __init__(self, ui, memory):
        self.sender=''
        self.receivedmsg=0
        # as proven, __init__ doesn't do shit :sob:
        self.PORT = 1
        self.HOST = 'localhost'
        self.target_host = ''
        self.ui = ui
        self.RELAY = '192.168.3.11'
        self.memory = memory

    # Deprecated function, I now invented a H.O.S.T. system
    #         |             This now means that we have THE SERVERRR!!!! My laptop will NOT pose as such with it being
    #         V             a core to the messenger infrastructure, meaning: the IP will be fixed from now on
    #                                        / \
    #                       This is bullshit  |   I invented AMR, check notes
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

    def SendNetwork(self):
        client = self.ui.chat[self.ui.chatid]
        print(client)
        print(self.HOST)
        if client == self.HOST:
            self.SendNetworkTest(False)
        else:
            self.SendNetworkTest(True)

    def SendNetworkTest(self, sending):
        self.PORT = 1
        client = self.ui.chat[self.ui.chatid]
        if self.ui.message.get() != '':
            if sending:
                try:
                    with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                        s.settimeout(1000)
                        s.connect((self.RELAY, self.PORT))
                        s.sendall(bytes(self.ui.nickname, 'utf-8') +bytes(self.ui.message.get(), 'utf-8') + bytes('Σ', 'utf-8') + bytes(client, 'utf-8'))
                        chk = s.recv(1024)
                        if chk==b'Rec':
                            self.memory.MemoryStorageUpdater()
                        else:
                            messagebox.showerror('Oops!', 'Client unreachable!')
                except OSError as e:
                    messagebox.showerror('Oops!', f'Relay unavailable! \n {e}')
            else:
                self.memory.MemoryStorageUpdater()
    def ReceiveNetworkTest(self):
        self.PORT = 1
        self.HOST = '26.0.2.167'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(4096)
                    plchldr, rmssg = data.decode('utf-8').split('ͳ')
                    rmssg, senderip = rmssg.split('Σ')
                    self.sender=senderip if senderip != self.RELAY else 'undefined'
                    if "Onlineλ" not in data.decode('utf-8'):
                        self.memory.MemoryReceiver(data, self.sender)
                        conn.send(b'Rec')
                    if 'Onlineλ' in data.decode('utf-8'):
                        conn.send(b'ConfirmedOnlineSentBack')

    def IsOnline(self, client):
        if client != self.HOST:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(.2)
                    s.connect((self.RELAY, self.PORT))
                    s.send(bytes(self.ui.nickname, 'utf-8') +bytes('Onlineλ', 'utf-8') + bytes('Σ', 'utf-8') + bytes(client, 'utf-8'))
                    if b'ConfirmedOnlineSentBack' in s.recv(1024):
                        return True
            except (ConnectionRefusedError, TimeoutError, OSError):
                return False
        else:
            return 'hide'