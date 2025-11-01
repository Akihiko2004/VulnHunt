#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Web Application Testing Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. SQL Injection - SQLmap")
    print("2. XSS Testing - XSStrike")
    print("3. Directory Brute Force - Dirb")
    print("4. Subdomain Enumeration - Subfinder")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        url = input(f"{Fore.WHITE}[?] Enter target URL: ").strip()
        cmd = f"sqlmap -u {url} --batch --level=3 --risk=3"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "2":
        url = input(f"{Fore.WHITE}[?] Enter target URL: ").strip()
        cmd = f"python3 xsstrike.py -u {url}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        print(f"{Fore.YELLOW}[*] Note: Ensure XSStrike is installed")
    
    elif choice == "3":
        url = input(f"{Fore.WHITE}[?] Enter target URL: ").strip()
        cmd = f"dirb {url} /usr/share/wordlists/dirb/common.txt"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        domain = input(f"{Fore.WHITE}[?] Enter domain: ").strip()
        cmd = f"subfinder -d {domain}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")