import socket

HOST='localhost'
PORT=1
print('Listening...')
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr, ', sending to ', addr)
            data = conn.recv(1024)
            print(f'Recieved {data}')
            conn.send(b'Received')
