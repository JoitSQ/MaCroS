import socket

HOST = "172.24.0.1"
PORT = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Client waiting for parry {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        with conn:

            while True:
                data = conn.recv(4096)
                if not data:
                    break
                if 'Σ'.encode('utf-8') not in data:
                    print("Missing separator:", data)
                    continue

                if 'Onlineλ' in data.decode('utf-8'):
                    conn.sendall(b'ConfirmedOnlineSentBack')
                    break
                print(data.decode('utf-8'))
                mssg, client = data.split('Σ'.encode('utf-8'), 1)
                conn.sendall(b'Rec')
                print('SENT BACK')
