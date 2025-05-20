import socket
import ssl

def start_tls_client():
    # Server configuration
    HOST = 'localhost'
    PORT = 8443
    
    # Create SSL context for the client
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False  # Disable for self-signed certificate
    context.verify_mode = ssl.CERT_NONE  # Bypass verification for self-signed cert
    
    # Create TCP socket
    with socket.create_connection((HOST, PORT)) as sock:
        # Wrap socket with SSL
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print(f"[TLS CLIENT] Connected to {HOST}:{PORT}")
            try:
                while True:
                    msg = input("Enter message (or 'exit' to quit): ")
                    if msg.lower() == 'exit':
                        break
                    ssock.sendall(msg.encode())
                    data = ssock.recv(1024)
                    print(f"[TLS CLIENT] Received: {data.decode()}")
            except Exception as e:
                print(f"[TLS CLIENT] Error: {e}")

if __name__ == "__main__":
    start_tls_client()