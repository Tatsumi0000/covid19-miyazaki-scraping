"""
@file: Scraping.py
@author: Tatsumi0000
@brief: 宮崎県のコロナ情報をスクレイピングする
"""
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraping:
    def __init__(self, url="https://www.pref.miyazaki.lg.jp/kansensho-taisaku/kenko/hoken/covid19.html", json_path = "./../data.json"):
        """コンストラクタ
        """
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url
        self.json_path = json_path
        self.json = json.load(open(json_path, 'r'))
        self.covid_data = None
        self.trs = None
        self.tbody = None

    def request_start(self):
        """リクエスト
        """
        self.driver.get(self.url)

    def get_table_data(self):
        """
        コロナ情報が入っているテーブルをタグを指定して取得
        """
        tbody = self.driver.find_element_by_tag_name('tbody')
        self.trs = tbody.find_elements(By.TAG_NAME, "tr")

    def parse_table_data(self):
        """
        テーブルの情報からコロナの
        検査者数と陽性者数を取得し，タプルに格納
        """
        for i in range(len(self.trs)):
            trs = self.trs[i]
            ths = trs.find_elements(By.TAG_NAME, "th")
            tds = trs.find_elements(By.TAG_NAME, "td")
            if ths[0].text == '累計':
                self.covid_data = (tds[3].text, tds[4].text)

    def set_parse_table_data_to_json(self):
        """
        取得したコロナ情報をjsonに格納
        """
        self.json["main_summary"]["value"] = int(self.covid_data[0])
        self.json["main_summary"]["children"][0]["value"] = int(self.covid_data[1])
        json.dump(self.json, open(self.json_path, 'w'), indent=4, ensure_ascii = False)


if __name__ == '__main__':
    """メイン関数的なやつ
    """
    scraping = Scraping()
    scraping.request_start()
    scraping.get_table_data()
    scraping.parse_table_data()
    scraping.set_parse_table_data_to_json()