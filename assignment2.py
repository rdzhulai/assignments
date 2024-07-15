import requests
from bs4 import BeautifulSoup
import json

class EbayScraper:
    def __init__(self, url):
        self.url = url
        self.data = {}
    
    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status() 
        return BeautifulSoup(response.text, 'html.parser')

    def parse_data(self, soup):
        self.data['title'] = soup.find('h1', {'class': 'x-item-title__mainTitle'}).find('span').text.strip()
        self.data['image_url'] = soup.find('div', {'class': 'ux-image-carousel-item image-treatment image'}).find('img')['data-src']
        self.data['product_url'] = self.url
        self.data['price'] = soup.find('div', {'class': 'x-price-primary'}).find('span').text.strip()
        self.data['seller'] = soup.find('div', {'class': 'x-sellercard-atf__info__about-seller'})['title'].strip()
        self.data['shipping_price'] = soup.find('div', {'class': 'ux-labels-values__values-content'}).find('span').text.strip()

    def scrape(self):
        soup = self.fetch_page()
        self.parse_data(soup)

if __name__ == "__main__":
    url = 'https://www.ebay.com/itm/256556803147'
    scraper = EbayScraper(url)
    scraper.scrape()
    with open("output.json", 'w', encoding='utf-8') as file:
            json.dump(scraper.data, file, ensure_ascii=False, indent=4)