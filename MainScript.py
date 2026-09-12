# Startup script - compile here
chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'r', encoding='utf-8')
if chatlist.readlines() == []:
    chatlist.close()
    chatlist = open(r"C:\MaCroS\P2PT\config.txt", 'a', encoding='utf-8')
    chatlist.write('26.0.2.167')
    chatlist.write('\n')
    chatlist.write('Ϡ')
    chatlist.write('\n')
    chatlist.write('Saved Messages')
chatlist.close()

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

wind.mainloop()

########################################################################
