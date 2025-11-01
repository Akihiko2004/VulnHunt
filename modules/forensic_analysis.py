#!/usr/bin/env python3

import subprocess
import sys
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Forensic Analysis Module")
    print(f"{Fore.YELLOW}[*] Available tools:")
    print("1. Autopsy - Digital forensics platform")
    print("2. Volatility - Memory forensics")
    print("3. Binwalk - Firmware analysis")
    print("4. Foremost - File carving")
    
    choice = input(f"{Fore.WHITE}[?] Select tool: ").strip()
    
    if choice == "1":
        print(f"{Fore.GREEN}[+] Starting Autopsy...")
        subprocess.run(["autopsy"])
    
    elif choice == "2":
        memory_file = input(f"{Fore.WHITE}[?] Enter memory dump file: ").strip()
        if memory_file:
            print(f"{Fore.YELLOW}[*] Available Volatility profiles:")
            subprocess.run(["volatility", "-h"])
            plugin = input(f"{Fore.WHITE}[?] Enter plugin (e.g., imageinfo, pslist): ").strip()
            cmd = f"volatility -f {memory_file} {plugin}"
            print(f"{Fore.GREEN}[+] Running: {cmd}")
            subprocess.run(cmd.split())
    
    elif choice == "3":
        firmware_file = input(f"{Fore.WHITE}[?] Enter firmware file: ").strip()
        cmd = f"binwalk {firmware_file}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "4":
        disk_image = input(f"{Fore.WHITE}[?] Enter disk image: ").strip()
        output_dir = input(f"{Fore.WHITE}[?] Enter output directory: ").strip()
        cmd = f"foremost -i {disk_image} -o {output_dir}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")