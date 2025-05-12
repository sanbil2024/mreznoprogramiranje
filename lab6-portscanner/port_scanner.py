import socket
import sys

def scan_port(host, port):
    socket.setdefaulttimeout(0.5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except socket.error:
                service = "unknown"
            return f"Port {port} ({service})"
        return None
    except socket.gaierror:
        print(f"Error: Could not resolve host {host}")
        return None
    except socket.error as e:
        print(f"Error: {e}")
        return None
    finally:
        sock.close()

def scan_port_range(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        result = scan_port(host, port)
        if result:
            open_ports.append(result)
    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 port_scanner.py <host> <start_port> <end_port>")
        sys.exit(1)
    
    host = sys.argv[1]
    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            print("Error: Ports must be between 1 and 65535")
            sys.exit(1)
        if start_port > end_port:
            print("Error: Start port must be less than or equal to end port")
            sys.exit(1)
    except ValueError:
        print("Error: Ports must be numbers")
        sys.exit(1)
    
    open_ports = scan_port_range(host, start_port, end_port)
    if open_ports:
        print(f"\nOtvoreni portovi na {host}:")
        for port in open_ports:
            print(f"- {port}")
    else:
        print(f"\nNema otvorenih portova na {host} u rasponu {start_port}-{end_port}")
