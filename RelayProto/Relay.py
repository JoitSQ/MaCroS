import sys
import threading
import socket

HOST = "0.0.0.0"
PORT = 1

def OpenConnection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"MaCroS test relay listening on {HOST}:{PORT}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=ConnMaint, args=(conn, addr), daemon=True)
            thread.start()

def ConnMaint(conn, addr):
        with conn:
            print("Connected:", addr)

            while True:
                data = conn.recv(4096)

                if not data:
                    break

                if 'Σ'.encode('utf-8') not in data:
                    print("Missing separator:", data)
                    continue

                mssg, client = data.split('Σ'.encode('utf-8'), 1)
                print(mssg, client)
                print((str(client.decode())))
                try:
                    with socket.create_connection(
                            (client.decode('utf-8'), 1),
                            timeout=5
                    ) as s:
                        s.settimeout(5)
                        sender_ip = addr[0].encode("utf-8")
                        packet = mssg + "Σ".encode("utf-8") + sender_ip
                        s.sendall(packet)
                        receivedmssg = s.recv(4096)

                    conn.sendall(receivedmssg)

                except OSError as e:
                    print(f"Forwarding failed: {e}")
                    conn.sendall(b'Failed')

OpenConnection()