# Startup script - compile here with:
# python -m PyInstaller --onedir --onefile --windowed --add-data "Images;Images" MaCroS.py


structure = r'C:\MaCroS'

# Imports

import sys
import tkinter as win
from tkinter import ttk
import time
import threading
import socket
from pathlib import Path
import ctypes
import sys

if not Path.exists(r'C:\MaCroS'):
    Path.mkdir(structure)
    if not Path.exists(rf'{structure}\P2PT'):
        Path.mkdir(rf'{structure}\P2PT')
        if not Path.exists(rf'{structure}\P2PT\H-C'):
            Path.mkdir(rf'{structure}\P2PT\H-C')
            open(rf'{structure}\P2PT\config.txt', 'a').close()
if Path.is_file(rf'{structure}\P2PT\config.txt'):
    chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'r', encoding='utf-8')
    if chatlist.readlines() == []:
        chatlist.close()
        chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'a', encoding='utf-8')
        chatlist.write('localhost')
        chatlist.write('\n')
        chatlist.write('Ϡ')
        chatlist.write('\n')
        chatlist.write('Saved Messages')
    chatlist.close()


# Class definition

from UInit import UI
from MemorySync import MemorySync
from Networking import Networking
# from Anim import Anim
# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Networking.ReceiveNetworkTest(Networking)

wind = win.Tk()

ui = UI(wind)


ui.UpdateChatListIncoming()
ui.ReadChatList()
ui.mainmenuinit()
ui.memory.IDDater()
ui.LoadMessages()
ui.UpdateIncomingMessages()
ui.UpdaterButtons()
thread = threading.Thread(target=ui.Net.ReceiveNetworkTest, daemon=True)
thread.start()
thread = threading.Thread(target=ui.UpdateOnline(), daemon=True)
thread.start()
thread = threading.Thread(target=ui.UpdateOnlineUI(), daemon=True)
thread.start()
#thread=threading.Thread(target=ui.MinimizeToTray())

wind.mainloop()

########################################################################
