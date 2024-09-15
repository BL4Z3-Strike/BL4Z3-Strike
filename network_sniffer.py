#!/usr/bin/env python
from scapy.all import sniff, IP, TCP, UDP, ICMP
from colorama import Fore, Style, init

init(autoreset=True)


def packet_handler(packet):
    print("\nNew Packet:")

    if IP in packet:
        ip_layer = packet[IP]
        print(f"{Fore.BLUE}Source IP: {ip_layer.src}")
        print(f"{Fore.BLUE}Destination IP: {ip_layer.dst}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"{Fore.RED}Protocol: TCP")
            print(f"{Fore.BLUE}Source Port: {tcp_layer.sport}")
            print(f"{Fore.BLUE}Destination Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"{Fore.RED}Protocol: UDP")
            print(f"{Fore.BLUE}Source Port: {udp_layer.sport}")
            print(f"{Fore.BLUE}Destination Port: {udp_layer.dport}")
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"{Fore.RED}Protocol: ICMP")
            print(f"{Fore.BLUE}ICMP Type: {icmp_layer.type}")
            print(f"{Fore.BLUE}ICMP Code: {icmp_layer.code}")
        else:
            print(f"{Fore.RED}Protocol: {packet.proto}")

        print(f"{Fore.BLUE}Packet Content: {packet.summary()}")
    else:
        print(f"{Fore.RED}IP Layer Not Found!")



def start_sniffing(interface=None):
    print(f"{Fore.BLUE}Sniffing Started. (Interface: {interface})")
    sniff(iface=interface, prn=packet_handler, store=0)


if __name__ == "__main__":
    interface = None
    start_sniffing(interface)
