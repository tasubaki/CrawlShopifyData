from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

class ShopifyScraper:
    def __init__(self, webdriver_path):
        self.webdriver_path = webdriver_path
        self.results = []

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Chạy ở chế độ ẩn
        service = Service(self.webdriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def scrape(self, url):
        self.driver.get(url)
        time.sleep(5)  # Chờ trang tải
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        self.extract_data(soup)

    def extract_data(self, soup):
        divs = soup.find_all('div', class_='tw-grid tw-grid-flow-dense tw-items-start tw-gap-gutter--mobile lg:tw-gap-gutter--desktop tw-grid-cols-1 md:tw-grid-cols-2 lg:tw-grid-cols-3 xl:tw-grid-cols-4')
        
        for div in divs:
            divcons = div.find_all("div", {"data-controller": "app-card"})
            for divcon in divcons:
                app_name_tag = divcon.find('a')
                app_name = app_name_tag.get_text(strip=True) if app_name_tag else "N/A"
                link = app_name_tag['href'] if app_name_tag else "N/A"

                rating_tags = divcon.find("span", string=lambda x: x and "out of 5 stars" in x)
                rating = rating_tags.previous_sibling.strip() if rating_tags else "N/A"

                review_count_tags = divcon.find_all('span', class_='tw-sr-only')
                review_count = review_count_tags[1].get_text(strip=True).strip("()") if len(review_count_tags) > 1 else "N/A"

                price_status = divcon.find('span', class_='tw-overflow-hidden tw-whitespace-nowrap tw-text-ellipsis').get_text(strip=True)
                description = divcon.find('div', class_='tw-text-body-xs tw-text-fg-tertiary').get_text(strip=True)

                self.results.append({
                    'App Name': app_name,
                    'Link App': link,
                    'Rating': rating,
                    'Review Count': review_count,
                    'Price Status': price_status,
                    'Description': description
                })

    def save_to_csv(self, file_name):
        if not os.path.exists('results'):
            os.makedirs('results')
        
        file_path = os.path.join('results', file_name)
        df = pd.DataFrame(self.results)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')

    def close_driver(self):
        self.driver.quit()
