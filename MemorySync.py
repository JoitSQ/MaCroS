import time
from pathlib import Path
import tkinter
from winotify import Notification

class MemorySync:
    msgindex = 0
    inmsgindex = 0

    def __init__(self, ui):
        self.messages = []
        self.namespace = 'MemorySync'
        self.ui = ui

    def IDDater(self):
        self.MemoryStorageUpdater()
        self.messages = []

        history = open(rf"C:\MaCroS\P2PT\H-C\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'r', encoding='utf-8')

        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)

        self.messages.sort(key=lambda x: float(x[2]))

        history.close()

    def MemoryStorageUpdater(self):
        if Path(rf"C:\MaCroS\P2PT\H-C\{self.ui.chat[self.ui.chatid]}").exists():
            pass
        else:
            Path.mkdir(rf"C:\MaCroS\P2PT\H-C\{self.ui.chat[self.ui.chatid]}")
            open(rf"C:\MaCroS\P2PT\H-C\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'a', encoding='utf-8')
        self.messageinput = self.ui.message.get()
        if self.messageinput != '':
            history = open(rf"C:\MaCroS\P2PT\H-C\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'a', encoding='utf-8')
            history.write(self.messageinput + f'⁝{self.msgindex}⁝{time.time()}⁝out' + '\n')
            history.close()

            self.ui.message.delete('0', tkinter.END)

            self.msgindex += 1
            self.ui.changed = True
            self.IDDater()

    def MemoryForgor(self):
        history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'w')
        history.close()

    def MemoryReceiver(self, rmssg, sender):
        if Path(rf"C:\MaCroS\P2PT\H-C\{sender}").exists():
            pass
        else:
            Path.mkdir(rf"C:\MaCroS\P2PT\H-C\{sender}")
            open(rf"C:\MaCroS\P2PT\H-C\{sender}\history-client.txt", 'a', encoding='utf-8')
        rmssg = rmssg.decode('utf-8')
        self.sendername, rmssg = rmssg.split('ͳ')
        if rmssg == 'Onlineλ':
            return
        if rmssg != '':
            if self.ui.trayed:
                notif = Notification(app_id='MaCroS', title="You've got mail!", msg=f'{self.sendername}: {rmssg}')
                notif.show()
            self.ui.inshadowtext = 123123
            self.inmsgindex += 1
            history = open(rf"C:\MaCroS\P2PT\H-C\{sender}\history-client.txt", 'a', encoding='utf-8')
            history.write(rmssg + f'⁝{self.inmsgindex}⁝{time.time()}⁝in' + '\n')
            history.close()
        elif rmssg == '':
            pass
        self.messages = []
        history = open(rf"C:\MaCroS\P2PT\H-C\{sender}\history-client.txt", 'r', encoding='utf-8')
        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)
        self.messages.sort(key=lambda x: float(x[2]))
        history.close()
        self.ui.changed=True
