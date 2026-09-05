import socket
from io import StringIO
HOST='localhost'
PORT=1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    inputtst = bytes(input(), 'utf-8')
    s.sendall(inputtst)
    data = s.recv(1024)

print('Received ', repr(data), ', by ', HOST)
