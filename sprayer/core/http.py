import sys
import requests
from .checker import check_http


def fetch(url, payload, sema, **kwargs):
    sema.acquire()
    try:
        r = requests.get(
            url,
            headers=kwargs.get('headers', {}),
            proxies=kwargs.get('proxies', {}),
            verify=False,
            allow_redirects=True
        )
        if check_http(r, payload):
            sys.stdout.write(f'{url}\n')
    except requests.exceptions.RequestException as e:
        # sys.stderr.write(f'[!] [{e}] {url}\n')
        pass
    sema.release()