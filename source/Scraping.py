from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



class Scraping:
    def __init__(self, url="https://www.pref.miyazaki.lg.jp/kansensho-taisaku/kenko/hoken/covid19.html"):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url
        self.tbody = None

    def request_start(self):
        self.driver.get(self.url)

    def get_table_data(self):
        tbody = self.driver.find_element_by_tag_name('tbody')
        trs = tbody.find_elements(By.TAG_NAME, "tr")
        # print()
        return trs

    def parse_table_data(self):
        pass

if __name__ == '__main__':
    """
    今後の流れいくらでもデータが増えても大丈夫なようにする必要あり
    以下手順
    1. trタグの中のthタグに累計があるとこまでfor文で進む（日時が進むにつれて累計の行番号が変わるため）
    2. その行の中の合計（3）と陽性件数（4）のところまでインデックス指定で取り出す
    3. 取出した値をdata.jsonに書き込む
    4. 終わり
    """
    scraping = Scraping()
    scraping.request_start()
    print(scraping.driver.page_source)
    print("Hello")
    trs = scraping.get_table_data()
    tds = trs[2].find_elements(By.TAG_NAME, "td")
    print(trs[2].text)
    print()
    print(tds[0].text)
    print(len(trs))