import subprocess

def change_mac(interface, new_mac):
    try:
        subprocess.call(['sudo', 'ip', 'link', 'set', 'dev', interface, 'down'])

        subprocess.call(['sudo', 'ip', 'link', 'set', 'dev', interface, 'address', new_mac])

        subprocess.call(['sudo', 'ip', 'link', 'set', 'dev', interface, 'up'])

        print(f"[+] MAC address for {interface} has been changed to {new_mac}.")
    except Exception as e:
        print(f"Error occurred: {e}")

