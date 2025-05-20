import socket
import ssl
import datetime

def get_certificate(host, port=443):
    # Create SSL context
    context = ssl.create_default_context()
    
    # Create socket and wrap with SSL
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Get peer certificate
            cert = ssock.getpeercert()
            return cert

def print_certificate_info(cert):
    # Extract and print subject
    subject = dict(x[0] for x in cert['subject'])
    print("Subject:")
    for key, value in subject.items():
        print(f"  {key}: {value}")
    
    # Extract and print issuer
    issuer = dict(x[0] for x in cert['issuer'])
    print("\nIssuer:")
    for key, value in issuer.items():
        print(f"  {key}: {value}")
    
    # Print validity period
    print("\nValidity:")
    print(f"  Not Before: {cert['notBefore']}")
    print(f"  Not After: {cert['notAfter']}")

if __name__ == "__main__":
    host = "www.google.com"
    print(f"Fetching certificate for {host}...")
    try:
        cert = get_certificate(host)
        print_certificate_info(cert)
    except Exception as e:
        print(f"Error: {e}")