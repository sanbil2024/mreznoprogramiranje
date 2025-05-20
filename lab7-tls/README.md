# Lab 7 - SSL/TLS with Python

This folder contains scripts for exploring SSL/TLS in Python for the Network Programming course.

## How to Run the Scripts

### Prerequisites
- Python 3 installed.
- OpenSSL for generating certificates.
- All scripts and certificate files (`server.crt`, `server.key`) are in the `lab7-tls` folder.

### Certificate Viewer (`cert_viewer.py`)
- **Purpose**: Fetches and displays TLS certificate details from www.google.com and compares plain vs TLS connections.
- **Run**:
  ```bash
  python3 cert_viewer.py
  ```

### TLS Echo Server (`tls_server.py`)
- **Purpose**: Runs a TLS-secured echo server using a self-signed certificate.
- **Run**:
  ```bash
  python3 tls_server.py
  ```
- **Note**: Requires `server.crt` and `server.key` in the same folder.

### TLS Client (`tls_client.py`)
- **Purpose**: Connects to the TLS echo server to send and receive messages.
- **Run**:
  ```bash
  python3 tls_client.py
  ```

## Example Certificate Output
```
Fetching certificate for www.google.com...
Subject:
  commonName: www.google.com
Issuer:
  countryName: US
  organizationName: Google Trust Services
  commonName: WR2
Validity:
  Not Before: Apr 21 08:42:35 2025 GMT
  Not After: Jul 14 08:42:34 2025 GMT
```

## Comparison: Plain vs TLS Connection
- **Plain (HTTP, port 80)**:
  - Unencrypted, redirects to HTTPS (301 Moved Permanently).
  - Headers: `Location: https://www.google.com/`, `Content-Type: text/html`.
- **TLS (HTTPS, port 443)**:
  - Encrypted, returns full HTML (200 OK).
  - Headers: `Content-Type: text/html`, includes security headers like `Strict-Transport-Security`.
- **Key Difference**: TLS ensures data confidentiality and integrity, preventing interception, while plain HTTP is vulnerable.