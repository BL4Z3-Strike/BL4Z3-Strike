import os
from colorama import Fore

def manage_tor_service(action):
    if action == 'start':
        os.system("sudo service tor start")
        os.system("sudo iptables -F")
        os.system("sudo iptables -t nat -F")
        os.system("sudo iptables -t nat -A OUTPUT -m owner --uid-owner $(id -u) -j RETURN")
        os.system("sudo iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 9053")
        os.system("sudo iptables -t nat -A OUTPUT -d 127.0.0.0/8 -j RETURN")
        os.system("sudo iptables -t nat -A OUTPUT -o lo -j RETURN")
        os.system("sudo iptables -t nat -A OUTPUT -m owner --uid-owner $(id -u) -j RETURN")
        os.system("sudo iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040")
        os.system("sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
        os.system("sudo iptables -A OUTPUT -m owner --uid-owner $(id -u) -j ACCEPT")
        os.system("sudo iptables -A OUTPUT -j REJECT")
        print(Fore.GREEN+"[+]Tor started and IP tables updated.")
        
    elif action == 'stop':
        os.system("sudo service tor stop")
        os.system("sudo iptables -F")
        os.system("sudo iptables -t nat -F")
        print(Fore.RED+"[-]Tor stopped and IP tables cleared.")
        
    else:
        print("Invalid action. Use 'start' or 'stop'.")

def main():
    print("[1] Start Anon Tor Service")
    print("[2] Stop Tor")
    choice = input("Choose an option: ")
    
    if choice == '1':
        manage_tor_service('start')
    elif choice == '2':
        manage_tor_service('stop')
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
