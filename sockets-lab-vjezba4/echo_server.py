import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12347))
server_socket.listen(5)

print("TCP Echo server aktivan na portu 12347...")

while True:
    conn, addr = server_socket.accept()
    print(f"{datetime.datetime.now()} | Konekcija s: {addr}")
    data = conn.recv(1024).decode()

    print(f"Vrijeme: {datetime.datetime.now()}")
    print(f"Poruka: {data}")
    print(f"Klijent IP: {addr[0]}")

    if data.lower() == "sandro_bilandzic":
        conn.send(b"Unos nije podrzan.")
    else:
        conn.send(data.encode())

    conn.close()
