# config.py

URLS = [
    'https://apps.shopify.com/search?q=facebook+pixel&st_source=autocomplete',
    'https://apps.shopify.com/search?q=tiktok+pixel&st_source=autocomplete',
    'https://apps.shopify.com/search?q=catalog&st_source=autocomplete',
    'https://apps.shopify.com/search?q=feed'
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "DNT": "1", "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

WEBDRIVER_PATH = 'D:\driver\chromedriver-win64\chromedriver.exe'