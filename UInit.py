# circular imports suck
# ---------------------------------
from tkinter import PhotoImage
# from tkinter import messagebox
import tkinter as win
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path


class UI:

    def __init__(self, windo):
        from MemorySync import MemorySync
        from Networking import Networking
        from Security import Security
        from Configparser import Config
        from BackgroundWorker import BG



        self.state = 'b'
        self.vernumber = '0.6.4'
        self.title = 'MaCroS ' + self.state + self.vernumber

        windo.geometry('800x800')
        self.window = windo
        windo.title(self.title)

        self.bg = BG(self)
        self.config = Config(self)
        self.memory = MemorySync(self)
        self.security = Security(self)
        self.Net = Networking(self, self.memory)

        self.THEbg = '#EDE8FF'
        self.bgcol = '#dde0ff'
        self.glasscol = '#c9cdff'
        self.sbcol = '#dfd6ff'
        self.sbbg = '#A99BDB'
        self.green = '#009E00'
        self.red = '#E80022'

        #                                              ↓ Windows dependant ↓
        #self.button = [background, text, border, light theme color, dark theme color]
        self.button = ['#A3AAFF', '#000000','#A3A6CE', "#c9cdff", "#8f80c5"]

        self.chat = ['Myself']
        self.chatlabel = ['Saved messages']
        self.chatid = 0
        self.onlined = False
        self.trayed=False

        self.changed=False

        self.backg = win.Frame(windo, bg=self.THEbg)
        self.backg.pack(fill="both", expand=True)

        style = ttk.Style()

        style.theme_use("clam")

        style.configure('Online.TLabel', background=self.glasscol, foreground = self.green)
        style.configure('Offline.TLabel', background=self.glasscol, foreground = self.red)
        style.configure(
            "UI.TButton",
            background=self.button[0],
            foreground=self.button[1],
            bordercolor=self.button[2],
            lightcolor=self.button[3],
            darkcolor=self.button[4],
            padding=5)

        style.map("UI.TButton",background=[("active", self.button[0]),
                                           ("pressed", self.button[0])],
                                        foreground=[("active", self.button[1])])

        style.configure("Chat.TLabel", background=self.glasscol)

        style.configure("Chat.Vertical.TScrollbar", background=self.sbcol,
                        troughcolor=self.sbbg, arrowcolor=self.sbbg,
                        lightcolor=self.glasscol, darkcolor=self.glasscol)


        self.sendbi = PhotoImage(file=str(rf"{self.config.resource_path('Images/sendbutton.png')}"))


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

        self.message = win.Text(self.bottombar, width=2, height=3)

        self.popupmenub = ttk.Button(self.chatselfow, text="Menu", command=self.popup, width=6)


        self.send = ttk.Button(self.bottombar,
                               image=self.sendbi,
                               width=3,
                               command=self.Net.send_stop)

        self.addchatip=ttk.Entry(self.sidebartop, width=25)

        self.addchatname=ttk.Entry(self.sidebartop, width=25)
        self.nicknameentry = ttk.Entry(self.sidebarbottom, width=25)

        self.username = self.config.read_username() if Path(r'C:\MaCroS\config.txt').exists() else ''
        self.chatuser = 'Username:'
        self.usernamehint = 'Your Username:'
        self.usernameupdate = 'Update Username'
        self.testing = 'WIP'
        self.useronline = 'User Online!'
        self.useroffline = 'User Offline!'


        self.securitywarn = ttk.Label(self.chatcanvas, text=self.testing, background=self.glasscol)
        self.IsOnlineText = ttk.Label(self.bottombar, text='', background = self.glasscol, style='Online.TLabel')
        self.nicknamedisplay = ttk.Label(self.sidebarbottom, text=self.username.rstrip('ͳ'), background=self.bgcol)

        # self.chatiphint = ttk.Label(self.sidebartop, text='Chat IP:', background=self.bgcol)

        self.chatnamehint = ttk.Label(self.sidebartop, text=self.chatuser, background=self.bgcol)
        self.addchat=ttk.Button(self.sidebartop, text='Add chat', command=self.chat_creator)
        self.nicknameupdate = ttk.Button(self.sidebarbottom, text=self.usernameupdate, command=self.config.update_username)

        self.close = ttk.Button(self.popupmenu, text='✕', command=self.popupdestroy, width=3)
        self.updateipsetb = ttk.Button(self.advanced_frame, text='Update Host IP')
        self.debugbtn = ttk.Button(self.advanced_frame, text="Debug info")
        self.clearhst = ttk.Button(self.advanced_frame, text='Clear local chat history', command=self.memory.MemoryForgor)




        self.sidebartop.pack(side='top', fill='y', pady=5)

        # self.chatiphint.pack(anchor='nw', padx=5)
        # self.addchatip.pack(padx=5, pady=1)

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

        self.IsOnlineText.pack(padx=5)

        self.message.pack(side='left', fill='x', expand=True, padx=10, pady=5)

        self.send.pack( side='right', padx=5, pady=5)

        self.securitywarn.pack(side='bottom', anchor='s', padx=5, pady=5)
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
        self.nicknameupdate.pack(pady=5)
        self.inshadowtext = ''


    def horrible_wrong(self, error):
        messagebox.showerror('Uh-oh!', f'Please look for a github issue with following code: {self.config.error_parse(error)}')


    def message_new(self, msg, direction):
        message = ttk.Label(
            self.chatF,
            text=msg,
            style="Chat.TLabel",
            wraplength=500,
            justify='left'
        )

        if direction == 'out':
            message.pack(
                anchor='e',
                padx=10,
                pady=3
            )

        elif direction == 'in':
            message.pack(
                anchor='w',
                padx=10,
                pady=3
            )


    def button_creator(self, chat_id, chat_name):
        button = ttk.Button(self.sidebarchats, text=f'{chat_name}', command=lambda: self.config.chat_open(chat_id))
        button.pack(fill="x", padx=5, pady=2)
        return button


    def button_updater(self):
        for i in range(len(self.chat)):
            self.button_creator(self.chat[i], self.chatlabel[i])


    def chat_creator(self):
        chatname=self.addchatname.get()
        # chatip=self.addchatip.get()
        self.addchatip.delete('0', win.END)
        self.addchatname.delete('0', win.END)
        self.chat.append(chatname)
        self.chatlabel.append(chatname)
        self.button_creator(chatname, chatname)
        self.config.update_nameplates()


    # Deprecated
    def init_menu(self):

        self.debugbtn.pack(anchor="e", pady=5)
        self.updateipsetb.pack(side='bottom', anchor='e', pady=10)
        self.clearhst.pack(anchor='e', pady=5)
        self.advanced_frame.pack(side="bottom", anchor="e", padx=15, pady=15)
        self.popupmenu.pack(side="top", anchor="e", padx=10, pady=10)

    # Deprecated
    def popup(self):
        # Add items to the popup menu
        self.init_menu()
        # Destroy the button to call the popup
        self.message.pack_forget()
        self.chatwindow.pack_forget()
        self.sidebar.pack_forget()
        self.chatwindow.pack_forget()
        # Reloading the popup menu button

    # Deprecated
    def popupdestroy(self):
        # Well... destroying the popup menu
        self.advanced_frame.pack_forget()
        self.popupmenu.pack_forget()
        self.sidebar.pack(side='left', anchor='nw', padx=5, pady=5, expand=True)
        self.chatwindow.pack(side='bottom', anchor='se', expand=True)
        # Reloading popupmenu
        self.mainmenuinit()

    # Deprecated
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


    def messages_load(self):

        self.chatcanvas.yview_moveto(0)
        # Remove currently displayed messages
        for widget in self.chatF.winfo_children():
            widget.destroy()

        # Create every message
        for message in self.memory.messages:
            self.message_new(message[0], message[3])

        # Scroll to bottom
        self.chatcanvas.update_idletasks()
        self.chatcanvas.configure(scrollregion=self.chatcanvas.bbox("all"))
        self.chatcanvas.yview_moveto(1)


    def incoming_updater(self):
        if self.changed:
            self.messages_load()

            self.changed=False
        self.window.after(100, self.incoming_updater)

    def chatlist_update_incoming(self):
        if self.Net.receivedmsg and self.Net.sender not in self.chat:

            self.button_creator(self.Net.sender, self.memory.sendername)
            self.chat.append(self.Net.sender)
            self.chatlabel.append(self.memory.sendername)
            # self.config.OpenChat(self.Net.sender)
            self.config.update_nameplates()
            self.Net.receivedmsg = False
        self.window.after(100, self.chatlist_update_incoming)


    def online_updater(self):
        self.onlined = True if self.Net.is_online_networking(self.chat[self.chatid]) else False
        if self.chat[self.chatid]==self.username:
            self.IsOnlineText.configure(text='', style='Offline.TLabel')
            self.securitywarn.configure(text='')
        elif self.onlined:
            self.IsOnlineText.configure(text=self.useronline, style='Online.TLabel')
        elif not self.onlined:
            self.IsOnlineText.configure(text=self.useroffline, style='Offline.TLabel')
        self.window.after(10000, self.online_updater)