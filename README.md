# Python Port Status Checker

A Python-based tool that checks the status of specified ports on a localhost or private IPv4/IPv6 target.

## Features

- Validate IP addresses.
- Check manually specified ports.
- Identify open and closed ports.
- Detect connection timeouts and errors.
- Display a scan summary.
- Validate port numbers (1–65535).
- Supports multiple port checks.

## Technologies

- Python 3
- Socket
- IP Address

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pradipta-web/python-port-status-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-port-status-checker
   ```

3. Run the program:

   ```bash
   py main.py
   ```

## Usage

1. Enter the target IP address.
2. Enter the port numbers separated by commas.
3. Wait for the results.

Example:

```text
Enter target IP address: 127.0.0.1
Enter ports to check: 22,80,443,8000
```

## Example Output

```text
Target IP : 127.0.0.1
Total Ports: 4

Port 22      : CLOSED
Port 80      : CLOSED
Port 443     : CLOSED
Port 8000    : OPEN

SCAN SUMMARY
Open Ports   : 1
Closed Ports : 3
Other Status : 0
```

## Port Status Explanation

| Status | Description |
|---|---|
| OPEN | A service accepts the connection. |
| CLOSED | The connection was refused or unsuccessful. |
| TIMEOUT | The connection attempt timed out. |
| ERROR | Another socket error occurred. |

## Learning Objectives

- Python socket programming.
- IP address validation.
- TCP connection handling.
- Exception handling.
- Input validation.

## Disclaimer

This tool is intended for educational purposes and authorized testing on localhost or private networks. Only test devices and networks you own or have permission to assess.

## Author

**Kinervaaa**
