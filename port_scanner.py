#!/usr/bin/env python3
import socket
import concurrent.futures

def scan_port(ip, port, timeout=2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            return port if result == 0 else None
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
        return None

def scan_ports(ip, start_port, end_port, max_workers=100):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
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
