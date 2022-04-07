# pip install selenium
# pip install undetected-chromedriver
# pip install beautifulsoup4
# pip install lxml

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def get_resumes(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    s = Service(executable_path=r"E:\project\NewParserVacansy\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    str_out = ''
    try:
        # driver.get('https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%BC%D0%B0%D0%BD%D0%B8%D0%BA%D1%8E%D1%80&radius=25&s=104')
        driver.get(url)
        # driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")
        soup = BeautifulSoup(driver.page_source, 'lxml')
        all_rezume = soup.find_all('div', class_='iva-item-content-rejJg')
        for rezume in all_rezume:

            data = rezume.find('div',
                               class_='date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs').text
            if not re.search('(час[ао]?[в]? назад)|(минут[уы]? назад)', data):
                break
            link = 'https://www.avito.ru' + rezume.find('a', class_='iva-item-sliderLink-uLz1v').get(
                'href')  # ссылка на резюме
            title = rezume.find('h3',
                                class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text
            many = rezume.find('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').text

            rezyme_str = f' {title} {many} {data}'
            rezyme_str = f'<a href="{link}">{rezyme_str}</a>'
            str_out = str_out + rezyme_str + '<p>'
        str_out += '<p>'
        if str_out == '<p>':
            str_out = 'на сегодняшний день новых резюме нет'
        print(str_out)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        return str_out


if __name__ == '__main__':
    get_resumes('https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%BC%D0%B0%D0%BD%D0%B8%D0%BA%D1%8E%D1%80&radius=25&s=104')