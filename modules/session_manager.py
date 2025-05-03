# modules/session_manager.py

import requests

def get_session(url, login_url, credentials):
    session = requests.Session()
    payload = {
        'username': credentials['username'],
        'password': credentials['password']
    }
    session.post(login_url, data=payload)
    return session
