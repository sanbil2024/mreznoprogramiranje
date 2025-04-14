import socket
from local_machine_info import print_machine_info

print_machine_info()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 12345))

print("UDP server spreman na portu 12345...")

while True:
    message, address = server_socket.recvfrom(1024)
    print(f"Primljena poruka: {message.decode()} od {address}")
    server_socket.sendto(b"Poruka primljena!", address)
