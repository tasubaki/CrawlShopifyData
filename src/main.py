# main.py

import threading
from scraper import ShopifyScraper
from config import URLS, WEBDRIVER_PATH

def scrape_url(url):
    scraper = ShopifyScraper(WEBDRIVER_PATH)  # Tạo scraper riêng cho mỗi luồng
    scraper.setup_driver()
    scraper.scrape(url)
    
    # Tạo tên file theo từ khóa của URL
    file_name = url.split('=')[1].split('&')[0] + '_search.csv'
    scraper.save_to_csv(file_name)
    scraper.close_driver()

def main():
    threads = []

    for url in URLS:
        thread = threading.Thread(target=scrape_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
