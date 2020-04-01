from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver

class Scraping:
    def __init__(self, url="https://www.pref.miyazaki.lg.jp/kansensho-taisaku/kenko/hoken/covid19.html"):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url

    def request_start(self):
        self.driver.get(self.url)


if __name__ == '__main__':
    scraping = Scraping()
    scraping.request_start()
    print(scraping.driver.page_source)