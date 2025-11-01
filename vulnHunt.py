#!/usr/bin/env python3
"""
VulnHunt - Red Team Cybersecurity Framework
A comprehensive penetration testing tool for Kali Linux
Author: Your Name
License: MIT
"""

import os
import sys
import subprocess
import time
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class VulnHunt:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Akihiko2004"
        self.banner = f"""
{Fore.RED}
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗
██║   ██║██║   ██║██║     ████╗  ██║██║  ██║██║   ██║████╗  ██║╚══██╔══╝
██║   ██║██║   ██║██║     ██╔██╗ ██║███████║██║   ██║██╔██╗ ██║   ██║   
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══██║██║   ██║██║╚██╗██║   ██║   
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║██║  ██║╚██████╔╝██║ ╚████║   ██║   
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                                         
{Fore.CYAN}                    Red Team Cybersecurity Framework
{Fore.YELLOW}                         Version: {self.version}
{Fore.GREEN}                          Author: {self.author}
{Style.RESET_ALL}
"""
        
        self.tools = {
            "1": {"name": "Network Reconnaissance", "module": "network_recon"},
            "2": {"name": "Web Application Testing", "module": "web_app_testing"},
            "3": {"name": "Vulnerability Scanning", "module": "vuln_scanning"},
            "4": {"name": "Password Attacks", "module": "password_attacks"},
            "5": {"name": "Wireless Attacks", "module": "wireless_attacks"},
            "6": {"name": "Social Engineering", "module": "social_engineering"},
            "7": {"name": "Post-Exploitation", "module": "post_exploitation"},
            "8": {"name": "Forensic Analysis", "module": "forensic_analysis"},
            "9": {"name": "Custom Tool Integration", "module": "custom_tools"},
            "10": {"name": "Automated Attack Chain", "module": "automated_chain"}
        }

    def display_menu(self):
        print(self.banner)
        print(f"{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                        AVAILABLE TOOLS                             ║")
        print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════════════════╣")
        
        for key, tool in self.tools.items():
            print(f"{Fore.CYAN}║ {Fore.WHITE}{key:>2}. {tool['name']:<55} {Fore.CYAN}║")
        
        print(f"{Fore.CYAN}╠══════════════════════════════════════════════════════════════════════╣")
        print(f"{Fore.CYAN}║ {Fore.WHITE} 0. Exit VulnHunt{' ':40} {Fore.CYAN}║")
        print(f"{Fore.CYAN}║ {Fore.WHITE}99. Multi-Tool Selection{' ':33} {Fore.CYAN}║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

    def check_dependencies(self):
        """Check if required tools are installed"""
        required_tools = [
            "nmap", "sqlmap", "metasploit-framework", "aircrack-ng",
            "hydra", "john", "wireshark", "burpsuite", "setoolkit"
        ]
        
        missing_tools = []
        for tool in required_tools:
            if subprocess.run(["which", tool], capture_output=True).returncode != 0:
                missing_tools.append(tool)
        
        if missing_tools:
            print(f"{Fore.RED}[!] Missing tools: {', '.join(missing_tools)}")
            print(f"{Fore.YELLOW}[*] Install with: sudo apt install {' '.join(missing_tools)}")
            return False
        return True

    def run_tool(self, choice):
        """Execute selected tool"""
        if choice == "0":
            print(f"{Fore.GREEN}[+] Exiting VulnHunt. Stay secure!")
            sys.exit(0)
        
        if choice == "99":
            self.multi_tool_selection()
            return
        
        if choice in self.tools:
            tool_name = self.tools[choice]["name"]
            module_name = self.tools[choice]["module"]
            print(f"{Fore.GREEN}[+] Starting {tool_name}...")
            
            # Import and run the module
            try:
                module = __import__(f"modules.{module_name}", fromlist=['run'])
                module.run()
            except ImportError as e:
                print(f"{Fore.RED}[!] Module {module_name} not implemented yet: {e}")
            except Exception as e:
                print(f"{Fore.RED}[!] Error running {tool_name}: {e}")
        else:
            print(f"{Fore.RED}[!] Invalid selection. Please choose a valid option.")

    def multi_tool_selection(self):
        """Allow user to select multiple tools"""
        print(f"{Fore.CYAN}\n[+] Multi-Tool Selection Mode")
        print(f"{Fore.YELLOW}[*] Select tools by number (comma-separated, e.g., 1,3,5)")
        
        selected = input(f"{Fore.WHITE}[?] Enter tool numbers: ").strip().split(',')
        
        for tool_num in selected:
            tool_num = tool_num.strip()
            if tool_num in self.tools:
                self.run_tool(tool_num)
                time.sleep(1)  # Small delay between tools
            else:
                print(f"{Fore.RED}[!] Invalid tool number: {tool_num}")

    def main(self):
        """Main program loop"""
        if not self.check_dependencies():
            print(f"{Fore.RED}[!] Please install missing dependencies before continuing.")
            return
        
        while True:
            self.display_menu()
            choice = input(f"\n{Fore.WHITE}[?] Select an option: ").strip()
            self.run_tool(choice)
            input(f"\n{Fore.YELLOW}[*] Press Enter to continue...")

if __name__ == "__main__":
    try:
        vulnhunt = VulnHunt()
        vulnhunt.main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] VulnHunt interrupted by user.")
        sys.exit(1) 