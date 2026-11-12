import socket
import ipaddress


def check_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)

            result = sock.connect_ex((target, port))

            if result == 0:
                return "OPEN"
            else:
                return "CLOSED"

    except socket.timeout:
        return "TIMEOUT"

    except socket.error:
        return "ERROR"


def validate_ports(port_input):
    try:
        ports = [int(port.strip()) for port in port_input.split(",")]

        if not ports:
            return None

        if any(port < 1 or port > 65535 for port in ports):
            return None

        return sorted(set(ports))

    except ValueError:
        return None


def main():
    print("=" * 45)
    print("          PYTHON PORT STATUS CHECKER")
    print("=" * 45)

    target = input("Enter target IP address: ")

    try:
        ip = ipaddress.ip_address(target)

        if not (ip.is_private or ip.is_loopback):
            print("Only localhost or private IP addresses are allowed.")
            return

    except ValueError:
        print("Invalid IP address!")
        return

    print("\nExample: 22,80,443,8000")
    port_input = input("Enter ports to check: ")

    ports = validate_ports(port_input)

    if ports is None:
        print("Invalid port input! Use ports between 1 and 65535.")
        return

    print("\n" + "=" * 45)
    print(f"Target IP : {target}")
    print(f"Total Ports: {len(ports)}")
    print("=" * 45)

    open_ports = 0
    closed_ports = 0
    other_ports = 0

    for port in ports:
        status = check_port(target, port)
        print(f"Port {port:<8}: {status}")

        if status == "OPEN":
            open_ports += 1
        elif status == "CLOSED":
            closed_ports += 1
        else:
            other_ports += 1

    print("=" * 45)
    print("              SCAN SUMMARY")
    print("=" * 45)
    print(f"Open Ports   : {open_ports}")
    print(f"Closed Ports : {closed_ports}")
    print(f"Other Status : {other_ports}")
    print("=" * 45)
    print("Scan completed!")


if __name__ == "__main__":
    main()