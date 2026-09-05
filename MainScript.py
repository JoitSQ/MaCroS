# Startup script - compile here

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
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
# thread = threading.Thread(target=Networking().ReceiveNetworkTest())
# thread.start()
Networking.ReceiveNetworkTest(Networking)

wind = win.Tk()

ui = UI(wind)

ui.mainmenuinit()

wind.mainloop()

########################################################################
