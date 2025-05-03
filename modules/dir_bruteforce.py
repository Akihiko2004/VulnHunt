# modules/dir_bruteforce.py

import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

def scan_url(url, path):
    test_url = f"{url.rstrip('/')}/{path}"
    try:
        r = requests.get(test_url, timeout=3)
        if r.status_code in [200, 301, 302]:
            print(Fore.GREEN + f"[+] Found: {test_url} ({r.status_code})" + Fore.RESET)
            return test_url
    except requests.exceptions.RequestException:
        return None

def scan(url, wordlist_file='wordlists/common.txt'):
    print(f"{Fore.YELLOW}[!] Starting directory brute force...{Fore.RESET}")
    try:
        with open(wordlist_file, 'r') as f:
            paths = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"{Fore.RED}[-] Wordlist not found: {wordlist_file}{Fore.RESET}")
        return []

    found = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda path: scan_url(url, path), paths))

    found = [result for result in results if result]
    return found
