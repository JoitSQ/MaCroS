import tkinter as win
import sys
from pathlib import Path


class Config:

    def __init__(self, ui):
        from MemorySync import MemorySync

        self.ui = ui
        self.memory = MemorySync(ui)
        self.structure = r'C:\MaCroS'
        self.config_file = rf'{self.structure}\config.txt'


    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).parent
        return base_path / relative_path


    def first_boot(self):
        # Pathing skeleton
        if not Path.exists(self.structure):
            Path.mkdir(self.structure)
            open(self.config_file, 'a').close()

        # Config skeleton

        if Path.is_file(self.config_file):
            if not open(self.config_file, 'r', encoding='utf-8').readlines():
                chatlist = open(self.config_file, 'w', encoding = 'utf-8')
                chatlist.write('[@IPSets]\n')

                chatlist.write('Myself\n')

                chatlist.write('[@NamePlates]\n')

                chatlist.write('Saved messages\n')

                chatlist.write(f'[@UserName]\nNoName')

                chatlist.close()
        self.booted = True


    def chatlist_read(self):
        c=0
        self.ui.chat=[]
        self.ui.chatlabel=[]
        chatlist = open(r"C:\MaCroS\config.txt", 'r', encoding='utf-8')

        chatlisttemp = chatlist.readlines()

        for i in chatlisttemp:
            i=i.rstrip('\n')
            if c==0 and '[@' not in i:
                self.ui.chat.append(i)
            elif c==1 and '[@' not in i:
                self.ui.chatlabel.append(i)
            if '[@' in i and i!='[@IPSets]':
                c+=1
            # print(i, '; ', self.ui.chat, '; ', self.ui.chatlabel)


    def chat_open(self, chatid):
        for i in range(len(self.ui.chat)):
            if self.ui.chat[i] == chatid:
                self.ui.chatid = i

        chatpath = Path(
            rf"C:\MaCroS\{chatid}"
        )

        if not chatpath.exists():
            chatpath.mkdir()
            open(
                chatpath / 'history-client.txt',
                'a',
                encoding='utf-8'
            ).close()

        self.memory.IDDater()

        self.ui.messages_load()


    def read_username(self):
        with open(self.config_file) as nick:
            tempconfig = nick.readlines()
            for i in range(len(tempconfig)):
                if '[@UserName]' in tempconfig[i]:
                    return tempconfig[i+1]
            return 'NoName'


    def update_username(self):

        self.ui.username = self.ui.nicknameentry.get()

        self.ui.nicknamedisplay.configure(text=self.ui.username)

        chatlist = open(self.config_file, 'w', encoding='utf-8')

        chatlist.write('[@IPSets]\n')

        for i in self.ui.chat:
            chatlist.write(i)
            chatlist.write('\n')

        chatlist.write('[@NamePlates]\n')

        for i in self.ui.chatlabel:
            chatlist.write(f'{i}\n')

        chatlist.write(f'[@UserName]\n{self.ui.username}')

        chatlist.close()

        self.ui.nicknameentry.delete(0, win.END)


    def update_nameplates(self):
        chatlist = open(self.config_file, 'w', encoding='utf-8')

        chatlist.write('[@IPSets]\n')

        for i in self.ui.chat:
            chatlist.write(i)
            chatlist.write('\n')

        chatlist.write('[@NamePlates]\n')

        for i in self.ui.chatlabel:
            chatlist.write(f'{i}\n')

        chatlist.write(f'[@UserName]\n{self.ui.username}')

        chatlist.close()


    def error_parse(self, err):
        if err == 'Networking.HostForbidden':
            return '0xc000H1'
        if err == 'Networking.Timeout':
            return '0xc000R1'
        if err == 'Networking.BadPacket':
            return '0xc000U1'
        if err == 'Networking.Interrupt':
            return '0xc000N1'
        if err == 'Memory.NoAccessPermission':
            return '0xc000P1'
        if err == 'Memory.NoPath':
            return '0xc000U2'
        if err == 'Security.EncryptionFailed':
            return '0xc000C1'
        if err == 'Config.BadConfig':
            return '0xc000U3'
        if err == 'Thread.Terminated':
            return '0xc000T1'
        if err == 'UI.ButtonFailed':
            return '0xc000B1'
        if err == 'UI.ChatOverflow':
            return '0xc000B2'
        else:
            return '1xc1UNb'
