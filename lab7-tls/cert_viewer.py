import socket
import ssl
import datetime

def get_certificate(host, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            return cert

def print_certificate_info(cert):
    subject = dict(x[0] for x in cert['subject'])
    print("Subject:")
    for key, value in subject.items():
        print(f"  {key}: {value}")
    issuer = dict(x[0] for x in cert['issuer'])
    print("\nIssuer:")
    for key, value in issuer.items():
        print(f"  {key}: {value}")
    print("\nValidity:")
    print(f"  Not Before: {cert['notBefore']}")
    print(f"  Not After: {cert['notAfter']}")

def send_http_request(host, port, use_tls=False):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if use_tls:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=host)
        
        sock.connect((host, port))
        # Add Accept-Encoding: identity to prevent compression
        request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Connection: close\r\n"
            f"Accept-Encoding: identity\r\n"
            f"\r\n"
        )
        sock.sendall(request.encode())
        
        # Receive response
        response = b""
        while True:
            data = sock.recv(1024)
            if not data:
                break
            response += data
        
        # Split headers and body, decode headers only
        headers = response.split(b"\r\n\r\n")[0]
        try:
            headers_str = headers.decode('utf-8')
        except UnicodeDecodeError:
            headers_str = headers.decode('latin-1', errors='ignore')
        
        print(f"\nResponse from {host}:{port} ({'TLS' if use_tls else 'Plain'}):")
        print(headers_str)
        
        sock.close()
    except Exception as e:
        print(f"Error on {host}:{port} ({'TLS' if use_tls else 'Plain'}): {e}")

if __name__ == "__main__":
    host = "www.google.com"
    
    # Zadatak 1
    print(f"Fetching certificate for {host}...")
    try:
        cert = get_certificate(host)
        print_certificate_info(cert)
    except Exception as e:
        print(f"Error: {e}")
    
    # Zadatak 2
    print("\nComparing plain and TLS connections...")
    send_http_request(host, 80, use_tls=False)
    send_http_request(host, 443, use_tls=True)