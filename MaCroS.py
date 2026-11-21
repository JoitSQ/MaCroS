# Startup script - compile here with:
# python -m PyInstaller --onedir --onefile --windowed --add-data "Images;Images" MaCroS.py




# Imports

import tkinter as win
import threading


# Class definition

from UInit import UI
from Configparser import Config


# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Networking.ReceiveNetworkTest(Networking)

wind = win.Tk()

ui = UI(wind)
config = Config(ui)
config.first_boot()



ui.chatlist_update_incoming()
config.chatlist_read()
ui.mainmenuinit()
ui.memory.IDDater()
ui.messages_load()
ui.incoming_updater()
ui.button_updater()

thread = threading.Thread(target=ui.Net.network_receiver, daemon=True)
thread.start()

thread = threading.Thread(target=ui.online_updater(), daemon=True)
thread.start()

#thread=threading.Thread(target=ui.MinimizeToTray())

wind.mainloop()

########################################################################
