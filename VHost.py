import socket

HOST='localhost'
PORT=1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(f'Recieved {data}')
            fuckass=b'Im here and responding'
            conn.sendall(fuckass)