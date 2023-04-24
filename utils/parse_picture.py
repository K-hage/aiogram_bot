import aiohttp
from bs4 import BeautifulSoup


async def get_image_links(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

    soup = BeautifulSoup(html, 'html.parser')
    image_links = []
    for img in soup.find_all('img'):
        src = img.get('data-src')
        if img.get('data-src'):
            image_links.append('https://klike.net/' + img.get('data-src'))

    return image_links

