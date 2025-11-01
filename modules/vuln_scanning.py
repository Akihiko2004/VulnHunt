#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Vulnerability Scanning Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Nessus - Comprehensive vulnerability scanner")
    print("2. OpenVAS - Open source vulnerability scanner")
    print("3. Nikto - Web server scanner")
    print("4. WPScan - WordPress vulnerability scanner")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        print(f"{Fore.YELLOW}[*] Starting Nessus...")
        subprocess.run(["systemctl", "start", "nessusd"])
        print(f"{Fore.GREEN}[+] Nessus started. Access via https://localhost:8834")
    
    elif choice == "2":
        target = input(f"{Fore.WHITE}[?] Enter target: ").strip()
        cmd = f"openvas-scanner --target {target}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "3":
        url = input(f"{Fore.WHITE}[?] Enter target URL: ").strip()
        cmd = f"nikto -h {url}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        url = input(f"{Fore.WHITE}[?] Enter WordPress site URL: ").strip()
        cmd = f"wpscan --url {url} --enumerate p,t,u"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")