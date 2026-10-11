import socket
sep = 'Σ'.encode('utf-8')
with socket.create_connection(("127.0.0.1", 55483)) as s:
    s.sendall("hello from MaCroSΣ26.0.2.167".encode('utf-8'))
    print(s.recv(4096))