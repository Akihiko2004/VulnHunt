import os
import sys
from modules.sql_injection import scan as sql_scan
from modules.xss_scanner import scan as xss_scan
from modules.header_checker import check as header_check
from modules.dir_bruteforce import scan as dir_scan
from modules.report_writer import save_report

def print_banner():
    try:
        with open("banner.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Banner file not found. Please make sure banner.txt is in the same folder.")

def get_url():
    url = input("Enter target URL (e.g. http://example.com): ").strip()
    if not url.startswith("http"):
        print("[!] URL must start with http:// or https://")
        return get_url()
    return url

def show_menu():
    print("\nSelect one or more options (comma-separated):")
    print("1. SQL Injection Scan")
    print("2. XSS Scan")
    print("3. Header Security Check")
    print("4. Directory Bruteforce")
    print("5. All (Full Scan)")
    print("6. Exit")

    choice = input("\nYour choice: ").strip()
    return [c.strip() for c in choice.split(",")]

def main():
    print_banner()
    url = get_url()

    while True:
        selected_options = show_menu()
        results = []

        if '6' in selected_options:
            print("Goodbye!")
            sys.exit(0)

        if '5' in selected_options:
            selected_options = ['1', '2', '3', '4']  # Full scan

        if '1' in selected_options:
            print("\n[+] Starting SQL Injection Scan...")
            results.extend(sql_scan(url))

        if '2' in selected_options:
            print("\n[+] Starting XSS Scan...")
            results.extend(xss_scan(url))

        if '3' in selected_options:
            print("\n[+] Checking Security Headers...")
            results.extend(header_check(url))

        if '4' in selected_options:
            print("\n[+] Starting Directory Bruteforce...")
            dirs = dir_scan(url)
            if dirs:
                results.append("\n[+] Found Directories:\n")
                results.extend(dirs)

        if results:
            report_filename = save_report(results)
            print(f"\n[+] Scan complete. Report saved to: {report_filename}")
        else:
            print("\n[-] No scan performed or no results.")

        input("\nPress Enter to scan again or Ctrl+C to exit...")

if __name__ == "__main__":
    main()
