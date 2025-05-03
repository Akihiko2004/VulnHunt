# modules/header_checker.py

import requests
from colorama import Fore

required_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def check(url):
    results = [f"\n[Security Header Check] Target: {url}"]
    try:
        response = requests.get(url, timeout=5)
        missing = []

        for header in required_headers:
            if header not in response.headers:
                missing.append(header)

        if missing:
            message = f"[!] Missing headers: {', '.join(missing)}"
            print(Fore.RED + message + Fore.RESET)
            results.append(message)
        else:
            message = "[+] All essential security headers are present."
            print(Fore.GREEN + message + Fore.RESET)
            results.append(message)

    except requests.exceptions.RequestException:
        error = "[!] Failed to connect to target for header check."
        print(Fore.RED + error + Fore.RESET)
        results.append(error)

    return results
