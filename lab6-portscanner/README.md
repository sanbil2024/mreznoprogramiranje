# Lab 6 - Port Scanner

This folder contains a TCP port scanner implemented in Python for the Network Programming course.

## How to Run the Scanner

### Prerequisites
- Python 3 installed.
- All scripts are in the `lab6-portscanner` folder.

### Running the Scanner

- **Single Port (Zadatak 1)**:
  ```bash
  python3 port_scanner.py <host> <port>
  ```
  Example:
  ```bash
  python3 port_scanner.py 127.0.0.1 22
  ```

- **Port Range (Zadatak 2)**:
  ```bash
  python3 port_scanner.py <host> <start_port> <end_port>
  ```
  Example:
  ```bash
  python3 port_scanner.py scanme.nmap.org 20 1024
  ```

## Example Output

- **Zadatak 1**:
  ```
  Port 22 on 127.0.0.1 is OPEN
  Port 80 on scanme.nmap.org is OPEN
  Port 80 on portquiz.net is OPEN
  ```

- **Zadatak 2**:
  ```
  Scanning 127.0.0.1 from port 20 to 1024...
  Otvoreni portovi na 127.0.0.1:
  - Port 22 (ssh)
  ```
  ```
  Scanning scanme.nmap.org from port 20 to 1024...
  Otvoreni portovi na scanme.nmap.org:
  - Port 22 (ssh)
  - Port 80 (http)
  ```

## Tested Ports
- **localhost (127.0.0.1)**: 22, 80, 443, 20–1024
- **scanme.nmap.org**: 22, 80, 20–1024
- **portquiz.net**: 80, 443, 8080