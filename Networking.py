import socket
from tkinter import messagebox
from winotify import Notification


class Networking:
    def __init__(self, ui, memory):
        self.sender = ''
        self.receivedmsg = False
        self.PORT = 1
        self.HOST = 'localhost'
        self.target_host = ''
        self.ui = ui
        self.RELAY = 'relay_ip_here'
        self.memory = memory

    def send_stop(self):
        client = self.ui.chat[self.ui.chatid]
        print(client)
        print(self.HOST)
        if client == self.HOST:
            self.network_sender(False)
        else:
            self.network_sender(True)

    # I need to absolutely rewrite the entirety of this code and memory controller

    def network_sender(self, sending):
        self.PORT = 1
        # Sending username, relay parses that to an IP adress
        client = self.ui.chat[self.ui.chatid]
        if self.ui.message.get('1.0', 'end-1c') != '':
            if sending:
                try:
                    with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                        s.settimeout(1000)
                        s.connect((self.RELAY, self.PORT))
                        s.sendall(bytes(self.ui.username, 'utf-8') + bytes(self.ui.message.get('1.0', 'end-1c'), 'utf-8') + bytes('Σ', 'utf-8') + bytes(client, 'utf-8'))
                        chk = s.recv(1024)
                        if chk==b'Rec':
                            self.memory.MemoryStorageUpdater()
                        else:
                            messagebox.showerror('Oops!', 'Client unreachable!')
                except OSError as e:
                    messagebox.showerror('Oops!', f'Relay unavailable! \n {e}')
            else:
                self.memory.MemoryStorageUpdater()
    def network_receiver(self):
        self.PORT = 1
        self.HOST = '0.0.0.0'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(4096)
                    self.receivedmsg = True
                    plchldr, rmssg = data.decode('utf-8').split('ͳ')
                    rmssg, senderip = rmssg.split('Σ')
                    print(plchldr, rmssg, senderip)
                    self.sender=senderip if senderip != self.RELAY else 'undefined'

                    # It's probably not rational doing this online ping packet
                    # bc of the user's input

                    # They can easily type [@Online] themselves
                    # Gotta change that a while later when i have a stable
                    # networking system

                    if "[@Online]" not in data.decode('utf-8'):
                        self.memory.MemoryReceiver(data, self.sender)
                        conn.send(b'Rec')
                        if self.ui.trayed or self.sender!=self.ui.chat[self.ui.chatid]:
                            notif = Notification(app_id='MaCroS', title="You've got mail!", msg=f'{self.sendername}: {rmssg}')
                            notif.show()
                    if '[@Online]' in data.decode('utf-8'):
                        conn.send(b'[@Online]')

    def is_online_networking(self, client):
        if client != self.HOST:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(.2)
                    s.connect((self.RELAY, self.PORT))
                    s.send(bytes(self.ui.username, 'utf-8') + bytes('Onlineλ', 'utf-8') + bytes('Σ', 'utf-8') + bytes(client, 'utf-8'))
                    if b'ConfirmedOnlineSentBack' in s.recv(1024):
                        return True
            except (ConnectionRefusedError, TimeoutError, OSError):
                return False
        else:
            return 'hide'