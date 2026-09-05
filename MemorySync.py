import time

import tkinter


class MemorySync:
    msgindex = 0
    inmsgindex = 0

    def __init__(self, ui):
        self.messages = []
        self.namespace = 'MemorySync'
        self.ui = ui

    def IDDater(self):
        self.messages = []
        history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'r', encoding='utf-8')
        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)
        self.messages.sort(key=lambda x: float(x[2]))
        history.close()

    def MemoryStorageDaterIn(self):
        self.inmsgindex += 1

    def MemoryStorageDater(self):
        self.msgindex += 1

    def MemoryStorageUpdater(self):
        self.ui.windowtext = ''
        self.messageinput = self.ui.message.get()
        if self.messageinput != '':
            history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'a', encoding='utf-8')
            history.write(self.messageinput + f'⁝{self.msgindex}⁝{time.time()}⁝out' + '\n')
            history.close()
            self.ui.message.delete('0', tkinter.END)
        self.messages = []
        history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'r', encoding='utf-8')
        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)
        self.messages.sort(key=lambda x: float(x[2]))
        history.close()

    def MemoryForgor(self):
        history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'w')
        history.close()

    def MemoryReceiver(self, rmssg):
        rmssg = rmssg.decode('utf-8')
        if rmssg != '':
            self.ui.inshadowtext = 123123
            self.inmsgindex += 1
            history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'a', encoding='utf-8')
            history.write(rmssg + f'⁝{self.msgindex}⁝{time.time()}⁝in' + '\n')
            history.close()
        elif rmssg == '':
            pass
        self.messages = []
        history = open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'r', encoding='utf-8')
        for line in history:
            message = line.rstrip('\n').split('⁝')
            message[2] = float(message[2])
            self.messages.append(message)
        self.messages.sort(key=lambda x: float(x[2]))
        history.close()
