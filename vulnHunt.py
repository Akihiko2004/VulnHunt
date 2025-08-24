import argparse
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

def main():
    print_banner()
    # Your tool's logic goes here
    print("Starting VulnHunt...")
    parser = argparse.ArgumentParser(description='Advanced Web Vulnerability Scanner')
    parser.add_argument('--url', required=True, help='URL of the website to scan')
    parser.add_argument('--skip-sqli', action='store_true', help='Skip SQL Injection scan')
    parser.add_argument('--skip-xss', action='store_true', help='Skip XSS scan')
    parser.add_argument('--skip-headers', action='store_true', help='Skip Header security scan')
    parser.add_argument('--brute', action='store_true', help='Enable directory brute-forcing')
    args = parser.parse_args()

    results = []

    if not args.skip_sqli:
        results.extend(sql_scan(args.url))
    
    if not args.skip_xss:
        results.extend(xss_scan(args.url))

    if not args.skip_headers:
        results.extend(header_check(args.url))

    if args.brute:
        brute_results = dir_scan(args.url)
        if brute_results:
            results.append(f"\n[+] Found directories:\n")
            results.extend(brute_results)
    
    report_filename = save_report(results)
    print(f"[+] Report saved to: {report_filename}")

if __name__ == "__main__":
    main()
