#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Password Attacks Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Hydra - Network login cracker")
    print("2. John the Ripper - Password cracker")
    print("3. Hashcat - Advanced password recovery")
    print("4. Crunch - Wordlist generator")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        target = input(f"{Fore.WHITE}[?] Enter target: ").strip()
        service = input(f"{Fore.WHITE}[?] Enter service (ssh/ftp/http): ").strip()
        user = input(f"{Fore.WHITE}[?] Enter username: ").strip()
        cmd = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {service}://{target}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "2":
        hash_file = input(f"{Fore.WHITE}[?] Enter hash file path: ").strip()
        cmd = f"john {hash_file}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "3":
        hash_file = input(f"{Fore.WHITE}[?] Enter hash file: ").strip()
        cmd = f"hashcat -m 0 {hash_file} /usr/share/wordlists/rockyou.txt"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        min_len = input(f"{Fore.WHITE}[?] Enter min length: ").strip()
        max_len = input(f"{Fore.WHITE}[?] Enter max length: ").strip()
        chars = input(f"{Fore.WHITE}[?] Enter character set: ").strip()
        output = input(f"{Fore.WHITE}[?] Enter output file: ").strip()
        cmd = f"crunch {min_len} {max_len} {chars} -o {output}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")