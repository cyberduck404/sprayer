import sys
import asyncio, aiohttp
from .checker import check_http


async def async_request(session, url, payload, proxy=None):
    try:
        async with session.get(url, proxy=proxy, allow_redirects=False) as resp:
            text = await resp.text()
            if check_http(text, payload):
                sys.stdout.write(f'{url}\n')
    except (
        asyncio.TimeoutError,
        aiohttp.ClientConnectorCertificateError,
        aiohttp.ClientConnectionError,
        aiohttp.ClientOSError,
        aiohttp.ClientConnectorError,
        aiohttp.ClientProxyConnectionError,
        aiohttp.ClientSSLError,
        aiohttp.ClientConnectorSSLError,
        aiohttp.ClientPayloadError,
        aiohttp.ClientResponseError,
        aiohttp.ClientHttpProxyError,
        aiohttp.WSServerHandshakeError,
        aiohttp.ContentTypeError,
    ) as e:
        ...
    except RuntimeError as e:
        ...
    except UnicodeDecodeError as e:
        ...