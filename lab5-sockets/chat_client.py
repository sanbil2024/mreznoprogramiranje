import socket

# Server configuration
HOST = 'localhost'
PORT = 65433

# Create and connect the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Send username
name = input("Unesite korisničko ime: ")
sock.sendall(name.encode())

print("Chat započet. Koristite Ctrl+C za izlaz.")

# Main loop for sending messages
while True:
    msg = input("> ")
    sock.sendall(msg.encode())
