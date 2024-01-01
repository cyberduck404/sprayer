#!/usr/bin/python3
# todo://
#   add proxy
#   -d
import argparse
import urllib.parse
import urllib3
from threading import Thread, Semaphore
from .core.http import fetch
from .core.helper import reader
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# argparse
p = argparse.ArgumentParser()
p.add_argument('-l', '--url-list', required=True, help='Specify URL list')
p.add_argument('-p', '--payload', default='fuckhackerone', help='Specify payload then we roll')
p.add_argument('-k', '--keyword', default='FUZZ', help='URL keyword, default is FUZZ')
# p.add_argument('-d', '--url-dir', help='Specify URL Directory')
p.add_argument('-x', '--proxy', help='Specify your proxy, like http://127.0.0.1:8080')
p.add_argument('-mc', '--max-conn', type=int, default=500, help='Max Concurrency')

# let's go!
def main():
    # parse args
    args = p.parse_args()
    payload = args.payload
    url_list = args.url_list
    proxy = args.proxy
    kwargs = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        },
        'proxies': {'http': proxy, 'https': proxy}
    }

    # sema
    sema = Semaphore(value=args.max_conn)

    # url encode
    e_payload = urllib.parse.quote(payload)

    # read urls
    urls = []
    if url_list:
        urls += reader(url_list)

    # replace payload with keyword
    murls = []
    for url in urls:
        murls.append(url.replace(args.keyword, e_payload))

    # send requests
    ts = []
    for murl in murls:
        t = Thread(target=fetch, args=(murl, payload, sema), kwargs=kwargs)
        t.start()
        ts.append(t)
    for t in ts:
        t.join()


if __name__ == '__main__':
    main()