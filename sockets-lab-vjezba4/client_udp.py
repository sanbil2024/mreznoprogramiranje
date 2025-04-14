import socket
from local_machine_info import print_machine_info

print_machine_info()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Unesi poruku ('exit' za kraj): ")
    if msg.lower() == "exit":
        break
    client_socket.sendto(msg.encode(), ("127.0.0.1", 12345))
    response, _ = client_socket.recvfrom(1024)
    print("Odgovor servera:", response.decode())
