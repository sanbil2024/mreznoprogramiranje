import socket
import sys

def scan_port(host, port):
    # Set default timeout for socket connections
    socket.setdefaulttimeout(0.5)
    
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} on {host} is OPEN")
        else:
            print(f"Port {port} on {host} is CLOSED or unavailable")
    except socket.gaierror:
        print(f"Error: Could not resolve host {host}")
    except socket.error as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 port_scanner.py <host> <port>")
        sys.exit(1)
    
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
        if not 1 <= port <= 65535:
            print("Error: Port must be between 1 and 65535")
            sys.exit(1)
    except ValueError:
        print("Error: Port must be a number")
        sys.exit(1)
    
    scan_port(host, port)
