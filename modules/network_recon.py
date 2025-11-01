#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Network Reconnaissance Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Nmap - Network discovery and security auditing")
    print("2. Masscan - Mass IP port scanner")
    print("3. DNS Recon - DNS enumeration")
    print("4. SNMP Walk - SNMP enumeration")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        target = input(f"{Fore.WHITE}[?] Enter target IP/hostname: ").strip()
        cmd = f"nmap -sS -sV -A -T4 {target}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "2":
        target = input(f"{Fore.WHITE}[?] Enter target IP range: ").strip()
        cmd = f"masscan -p1-65535 {target} --rate=1000"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "3":
        domain = input(f"{Fore.WHITE}[?] Enter domain: ").strip()
        cmd = f"dnsrecon -d {domain}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        target = input(f"{Fore.WHITE}[?] Enter SNMP target: ").strip()
        cmd = f"snmpwalk -c public -v1 {target}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")