# modules/xss_scanner.py

import requests
from colorama import Fore

xss_payload = "<script>alert('xss')</script>"

def scan(url):
    results = [f"\n[XSS Test] Target: {url}"]
    test_url = f"{url}?q={xss_payload}"

    try:
        response = requests.get(test_url, timeout=5)
        if xss_payload in response.text:
            message = f"[!] Possible XSS vulnerability at: {test_url}"
            print(Fore.RED + message + Fore.RESET)
            results.append(message)
        else:
            message = "[+] No XSS vulnerabilities found."
            print(Fore.GREEN + message + Fore.RESET)
            results.append(message)
    except requests.exceptions.RequestException:
        error = "[!] Error testing for XSS."
        print(Fore.RED + error + Fore.RESET)
        results.append(error)

    return results
