import sys
import requests
from .checker import check_http


def fetch(url, payload):
    try:
        r = requests.get(url)
        if check_http(r, payload):
            sys.stdout.write(f'{url}\n')
    except requests.exceptions.RequestException as e:
        sys.stderr.write(f'[!] [{e}] {url}')