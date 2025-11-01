#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Wireless Attacks Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Aircrack-ng - WiFi security auditing")
    print("2. Wifite - Automated wireless auditor")
    print("3. Reaver - WPS PIN attack")
    print("4. Kismet - Wireless network detector")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        print(f"{Fore.YELLOW}[*] Starting monitor mode...")
        subprocess.run(["airmon-ng", "start", "wlan0"])
        print(f"{Fore.GREEN}[+] Monitor mode started")
    
    elif choice == "2":
        cmd = "wifite"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "3":
        bssid = input(f"{Fore.WHITE}[?] Enter target BSSID: ").strip()
        cmd = f"reaver -i wlan0mon -b {bssid} -vv"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        cmd = "kismet"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")