from Networking import *
from MemorySync import *
from tkinter import PhotoImage
# from tkinter import messagebox
import tkinter as win
from tkinter import ttk


class UI():

    def __init__(self):
        self.namespace = 'UI'
    #djusklgfkldjhgjklfdhgjklfdhkjghfjkdhjkgfhdk

    def FirstInit(self):
        self.geometry('800x800')

        self.title('messenger duh')

        self.bg = win.Frame(self, bg="#dfefff")

        self.text = win.Label(self.bg, bg="#dfefff", text='initializing')
        self.error = win.Label(self.bg, bg="#dfefff")
        self.text.pack(anchor='center', expand=True)
        self.error.pack(anchor='center', expand=True)
        self.bg.pack(fill="both", expand=True)

        self.glass = win.Frame(self.bg, bg="#f8fbff", bd=1, relief="solid")

        self.advanced_frame = win.Frame(self.glass, bg="#f8fbff")

        self.bFrame1 = win.Frame(self.glass)

        # Further first stage selfow management
        self.sendbi = PhotoImage(file=r'Images/sendbutton.png')
        # Loading some variables for ts to be alive
        self.popupmenu = win.Frame(self.glass, bg="#f8fbff")

        self.sidebar = win.Frame(self.glass, bg='#dbeaff')
        self.popupmenub = ttk.Button(self.sidebar, text="Menu", command=UI.popup, width=6)
        # chat1=ttk.Button(sidebar, text=contact[0])
        self.chatselfow = win.Frame(self.glass, bg="#f8fbff")
        self.message = ttk.Entry(self.chatselfow, width=200)
        self.send = ttk.Button(self.chatselfow, image=self.sendbi, width=5, command=MemorySync.MemoryStorageUpdater)
        self.sidebar = win.Frame(self.glass, bg='#dbeaff')
        self.chatwindow = win.Frame(self.glass, bg="#f8fbff")
        self.message = ttk.Entry(self.chatwindow, width=200)
        self.send = ttk.Button(self.chatwindow, image=self.sendbi, width=5, command=MemorySync.MemoryStorageUpdater)
        self.previousmessages = ttk.Label()
        self.windowtext = ''

        self.updateipsetb = ttk.Button(self.advanced_frame, text="Update ipset", command=Networking.IPSetinit)
        self.debugbtn = ttk.Button(self.advanced_frame, text="Debug info")
        self.clearhst = ttk.Button(self.advanced_frame, text='Clear local chat history',
                                   command=MemorySync.MemoryForgor)

    def MenuInit(self):
        # Initializing the closing menu button
        self.close = ttk.Button(self.popupmenu, text='✕', command=UI.popupdestroy, width=3)

        # Packing said button in its place
        self.close.pack(side='right', padx=5, pady=5)

        # Packing the Frames themselves
        self.advanced_frame.pack(side="bottom", anchor="e", padx=15, pady=15)
        self.popupmenu.pack(side="top", anchor="e", padx=10, pady=10)

    def popup(self):
        # Add items to the popup menu
        UI.MenuInit(self)
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
        self.sidebar.pack(side='left', anchor='ne', expand=True, pady=5)
        self.send.pack(side='left', anchor='sw', expand=False)
        self.message.pack(side='bottom', anchor='sw', pady=5, padx=10)
        self.chatwindow.pack(side='bottom', anchor='se', expand=True)
        self.popupmenub.pack(side='top', anchor='nw', expand=True)
