# modules/xss_scanner.py

import requests
from colorama import Fore

# You can extend this list or load from a file
xss_payloads = [
    "<script>alert('xss')</script>",
    "'\"><script>alert('xss')</script>",
    "<img src=x onerror=alert('xss')>",
    "<body onload=alert('xss')>"
]

def scan(url, payload_list=None):
    """
    Scan URL for XSS vulnerabilities using provided payloads.
    Yields results live as they are found.
    """
    if payload_list is None:
        payload_list = xss_payloads

    yield f"\n[XSS Test] Target: {url}"

    vulnerable_found = False

    for payload in payload_list:
        test_url = f"{url}?q={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            # Simple check: payload reflected in response?
            if payload in response.text:
                message = f"[!] Possible XSS vulnerability at: {test_url}"
                print(Fore.RED + message + Fore.RESET)
                yield message
                vulnerable_found = True
        except requests.exceptions.RequestException:
            error = f"[!] Error testing for XSS with payload: {payload}"
            print(Fore.RED + error + Fore.RESET)
            yield error

    if not vulnerable_found:
        message = "[+] No XSS vulnerabilities found."
        print(Fore.GREEN + message + Fore.RESET)
        yield message
