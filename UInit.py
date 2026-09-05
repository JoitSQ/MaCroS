# circular imports suck
# ---------------------------------
from functools import partial
from tkinter import PhotoImage
# from tkinter import messagebox
import tkinter as win
from tkinter import ttk


class UI:

    def __init__(self, windo):
        from MemorySync import MemorySync
        from Networking import Networking
        windo.geometry('800x800')
        self.memory = MemorySync(self)
        self.Networking = Networking(self, self.memory)
        self.window = windo
        windo.title('messenger duh')

        self.backg = win.Frame(windo, bg="#dfefff")

        # self.text = win.Label(self.backg, bg="#dfefff", text='initializing')
        # self.error = win.Label(self.backg, bg="#dfefff")
        # self.text.pack(anchor='center', expand=True)
        # self.error.pack(anchor='center', expand=True)
        self.backg.pack(fill="both", expand=True)

        self.glass = win.Frame(self.backg, bg="#f8fbff", bd=1, relief="solid")
        self.sidebar = win.Frame(self.glass, bg='#dbeaff')

        self.bFrame1 = win.Frame(self.glass)

        # Further first stage selfow management
        self.sendbi = PhotoImage(file=r'Images/sendbutton.png')
        # Loading some variables for ts to be alive
        self.popupmenu = win.Frame(self.glass, bg="#f8fbff")
        self.advanced_frame = win.Frame(self.glass, bg="#f8fbff")

        self.sidebar = win.Frame(self.glass, bg='#dbeaff')
        self.popupmenub = ttk.Button(self.sidebar, text="Menu", command=self.popup, width=6)
        # chat1=ttk.Button(sidebar, text=contact[0])
        self.chatselfow = win.Frame(self.glass, bg="#f8fbff")
        style = ttk.Style()
        style.configure("Chat.TLabel", background='#f8fbff')
        self.chatwindow = win.Frame(self.glass, bg="#f8fbff")
        self.message = ttk.Entry(self.chatwindow, width=200)
        self.send = ttk.Button(self.chatwindow,
                               image=self.sendbi,
                               width=5,
                               command=self.Networking.SendNetworkTest)
        self.row = ttk.Frame(self.chatwindow)
        self.previousmessagesout = ttk.Label(self.row, style="Chat.TLabel")
        self.windowtext = ''

        self.previousmessagesin = ttk.Label(self.row, style="Chat.TLabel")
        self.inwindowtext = ''

        self.row.columnconfigure(0, weight=1)
        self.row.columnconfigure(1, weight=1)

        self.previousmessagesout.grid(row=0, column=1, sticky='e')
        self.previousmessagesin.grid(row=0, column=0, sticky='w')
        self.send.grid(row=1, column=0, sticky='s')
        # self.send.grid(row=1, column=1, sticky='s')
        self.close = ttk.Button(self.popupmenu, text='✕', command=self.popupdestroy, width=3)

        self.updateipsetb = ttk.Button(self.advanced_frame, text='Update Host IP')
        self.debugbtn = ttk.Button(self.advanced_frame, text="Debug info")
        self.clearhst = ttk.Button(self.advanced_frame, text='Clear local chat history',
                                   command=self.memory.MemoryForgor)
        self.sidebar.pack(side='left', anchor='ne', expand=True, pady=5)
        self.send.pack(side='left', anchor='sw', expand=False)
        self.message.pack(side='bottom', anchor='sw', pady=5, padx=10)
        self.chatwindow.pack(side='bottom', anchor='se', expand=True)
        self.popupmenub.pack(side='top', anchor='nw', expand=True)
        self.close.pack(side='right', padx=5, pady=5)
        self.row.pack(fill='x')
        self.inshadowtext = ''
        # self.glass.pack(padx=30, pady=30, fill="both", expand=True)


    def FirstInit(self, windo):
        pass


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
        self.send.pack_forget()
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
        self.send.pack(side='left', anchor='sw', expand=False)
        self.message.pack(side='bottom', anchor='sw', pady=5, padx=10)
        # Reloading popupmenu
        self.mainmenuinit()

    def mainmenuinit(self):
        self.glass.pack(padx=30, pady=30, fill="both", expand=True)
        self.sidebar.pack(side='left', anchor='ne', expand=True, pady=5)
        self.memory.MemoryStorageUpdater()
        self.send.pack(side='left', anchor='sw', expand=False)
        self.message.pack(side='bottom', anchor='sw', pady=5, padx=10)
        self.chatwindow.pack(side='bottom', anchor='se', expand=True)
        self.popupmenub.pack(side='top', anchor='nw', expand=True)

    def UpdateIncomingMessages(self):
        if self.inshadowtext != self.inwindowtext or self.memory.messageinput != '':
            self.windowtext = ''
            self.inwindowtext = ''
            for i in self.memory.messages:
                if i[3] == 'out':
                    self.windowtext += i[0]
                    self.windowtext += '\n'
                    self.inwindowtext += '\n'
                if i[3] == 'in':
                    self.inwindowtext += i[0]
                    self.inwindowtext += '\n'
                    self.windowtext += '\n'
            self.previousmessagesout.configure(text=self.windowtext)
            self.previousmessagesin.configure(text=self.inwindowtext)
            self.memory.messageinput = ''
            self.inshadowtext = self.inwindowtext
        self.window.after(100, self.UpdateIncomingMessages)
