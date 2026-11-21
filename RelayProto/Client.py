import socket
sep = 'Σ'.encode('utf-8')
with socket.create_connection(("192.168.3.11", 55483)) as s:
    s.sendall("hello from MaCroSΣ26.0.2.167".encode('utf-8'))
    print(s.recv(4096))