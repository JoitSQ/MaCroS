# Startup script - compile here
open(r"C:\MaCroS\P2PT\H-C\history-client.txt", 'a', encoding='utf-8')

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

ui.mainmenuinit()
ui.memory.IDDater()
ui.memory.MemoryStorageUpdater()
ui.UpdateIncomingMessages()

thread = threading.Thread(target=ui.Networking.ReceiveNetworkTest, daemon=True)
thread.start()

wind.mainloop()

########################################################################
