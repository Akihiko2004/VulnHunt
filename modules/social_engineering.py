#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Social Engineering Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Social Engineering Toolkit (SET)")
    print("2. Phishing Framework - Gophish")
    print("3. Credential Harvester")
    print("4. Website Cloner")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        print(f"{Fore.GREEN}[+] Starting Social Engineering Toolkit...")
        subprocess.run(["setoolkit"])
    
    elif choice == "2":
        print(f"{Fore.YELLOW}[*] Starting Gophish...")
        subprocess.run(["systemctl", "start", "gophish"])
        print(f"{Fore.GREEN}[+] Gophish started. Access via https://localhost:3333")
    
    elif choice == "3":
        print(f"{Fore.YELLOW}[*] Starting credential harvester...")
        # Custom credential harvester implementation
        target_url = input(f"{Fore.WHITE}[?] Enter target URL to clone: ").strip()
        print(f"{Fore.GREEN}[+] Cloning {target_url} for credential harvesting")
        # Implementation would clone site and set up harvesting
    
    elif choice == "4":
        target_url = input(f"{Fore.WHITE}[?] Enter website URL to clone: ").strip()
        output_dir = input(f"{Fore.WHITE}[?] Enter output directory: ").strip()
        cmd = f"setoolkit --website-cloner --url {target_url} --output {output_dir}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")