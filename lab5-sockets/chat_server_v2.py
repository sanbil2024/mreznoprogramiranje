import selectors
import socket
import threading
import time
import logging

# Postavke logiranja
logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize the selector
sel = selectors.DefaultSelector()

# Dictionary to store client information
clients = {}

# Server configuration
HOST = 'localhost'
PORT = 65433

# Create and configure the listening socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)

# Register the listening socket for read events
sel.register(lsock, selectors.EVENT_READ)
print(f"[CHAT SERVER] Listening on {HOST}:{PORT}")
logging.info(f"[CHAT SERVER] Listening on {HOST}:{PORT}")

def prikaz_broja_korisnika():
    while True:
        status = f"[STATUS] Trenutno aktivnih korisnika: {len(clients)}"
        print(status)
        logging.info(status)
        time.sleep(10)

# Pokreni thread za status prikaz
status_thread = threading.Thread(target=prikaz_broja_korisnika, daemon=True)
status_thread.start()

# Main event loop
while True:
    events = sel.select()
    for key, _ in events:
        if key.fileobj == lsock:
            # New client connection
            conn, addr = lsock.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ)
            clients[conn] = {"addr": addr, "name": None}
            print(f"[NEW] Connection from {addr}")
            logging.info(f"[NEW] Connection from {addr}")
        else:
            # Data from existing client
            conn = key.fileobj
            data = conn.recv(1024)
            if data:
                if clients[conn]["name"] is None:
                    # First message is the client's name
                    clients[conn]["name"] = data.decode().strip()
                    print(f"[LOGIN] {clients[conn]['name']} from {clients[conn]['addr']}")
                    logging.info(f"[LOGIN] {clients[conn]['name']} from {clients[conn]['addr']}")
                else:
                    msg_text = data.decode().strip()
                    if msg_text == "/users":
                        korisnici = ", ".join(c["name"] for c in clients.values() if c["name"])
                        conn.sendall(f"[SERVER] Aktivni korisnici: {korisnici}".encode())
                    else:
                        msg = f"{clients[conn]['name']}: {msg_text}"
                        print(msg)
                        logging.info(f"[MESSAGE] {msg}")
                        for c in clients:
                            if c != conn:
                                c.sendall(msg.encode())
            else:
                # Client disconnected
                print(f"[LOGOUT] {clients[conn]['name']}")
                logging.info(f"[LOGOUT] {clients[conn]['name']}")
                sel.unregister(conn)
                conn.close()
                del clients[conn]
