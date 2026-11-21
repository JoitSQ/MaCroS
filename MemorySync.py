import time
from pathlib import Path
import tkinter

class MemorySync:
    msgindex = 0
    inmsgindex = 0

    def __init__(self, ui):
        self.messages = []
        self.namespace = 'MemorySync'
        self.ui = ui
        self.RELAY = '127.0.0.1' # wtf

    def IDDater(self):
        self.MemoryStorageUpdater()
        self.messages = []

        history = open(rf"C:\MaCroS\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'r', encoding='utf-8')

        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)

        self.messages.sort(key=lambda x: float(x[2]))

        history.close()

    def MemoryStorageUpdater(self):
        if Path(rf"C:\MaCroS\{self.ui.chat[self.ui.chatid]}").exists():
            pass
        else:
            Path(rf"C:\MaCroS\{self.ui.chat[self.ui.chatid]}").mkdir()
            open(rf"C:\MaCroS\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'a', encoding='utf-8')
        self.messageinput = self.ui.message.get('1.0', 'end-1c')
        if self.messageinput != '':
            history = open(rf"C:\MaCroS\{self.ui.chat[self.ui.chatid]}\history-client.txt", 'a', encoding='utf-8')
            history.write(self.messageinput + f'⁝{self.msgindex}⁝{time.time()}⁝out' + '\n')
            history.close()

            self.ui.message.delete('1.0', 'end-1c')

            self.msgindex += 1
            self.ui.changed = True
            self.IDDater()

    def MemoryForgor(self):
        history = open(r"C:\MaCroS\history-client.txt", 'w')
        history.close()

    def MemoryReceiver(self, rmssg, sender):
        if Path(rf"C:\MaCroS\{sender}").exists():
            pass
        else:
            Path.mkdir(rf"C:\MaCroS\{sender}")
            open(rf"C:\MaCroS\{sender}\history-client.txt", 'a', encoding='utf-8')
        rmssg = rmssg.decode('utf-8')
        if rmssg == 'Onlineλ':
            return
        self.sendername, rmssg = rmssg.split('ͳ')
        print(rmssg)
        rmssg, senderip = rmssg.split('Σ')
        if rmssg != '':
            self.ui.inshadowtext = 123123
            self.inmsgindex += 1
            history = open(rf"C:\MaCroS\{sender}\history-client.txt", 'a', encoding='utf-8')
            history.write(rmssg + f'⁝{self.inmsgindex}⁝{time.time()}⁝in' + '\n')
            history.close()
        elif rmssg == '':
            pass
        self.messages = []
        history = open(rf"C:\MaCroS\{sender}\history-client.txt", 'r', encoding='utf-8')
        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)
        self.messages.sort(key=lambda x: float(x[2]))
        history.close()
        self.ui.changed=True
