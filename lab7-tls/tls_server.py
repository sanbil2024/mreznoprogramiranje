import socket
import ssl

def start_tls_server():
    # Server configuration
    HOST = 'localhost'
    PORT = 8443
    CERTFILE = 'server.crt'
    KEYFILE = 'server.key'
    
    # Create SSL context for the server
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
    
    # Create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    print(f"[TLS SERVER] Listening on {HOST}:{PORT}")
    
    # Wrap socket with SSL
    with context.wrap_socket(sock, server_side=True) as ssock:
        try:
            conn, addr = ssock.accept()
            with conn:
                print(f"[TLS SERVER] Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print(f"[TLS SERVER] Client {addr} disconnected")
                        break
                    print(f"[TLS SERVER] Received: {data.decode()}")
                    conn.sendall(data)
        except Exception as e:
            print(f"[TLS SERVER] Error: {e}")
        finally:
            sock.close()

if __name__ == "__main__":
    start_tls_server()