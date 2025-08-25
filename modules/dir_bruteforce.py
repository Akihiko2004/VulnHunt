import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore

def scan_url(url, path):
    test_url = f"{url.rstrip('/')}/{path}"
    try:
        r = requests.get(test_url, timeout=3)
        if r.status_code in [200, 301, 302]:
            message = f"[+] Found: {test_url} ({r.status_code})"
            print(Fore.GREEN + message + Fore.RESET)
            return message
    except requests.exceptions.RequestException:
        return None

def scan(url, wordlist_file='wordlists/common.txt'):
    """
    Directory brute force scanning.
    Yields results live as directories are found.
    """
    print(f"{Fore.YELLOW}[!] Starting directory brute force...{Fore.RESET}")
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as f:
            paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        error_msg = f"[-] Wordlist not found: {wordlist_file}"
        print(Fore.RED + error_msg + Fore.RESET)
        yield error_msg
        return

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_path = {executor.submit(scan_url, url, path): path for path in paths}

        for future in as_completed(future_to_path):
            result = future.result()
            if result:
                yield result
