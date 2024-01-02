#!/usr/bin/python3
# todo://
#   -d
import argparse, gc
import urllib.parse
import urllib3
import asyncio, aiohttp
from .core.http import async_request
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
p.add_argument('-sw', '--single-waiting', type=int, default=30, help='Aiohhtp single waiting')

# parse args
args = p.parse_args()
payload = args.payload
url_list = args.url_list
max_conn = args.max_conn
single_waiting = args.single_waiting
proxy = args.proxy
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# let's go!
async def main():
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
    length = len(murls)

    # send requests
    count = 0
    timeout = aiohttp.ClientTimeout(total=single_waiting, sock_connect=single_waiting, sock_read=single_waiting)
    connector = aiohttp.TCPConnector(limit=max_conn, ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector, timeout=timeout) as s:
        while count < length:
            tasks = []
            sliced = murls[count:count + max_conn]
            for domain in sliced:
                tasks.append(asyncio.ensure_future(async_request(s, domain, payload, proxy=args.proxy)))
            await asyncio.gather(*tasks)
            s.cookie_jar.clear()

            # the end of loop
            del tasks
            gc.collect()
            count += max_conn


if __name__ == '__main__':
    asyncio.run(main())