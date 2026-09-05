from UInit import UI
import tkinter


class MemorySync:
    def __init__(self):
        self.namespace = 'MemorySync'
        self.msgindex = 0
        self.inmsgindex = 0

    def MemoryStorageDaterIn(self):
        self.inmsgindex += 1

    def MemoryStorageDater(self):
        self.msgindex += 1

    def MemoryStorageUpdater(self):
        messageinput = UI.message.get()
        if messageinput != '':
            history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'a', encoding='utf-8')
            self.MemoryStorageDater()
            history.write(UI.message.get() + f'⁝{self.msgindex}' + '\n')
            history.close()
        history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'r', encoding='utf-8')
        actualhistorylines = history.readlines()
        for i in actualhistorylines:
            for j in i:
                if j != '⁝':
                    UI.windowtext += j
                if j == '⁝':
                    break
            UI.windowtext += '\n'
        UI.previousmessages.configure(text=UI.windowtext)
        UI.previousmessages.pack(side='bottom', anchor='e')
        history.close()
        UI.message.delete('0', tkinter.END)

    def MemoryForgor(self):
        history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'w')
        history.write('\n')
        history.close()

    def MemoryReceiver(self, rmssg):
        if rmssg != '':
            history = open(r"C:\MaCroS\P2PT\H-C\history-client-in.txt", 'a', encoding='utf-8')
            self.MemoryStorageDaterIn()
            history.write(rmssg + f'⁝{self.inmsgindex}' + '\n')
            history.close()
        elif rmssg == '':
            pass
