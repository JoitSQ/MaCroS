from UInit import UI
import tkinter

class MemorySync():
    def __init__(self):
        self.namespace = 'MemorySync'
        self.msgindex = 0

    def MemoryStorageDate(self):
        # Being a smart ass (not) i am i will make this dependant NOT on IDs but on date
        self.msgindex += 1
        # nvm i caved in and made it on IDs

    def MemoryStorageUpdater(self):
        messageinput = UI.message.get()
        if messageinput != '':
            history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'a', encoding='utf-8')
            self.MemoryStorageDate()
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

    # def clearchat(self):
    #   history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'w')
    #  history.write('\n')
    # history.close()
    # UI.clearhst.configure(text='Done!')
    def MemoryForgor(self):
        history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'w')
        history.write('\n')
        history.close()
        UI.clearhst.configure(text='Done!')
