import socket
from local_machine_info import print_machine_info

print_machine_info()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12347))

msg = input("Unesi poruku za slanje serveru: ")
client_socket.send(msg.encode())
response = client_socket.recv(1024).decode()
print("Odgovor servera:", response)

client_socket.close()
