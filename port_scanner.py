# port_scanner.py
import socket
import concurrent.futures

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        return port if result == 0 else None

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        ports = range(start_port, end_port + 1)
        future_to_port = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                result = future.result()
                if result is not None:
                    open_ports.append(result)
            except Exception as e:
                print(f"Error scanning port {port}: {e}")
    return open_ports
