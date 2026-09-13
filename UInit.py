# circular imports suck
# ---------------------------------
from functools import partial
from tkinter import PhotoImage
# from tkinter import messagebox
import tkinter as win
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox
import sys
from pathlib import Path

class UI:

    def __init__(self, windo):
        from MemorySync import MemorySync
        from Networking import Networking

        self.memory = MemorySync(self)
        self.Net = Networking(self, self.memory)

        windo.geometry('800x800')
        self.window = windo
        windo.title('MaCroS A0.5.3')

        self.THEbg = '#EDE8FF'
        self.bgcol = '#dde0ff'
        self.glasscol = '#c9cdff'
        self.sbcol = '#dfd6ff'
        self.sbbg = '#A99BDB'
        #                                              ↓ Windows dependant ↓
        #self.button = [background, text, border, light theme color, dark theme color]
        self.button = ['#A3AAFF', '#000000','#A3A6CE', "#c9cdff", "#8f80c5"]

        self.chat=['localhost']
        self.chatlabel=['Saved messages']
        self.chatid=0
        self.nickname=''
        with open(r'C:\MaCroS\P2PT\config.txt') as nick:
            c=0
            for i in nick.readlines():
                if 'Í³' in i:
                    self.nickname=i.rstrip('Í³') + 'ͳ'

                else:
                    self.nickname = 'NoNameͳ'
                c+=1
        self.changed=False

        self.backg = win.Frame(windo, bg=self.THEbg)
        self.backg.pack(fill="both", expand=True)

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "UI.TButton",
            background=self.button[0],
            foreground=self.button[1],
            bordercolor=self.button[2],
            lightcolor=self.button[3],
            darkcolor=self.button[4],
            padding=5)
        style.map("UI.TButton",background=[("active", self.button[0]),("pressed", self.button[0])],foreground=[("active", self.button[1])])
        style.configure("Chat.TLabel", background=self.glasscol)
        superstyle = ttk.Style()
        superstyle.configure("Chat.Vertical.TScrollbar", background=self.sbcol, troughcolor=self.sbbg, arrowcolor=self.sbbg, lightcolor=self.glasscol, darkcolor=self.glasscol)

        self.sendbi = PhotoImage(file=str(rf"{self.resource_path('Images/sendbutton.png')}"))

        self.glass = win.Frame(self.backg, bg=self.glasscol, bd=1, relief="solid")
        self.sidebar = win.Frame(self.glass, bg=self.bgcol, relief='solid')
        self.sidebartop=win.Frame(self.sidebar, bg=self.bgcol)
        self.sidebarchats=win.Frame(self.sidebar, bg=self.bgcol)
        self.sidebarbottom = win.Frame(self.sidebar, bg=self.bgcol)

        self.topsidebardivider = win.Frame(self.sidebartop, height=2, bg='#888888')
        self.bottomsidebardivider = win.Frame(self.sidebarbottom, height=2, bg='#888888')
        self.sidebardivier = win.Frame(self.glass, width=2, bg="#888888")

        # So far unused
        self.popupmenu = win.Frame(self.glass, bg="#f8fbff")
        self.advanced_frame = win.Frame(self.glass, bg="#f8fbff")

        self.chatselfow = win.Frame(self.glass, bg=self.glasscol)
        self.chatwindow = win.Frame(self.glass, bg=self.glasscol)
        self.bottombar = win.Frame(self.chatwindow, bg=self.glasscol)

        self.chatcanvas = win.Canvas(self.chatwindow, bg=self.glasscol, highlightthickness=0)

        self.chatscroller = ttk.Scrollbar(self.chatwindow, orient='vertical', style="Chat.Vertical.TScrollbar", command=self.chatcanvas.yview)

        self.chatF = win.Frame(self.chatcanvas, bg=self.glasscol)

        self.chatcanvas.configure(yscrollcommand=self.chatscroller.set)

        self.message = ttk.Entry(self.bottombar, width=20)

        self.popupmenub = ttk.Button(self.chatselfow, text="Menu", command=self.popup, width=6)
        self.send = ttk.Button(self.bottombar,
                               image=self.sendbi,
                               width=3,
                               command=self.Net.SendNetworkTest)

        self.addchatip=ttk.Entry(self.sidebartop, width=25)
        self.addchatname=ttk.Entry(self.sidebartop, width=25)
        self.nicknameentry = ttk.Entry(self.sidebarbottom, width=25)

        self.nicknamedisplay = ttk.Label(self.sidebarbottom, text=self.nickname.rstrip('ͳ'), background=self.bgcol)
        self.chatiphint = ttk.Label(self.sidebartop, text='Chat IP:', background=self.bgcol)
        self.chatnamehint = ttk.Label(self.sidebartop, text='Chat name:', background=self.bgcol)
        self.addchat=ttk.Button(self.sidebartop, text='Add chat', command=self.CreateChat)
        self.nicknameupdate = ttk.Button(self.sidebarbottom, text='Update nickname', command=self.UpdateNickname)
        self.close = ttk.Button(self.popupmenu, text='✕', command=self.popupdestroy, width=3)
        self.updateipsetb = ttk.Button(self.advanced_frame, text='Update Host IP')
        self.debugbtn = ttk.Button(self.advanced_frame, text="Debug info")
        self.clearhst = ttk.Button(self.advanced_frame, text='Clear local chat history', command=self.memory.MemoryForgor)




        self.sidebartop.pack(side='top', fill='y', pady=5)

        self.chatiphint.pack(anchor='nw', padx=5)
        self.addchatip.pack(padx=5, pady=1)
        self.chatnamehint.pack(anchor='nw', padx=5)
        self.addchatname.pack(padx=5)
        self.addchat.pack(anchor='nw', padx=5, pady=5)
        self.topsidebardivider.pack(fill='x', padx=5, pady=5)

        self.sidebarchats.pack(side='top', fill='both', expand=True)

        self.bottomsidebardivider.pack(fill='x', padx=5, pady=5)
        self.nicknamedisplay.pack(pady=5)
        self.sidebarbottom.pack(side='bottom', fill='x')
        self.sidebar.pack(side='left', fill='y')
        self.sidebardivier.pack(side='left', fill='y')

        self.chatwindow.pack(side='right', fill='both', expand=True, pady=5)

        # Bottom input bar
        self.bottombar.pack(side='bottom', fill='x')

        self.message.pack(side='left', fill='x', expand=True, padx=10, pady=5)

        self.send.pack( side='right', padx=5, pady=5)

        # Scrollbar
        self.chatscroller.pack(side='right', fill='y')

        # Canvas
        self.chatcanvas.pack(side='left', fill='both', expand=True)

        # Messages frame inside canvas
        self.chatcanvas_window = self.chatcanvas.create_window((0, 0), anchor='nw', window=self.chatF)

        # Make the message frame as wide as the canvas
        self.chatcanvas.bind("<Configure>",lambda e: self.chatcanvas.itemconfigure(self.chatcanvas_window,width=e.width))

        # Update scrollbar region
        self.chatF.bind("<Configure>",lambda e: self.chatcanvas.configure(scrollregion=self.chatcanvas.bbox("all")) )
        self.close.pack(side='right', padx=5, pady=5)
        self.nicknameentry.pack()
        self.nicknameupdate.pack()
        self.inshadowtext = ''

    def NewMessage(self, msg, dir):
        message = ttk.Label(
            self.chatF,
            text=msg,
            style="Chat.TLabel",
            wraplength=500,
            justify='left'
        )

        if dir == 'out':
            message.pack(
                anchor='e',
                padx=10,
                pady=3
            )

        elif dir == 'in':
            message.pack(
                anchor='w',
                padx=10,
                pady=3
            )

    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).parent
        return base_path / relative_path

    def UpdateNickname(self):
        self.nickname = self.nicknameentry.get() + 'ͳ'
        self.nicknamedisplay.configure(text=self.nicknameentry.get())
        chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'w', encoding='utf-8')
        for i in self.chat:
            chatlist.write(i)
            chatlist.write('\n')
        chatlist.write('Ϡ')
        chatlist.write('\n')
        for i in self.chatlabel:
            chatlist.write(i)
            chatlist.write('\n')
        chatlist.write('Ϡ')
        chatlist.write('\n')
        chatlist.write(self.nickname)
        chatlist.close()
        self.nicknameentry.delete(0, win.END)


    def ButtonCreate(self, chat_id, chat_name):
        button = ttk.Button(self.sidebarchats, text=chat_name, command=lambda: self.OpenChat(chat_id))
        button.pack(fill="x", padx=5, pady=2)
        return button

    def UpdaterButtons(self):
        for i in range(len(self.chat)):
            self.ButtonCreate(self.chat[i], self.chatlabel[i])

    def OpenChat(self, chatid):
        for i in range(len(self.chat)):
            if self.chat[i] == chatid:
                self.chatid = i

        chatpath = Path(
            rf"C:\MaCroS\P2PT\H-C\{chatid}"
        )

        if not chatpath.exists():
            chatpath.mkdir()
            open(
                chatpath / 'history-client.txt',
                'a',
                encoding='utf-8'
            ).close()

        self.memory.IDDater()

        self.LoadMessages()

    def CreateChat(self):
        chatname=self.addchatname.get()
        chatip=self.addchatip.get()
        self.addchatip.delete('0', win.END)
        self.addchatname.delete('0', win.END)
        self.chat.append(chatip)
        self.chatlabel.append(chatname)
        self.ButtonCreate(chatip, chatname)
        self.UpdateChatlist()

    def UpdateChatlist(self):
        chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'w', encoding='utf-8')
        for i in self.chat:
            chatlist.write(i)
            chatlist.write('\n')
        chatlist.write('Ϡ')
        chatlist.write('\n')
        for i in self.chatlabel:
            chatlist.write(i)
            chatlist.write('\n')
        chatlist.close()

    def ReadChatList(self):
        c=0
        self.chat=[]
        self.chatlabel=[]
        chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'r', encoding='utf-8')

        chatlisttemp = chatlist.readlines()

        for i in chatlisttemp:
            i=i.rstrip('\n')
            if c==0 and 'Ϡ' not in i:
                self.chat.append(i)
            elif c==1 and 'Ϡ' not in i:
                self.chatlabel.append(i)
            elif c==2 and 'Ϡ' not in i:
                self.nickname=i
            if 'Ϡ' in i:
                c+=1

    def MenuInit(self):
        # Initializing the closing menu button

        # Packing said button in its place

        # Packing the Frames themselves
        self.debugbtn.pack(anchor="e", pady=5)
        self.updateipsetb.pack(side='bottom', anchor='e', pady=10)
        self.clearhst.pack(anchor='e', pady=5)
        self.advanced_frame.pack(side="bottom", anchor="e", padx=15, pady=15)
        self.popupmenu.pack(side="top", anchor="e", padx=10, pady=10)

    def popup(self):
        # Add items to the popup menu
        self.MenuInit()
        # Destroy the button to call the popup
        self.message.pack_forget()
        self.chatwindow.pack_forget()
        self.sidebar.pack_forget()
        self.chatwindow.pack_forget()
        # Reloading the popup menu button

    def popupdestroy(self):
        # Well... destroying the popup menu
        self.advanced_frame.pack_forget()
        self.popupmenu.pack_forget()
        self.sidebar.pack(side='left', anchor='nw', padx=5, pady=5, expand=True)
        self.chatwindow.pack(side='bottom', anchor='se', expand=True)
        # Reloading popupmenu
        self.mainmenuinit()

    def mainmenuinit(self):
        self.glass.pack(
            padx=30,
            pady=30,
            fill="both",
            expand=True
        )

        self.sidebar.pack(
            side='left',
            fill='y',
        )

        self.chatwindow.pack(
            side='right',
            fill='both',
            expand=True,
            pady=5
        )

    def LoadMessages(self):
        # Remove currently displayed messages
        for widget in self.chatF.winfo_children():
            widget.destroy()

        # Create every message
        for message in self.memory.messages:
            self.NewMessage(message[0], message[3])

        # Scroll to bottom
        self.chatcanvas.update_idletasks()
        self.chatcanvas.yview_moveto(1)

    def UpdateIncomingMessages(self):
        if self.changed:
            self.LoadMessages()
            self.changed=False
        self.window.after(100, self.UpdateIncomingMessages)

    def UpdateChatListIncoming(self):
        if self.Net.receivedmsg==1:
            messagebox.showinfo('Notification', 'New Message!')
            self.ButtonCreate(self.Net.sender, self.memory.sendername)
            self.chat.append(self.Net.sender)
            self.chatlabel.append(self.memory.sendername)
            self.OpenChat(self.Net.sender)
            self.UpdateChatlist()
            self.Net.receivedmsg=0
        self.window.after(100, self.UpdateChatListIncoming)