import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

class PortScanner:
    def scan_port(self, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout süresi
            result = sock.connect_ex((ip, port))
            return port if result == 0 else None

    def scan_ports(self, ip, start_port, end_port):
        open_ports = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.scan_port, ip, port) for port in range(start_port, end_port + 1)]
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    open_ports.append(result)
        return open_ports
