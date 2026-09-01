import asyncio
import requests
import aiohttp

async def fetch_url(url):
    for url in urls:
        r = requests.get(url)

async def main():
    urls = ["https://httpbin.org/delay/1", "https://httpbin.org/delay/1", "https://httpbin.org/delay/1"]
    asyncio.gather()