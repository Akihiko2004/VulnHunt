#!/usr/bin/env python3

import subprocess
import sys
import time
from colorama import Fore, Style

def run():
    print(f"{Fore.CYAN}\n[+] Automated Attack Chain Module")
    print(f"{Fore.YELLOW}[*] Available attack chains:")
    print("1. Web Application Full Assessment")
    print("2. Network Penetration Test")
    print("3. Wireless Security Audit")
    print("4. Social Engineering Campaign")
    
    choice = input(f"{Fore.WHITE}[?] Select attack chain: ").strip()
    
    if choice == "1":
        target_url = input(f"{Fore.WHITE}[?] Enter target URL: ").strip()
        print(f"{Fore.GREEN}[+] Starting Web Application Full Assessment...")
        
        # Step 1: Reconnaissance
        print(f"{Fore.YELLOW}[*] Step 1: Reconnaissance")
        subprocess.run(["nmap", "-sS", "-sV", "-A", target_url])
        time.sleep(2)
        
        # Step 2: Directory Brute Force
        print(f"{Fore.YELLOW}[*] Step 2: Directory Brute Force")
        subprocess.run(["dirb", target_url, "/usr/share/wordlists/dirb/common.txt"])
        time.sleep(2)
        
        # Step 3: Vulnerability Scanning
        print(f"{Fore.YELLOW}[*] Step 3: Vulnerability Scanning")
        subprocess.run(["nikto", "-h", target_url])
        time.sleep(2)
        
        # Step 4: SQL Injection Testing
        print(f"{Fore.YELLOW}[*] Step 4: SQL Injection Testing")
        subprocess.run(["sqlmap", "-u", f"{target_url}", "--batch", "--level=3", "--risk=3"])
        
        print(f"{Fore.GREEN}[+] Web application assessment completed!")
    
    elif choice == "2":
        target_ip = input(f"{Fore.WHITE}[?] Enter target IP/range: ").strip()
        print(f"{Fore.GREEN}[+] Starting Network Penetration Test...")
        
        # Step 1: Network Discovery
        print(f"{Fore.YELLOW}[*] Step 1: Network Discovery")
        subprocess.run(["nmap", "-sn", target_ip])
        time.sleep(2)
        
        # Step 2: Port Scanning
        print(f"{Fore.YELLOW}[*] Step 2: Port Scanning")
        subprocess.run(["nmap", "-sS", "-sV", "-A", "-T4", target_ip])
        time.sleep(2)
        
        # Step 3: Vulnerability Scanning
        print(f"{Fore.YELLOW}[*] Step 3: Vulnerability Scanning")
        subprocess.run(["nmap", "--script", "vuln", target_ip])
        
        print(f"{Fore.GREEN}[+] Network penetration test completed!")
    
    elif choice == "3":
        print(f"{Fore.GREEN}[+] Starting Wireless Security Audit...")
        
        # Step 1: Monitor Mode
        print(f"{Fore.YELLOW}[*] Step 1: Enabling Monitor Mode")
        subprocess.run(["airmon-ng", "start", "wlan0"])
        time.sleep(2)
        
        # Step 2: Network Discovery
        print(f"{Fore.YELLOW}[*] Step 2: Network Discovery")
        subprocess.run(["airodump-ng", "wlan0mon"])
        time.sleep(2)
        
        # Step 3: Automated Attack
        print(f"{Fore.YELLOW}[*] Step 3: Automated Attack")
        subprocess.run(["wifite"])
        
        print(f"{Fore.GREEN}[+] Wireless security audit completed!")
    
    elif choice == "4":
        print(f"{Fore.GREEN}[+] Starting Social Engineering Campaign...")
        print(f"{Fore.YELLOW}[*] Launching Social Engineering Toolkit")
        subprocess.run(["setoolkit"])
        
        print(f"{Fore.GREEN}[+] Social engineering campaign completed!")
    
    else:
        print(f"{Fore.RED}[!] Invalid selection")