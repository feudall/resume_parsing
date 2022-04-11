# pip install selenium
# pip install undetected-chromedriver
# pip install beautifulsoup4
# pip install lxml

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from JobLab import meseg_compil
from selenium.webdriver.chrome.options import Options

def avito_resumes(url):
    global list_rezume, vacansy
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('headless')
    s = Service(executable_path=r"chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    dict_rezyme = {}
    try:
        for val, (vacansy, url) in enumerate(url.items()):
            list_rezume = []
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            all_rezume = soup.find_all('div', class_='iva-item-content-rejJg')
            for rezume in all_rezume:
                data = rezume.find('div',
                                   class_='date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs').text
                if not re.search('(час[ао]?[в]? назад)|(минут[уы]? назад)', data):
                    break
                link = 'https://www.avito.ru' + rezume.find('a', class_='iva-item-sliderLink-uLz1v').get('href')  # ссылка на резюме
                title = rezume.find('h3',
                                    class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text
                many = rezume.find('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL').text
                rezyme_str = f' {title} {many} {data}'
                rezyme_str = f'<a href="{link}">{rezyme_str}</a>'
                list_rezume.append(rezyme_str)
            dict_rezyme[vacansy] = list_rezume
    except Exception as _ex:
        list_rezume.append(f'error {_ex}')
        dict_rezyme[vacansy] = list_rezume
    finally:
        driver.close()
        driver.quit()
        return meseg_compil(dict_rezyme, 'Avito.ru')
        # messeg_avto = 'Резюме с Avito.ru____________________________________________________________________________<p>'
        # for val, (vacansy, resumes) in enumerate(dict_rezyme.items()):
        #     if resumes:
        #         messeg_avto = messeg_avto + f'Резюме "{vacansy}" за последние сутки<p>'
        #         for resume in resumes:
        #             messeg_avto = messeg_avto + resume + '<p>'
        #     else:
        #         messeg_avto = messeg_avto + f'За последние сутки новых резюме "{vacansy}" нет<p>'
        # return messeg_avto


if __name__ == '__main__':
    dict_url = {
        'test': 'https://joblab.ru/searc',
        # 'автослесарь': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%B0%D1%80%D1%8C&radius=25&s=104',
        # 'автомойщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B9%D1%89%D0%B8%D0%BA&radius=25&s=104',
        # 'арматурщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D1%80%D0%BC%D0%B0%D1%82%D1%83%D1%80%D1%89%D0%B8%D0%BA&radius=25&s=104',
        # 'автомаляр': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D0%BB%D1%8F%D1%80&radius=25&s=104',
        # 'жестянщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B6%D0%B5%D1%81%D1%82%D1%8F%D0%BD%D1%89%D0%B8%D0%BA&radius=25&s=104',
        # 'диагност': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82&radius=25&s=104',
        'маникюр':'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%BC%D0%B0%D0%BD%D0%B8%D0%BA%D1%8E%D1%80&radius=25&s=104'
    }
    print(avito_resumes(dict_url))
