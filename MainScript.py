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

from UInit import *
from MemorySync import *
from Networking import *
from Anim import Anim

wind = win.Tk()

UI.FirstInit(wind)

Anim.fade(wind, wind)

wind.mainloop()

########################################################################


# DEPRECATED FILE REMAINS - KEEP OUT OF THIS NIGHTMARE FUEL
'''
# okay now how tf do i connect to internet here
import sys
import tkinter as win
from tkinter import ttk
import time
import calendar
import zoneinfo
import datetime
import threading
import socket
from tkinter import PhotoImage
from tkinter import messagebox
from pathlib import Path
import ctypes
import sys

# Apply admin privileges

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    msg = messagebox.showerror('An exception has occurred', 'Please rerun this program with admin privileges. ')
    #sys.exit()




# Window init

wind=win.Tk()

wind.geometry('800x800')

wind.title('messenger duh')

bg = win.Frame(wind, bg="#dfefff")

text = win.Label(bg, bg="#dfefff", text='initializing')
error = win.Label(bg, bg="#dfefff")
text.pack(anchor='center', expand=True)
error.pack(anchor='center', expand=True)
bg.pack(fill="both", expand=True)

glass = win.Frame(bg, bg="#f8fbff", bd=1, relief="solid")

advanced_frame = win.Frame(glass, bg="#f8fbff")

bFrame1=win.Frame(glass)

# Further first stage window management
sendbi=PhotoImage(file=r'Images/sendbutton.png')
# Loading some variables for ts to be alive
popupmenu = win.Frame(glass, bg="#f8fbff")

# Finalizing fist stage prep for window


# Loading IP set
# This only works for ONE IP Adress and ONE Port placed consecutively on different lines
# in a text file mentioned in further code
def IPSetGlobalFetch():
    #Define IP Adress and port
    with open(r"C:\MaCroS\P2PT\H-C\ipset.txt", 'x') as ipset:
        ipset.write(input("Please enter your OWN IPv4 adress. It can be accessed by typing 'ipconfig' in command prompt and looking at your active connection method (e.g. Ethernet adapter). \n"))
        ipset.write('\n' + ' ')
    with open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'x') as history:
        pass
    warning=messagebox.showinfo('Important', 'Please reopen the application. This is needed to get rid of this useless console window. Have a nice chat!')


if Path(r"C:\MaCroS\P2PT\H-C\ipset.txt").exists():
    pass
elif not Path(r"C:\MaCroS\P2PT\H-C").exists():
    Path.mkdir(Path("C:/MaCroS"), exist_ok=True)
    Path.mkdir(Path("C:/MaCroS/P2PT"), exist_ok=True)
    Path.mkdir(Path("C:/MaCroS/P2PT/H-C"), exist_ok=True)
    IPSetGlobalFetch()
    PORT = 54886
    exit()
PORT=54886
if Path(r"C:\MaCroS\config.txt").exists():
    pass
elif not Path(r"C:\MaCroS\config.txt").exists():
    with open(r"C:\MaCroS\config.txt", 'x') as config:
        config.write('0\n')
        config.write('1\n')
with open(r"C:\MaCroS\config.txt", 'r') as config:
    contactnum=config.readline(1)
    print(contactnum)
    int(contactnum)
    print(contactnum)
int(contactnum)

TARGET_HOST=[]
TARGET_PORT=54886
HOST=''

# Broken for now, will fix tmrw
def IPSetinit():
    global target_host, contactnum, HOST
    target_host = ''
    int(contactnum)
    with open(r"C:\MaCroS\P2PT\H-C\ipset.txt", 'r') as ipset:
        ippp=ipset.readlines()
        for i in range(len(ippp)):
            if i==0:
                host=ippp[i]
            else:
                TARGET_HOST.append(ippp[i])
    for i in host:
        if i!='\n':
            HOST+=i

IPSetinit()
print(HOST)
print(TARGET_HOST)

# IPSet loaded


# Loading variables for this shit to work properly
counter=1
connected=0
sendd=0

# In case i need to deliver updates here
def sendS():
    global sendd
    sendd=1


# Useless shit for now, doesn't get invoked ANYWHERE
# Connecting to host
def actualconnect():
    global connected, target_host, target_port
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Set a timeout for the connection attempt
            client_socket.settimeout(5.0)

            # Connect to the server
            client_socket.connect((target_host, int(target_port)))
            connected=1
            # We connected!!

            # Communicate with server to ensure stability
            message = "Hello, server!"
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)

            # I know everything went smooth because these next lines are for catching errors
    # If any socket errors occur, display them
    except socket.error as e:
        connected=0
        error.configure(text=e)

    # If any exceptions occur, display them
    except Exception as e:
        connected=0
        error.configure(text=e)

        # At this point, if code before fails this program will not function without restart, I believe


# Be a menace and make them wait 2 seconds before actually booting up
def connecttext():
    global connected, sendd
    time.sleep(2)
    error.configure(text='')
    text.configure(text='Success!')

    # Let the user read the text, 1 second should be enough
    time.sleep(1)

    # Initiate actual functionality of program
    start_fade()
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    opp+=data
                if sendd==1:
                    s.send(messageinput)
                    sendd=0

# old code remains

    # KILL. THREAD.

    # sys.exit()
    # I hate this line in particular because this means what? This means that I decided to kill the thread
    # BY FORCEFULLY SHUTTING IT DOWN
    # I have no other way to do so, and that is quite unfortunate, let me explain why
    # The Threading system in Python doesn't natively support something stupid like this
    # The said action can cause memory leaks and instability in program's functionality
    # I tried some alternatives but shit failed miserably, so I don't have any
    # This is why I HEAVILY recommend getting the fuck away from this line and never question it
    # Because it works, just like intended, so PLEASE DON'T TRY TO INTERFERE THIS WILL BREAK SHIT


# Start a thread above, connecting alongside mainloop
def start_task():
    global conthread
    conthread = threading.Thread(target=connecttext)
    conthread.start()
    # I also heavily recommend not touching shit here either
    # But in contrast to killing threads, I have no fucking idea how this works
    # So just don't touch it as long as shit works


# Start fading the window, create new thread for it to work alongside mainloop
def start_fade():
    thread = threading.Thread(target=fade)
    thread.start()


# Start the actual fade
def fade():
    global counter
    # Check if alpha counter is above zero
    while counter>0:

        # If is - destroy shit
        text.destroy()
        error.destroy()

        # Sleeping for this to be slower than instant
        time.sleep(.03)
        # ...and lower opacity counter
        counter-=0.05
        # Update window's opacity
        wind.attributes('-alpha', counter)
        # Repeat
        fade()
        # If counter reaches zero meaning the window is completely opaque
        if counter<=0:
            # Make UI appear
            bFrame1.pack(side='left', anchor='nw', padx=5, pady=5)
            glass.pack(padx=30, pady=30, fill="both", expand=True)
            # Start fading the window back
            mainmenuinit()
            fadeback()


            # AND KILL THE FUCKING THREAD ONCE AGAIN
            sys.exit()


# Fading window back, in a process completely mirroring fade()
def fadeback():
    global counter
    while counter < 1:
        time.sleep(.03)
        counter += 0.05
        wind.attributes('-alpha', counter)
        fadeback()


#################################################################################################


⌈¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯⌉
|         /\                                                                  |
|        /  \                                                                 |
|       /    \      ⌈⌉   ⌈⌉  ⌈¯¯¯¯\  ⌈¯\ ⌈¯⌉  ⌈⌉   []            ⌈¯\ ⌈¯⌉      |
|      /  /\  \    ⌊  ⌋ ⌊  ⌋ | [] |  |  \| | ⌊  ⌋  ⌈⌉   /¯¯¯¯¯\  |  \| |      |  
|     /  /__\  \    ||   ||  | ___/  ||\ \ |  ||   ||  /  /¯\  \ ||\ \ |      |
|    /  ______  \   ||   ||  | ⌊__   || \  |  ||   ||  \  \_/  / || \  |      |
|   /_ /      \_ \  ⌊⌋   ⌊⌋  ⌊____]  ⌊⌋  \_⌋  ⌊⌋   ⌊⌋   \_____/  ⌊⌋  \_⌋      | 
⌊_____________________________________________________________________________⌋

(i spent a lot of time on this ASCII art...)

# Functionality incoming :D
#################################################################################################

# Initializing the popup menu itself
def popup():
    # Add items to the popup menu
    MenuInit()
    # Destroy the button to call the popup
    send.pack_forget()
    message.pack_forget()
    chatwindow.pack_forget()
    sidebar.pack_forget()
    chatwindow.pack_forget()
    # Reloading the popup menu button


# Destroying the popup menu
def popupdestroy():
    global popupmenu, advanced_frame
    # Well... destroying the popup menu
    advanced_frame.pack_forget()
    popupmenu.pack_forget()
    sidebar.pack(side='left', anchor='nw', padx=5, pady=5, expand=True)
    chatwindow.pack(side='bottom', anchor='se', expand=True)
    send.pack(side='left', anchor='sw', expand=False)
    message.pack(side='bottom', anchor='sw', pady=5, padx=10)
    # Reloading popupmenu
    popupmenu = win.Frame(glass, bg="#f8fbff")
    mainmenuinit()


def clearchat():
    history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'w')
    history.write('\n')
    history.close()
    clearhst.configure(text='Done!')


updateipsetb = ttk.Button(advanced_frame, text="Update ipset", command=IPSetinit)
debugbtn = ttk.Button(advanced_frame, text="Debug info")
clearhst=ttk.Button(advanced_frame, text='Clear local chat history', command=clearchat)

debugbtn.pack(anchor="e", pady=5)
updateipsetb.pack(side='bottom', anchor='e', pady=10)
clearhst.pack(anchor='e', pady=5)
# Adding items to the popup menu


def MenuInit():
    global advanced_frame

    # Initializing the closing menu button
    close=ttk.Button(popupmenu, text='✕', command=popupdestroy, width=3)

    # Packing said button in its place
    close.pack(side='right', padx=5, pady=5)

    # Packing the Frames themselves
    advanced_frame.pack(side="bottom", anchor="e", padx=15, pady=15)
    popupmenu.pack(side="top", anchor="e", padx=10, pady=10)
# HOLY PEAK WE HAVE HIT THE TOP OF THE WORLD


windowtext=''
previousmessages=ttk.Label()
msgindex=0

def getdate():
    global msgindex
    # Being a smart ass (not) i am i will make this dependant NOT on IDs but on date
    msgindex+=1
    # nvm i caved in and made it on IDs

def SendingTest():
    global message, previousmessages, history, windowtext, msgindex
    windowtext = ''
    previousmessages.pack_forget()
    previousmessages=win.Label(chatwindow, text=windowtext, bg="#f8fbff", justify='right')
    messageinput=message.get()
    sendS()
    if messageinput!='':
        history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'a', encoding='utf-8')
        getdate()
        history.write(message.get() + f'⁝{msgindex}' + '\n')
        history.close()
    history = open(r"C:\MaCroS\P2PT\H-C\history-client-out.txt", 'r', encoding='utf-8')
    actualhistorylines=history.readlines()
    for i in actualhistorylines:
        for j in i:
            if j!='⁝':
                windowtext += j
            if j == '⁝':
                break
        windowtext += '\n'
    previousmessages.configure(text=windowtext)
    previousmessages.pack(side='bottom', anchor='e')
    history.close()
    message.delete('0', win.END)

###############################


#contact=[]
#contact.append('Local computer')

sidebar = win.Frame(glass, bg = '#dbeaff')
popupmenub = ttk.Button(sidebar, text="Menu", command=popup, width=6)
#chat1=ttk.Button(sidebar, text=contact[0])
chatwindow = win.Frame(glass, bg="#f8fbff")
message = ttk.Entry(chatwindow, width=200)
send = ttk.Button(chatwindow, image=sendbi, width=5, command=SendingTest)


# scraps, delayed
def AddContact():
    with open(r"C:\MaCroS\P2PT\H-C\ipset.txt", 'a') as ipset:
        ipset.write(input('Please enter IP-v4 address: ') + '\n')
        ipset.write(input("Enter Contact's name: \n"))
        messagebox.showinfo('Annoying?','If you want to get rid of console window - restart the program ;)')
    with open(r"C:\MaCroS\config.txt", 'a') as config:
        config.write(contactnum+1)
        contactnum += 1


#AddC = ttk.Button(sidebar, width = 5, text='Add Contact', command=AddContact)

# Add UI elements onto main screen

def mainmenuinit():
    global windowtext, HOST
    windowtext = ''
    sidebar.pack(side='left', anchor='ne', expand=True, pady=5)
    send.pack(side='left', anchor='sw', expand=False)
    message.pack(side='bottom', anchor='sw', pady=5, padx=10)
    chatwindow.pack(side='bottom', anchor='se', expand=True)
#   AddC.pack(side='bottom', anchor = 'sw', expand=True)
    popupmenub.pack(side='top', anchor='nw', expand=True)
    SendingTest()


# Kickstart this whole mess
start_task()

wind.mainloop()
'''
