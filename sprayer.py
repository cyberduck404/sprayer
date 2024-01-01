#!/usr/bin/python3
import os, sys
import urllib.parse, argparse, gc, logging, json
from threading import Thread
from core.http import fetch
from core.helper import reader


# argparse
p = argparse.ArgumentParser()
p.add_argument('-p', '--payload', required=True, help='Specify payload then we roll')
p.add_argument('-l', '--url-list', required=True, help='Specify URL list')
p.add_argument('-k', '--keyword', default='FUZZ', help='URL keyword, default is FUZZ')
# p.add_argument('-d', '--url-dir', help='Specify URL Directory')

# let's go!
def main():
    # parse args
    args = p.parse_args()
    payload = args.payload
    url_list = args.url_list
    keyword = args.keyword

    # url encode
    e_payload = urllib.parse.quote(payload)

    # read urls
    urls = []
    if url_list:
        urls += reader(url_list)

    # replace payload with keyword
    murls = []
    for url in urls:
        murls.append(url.replace('FUZZ', e_payload))

    # send requests
    ts = []
    for murl in murls:
        t = Thread(target=fetch, args=(murl, payload))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()


if __name__ == '__main__':
    main()