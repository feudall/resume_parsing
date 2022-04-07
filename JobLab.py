from bs4 import BeautifulSoup

import re

import requests

def joblab_resume(**kwargs):
    url_dict = kwargs
    str_out = ''
    try:

        for val, (vacansy, url) in enumerate(url_dict.items()):
            # print(val,vacansy,url)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'lxml')

            hrefs = soup.find_all('p', class_='prof')
            if not hrefs:
                str_out = f'на сегодняшний день новых резюме {vacansy} нет'
                return str_out
            # locols = soup.find_all('p', class_='sshow')
            # names = soup.find_all('p', style="font-size:16px; padding:6px 0 6px 0;")
            # about_mys = soup.find_all('p', {'class':'font14','style':"padding:6px 0 6px 0;"})
            # experiences = soup.find_all('p', style="font-size:14px; padding:6px 0 6px 0; color:#555;")
            maneys = soup.find_all('p', class_='font18')
            data_times = soup.find_all(text=re.compile("(\d\d \w\w\w\w?\w?\w?\w?\w?\w? \d\d\d\d, \d?\d:\d\d?)"))

            for i in range(len(hrefs)):
                title = hrefs[i].find('a').text
                many = maneys[i].text
                link = 'https://joblab.ru/' + hrefs[0].find('a').get('href')
                # data = data_times[i]
                rezyme_str = f' {title} {many}'
                rezyme_str = f'<a href="{link}">{rezyme_str}</a>'
                str_out = str_out + rezyme_str + '<p>'
    except Exception as _ex:
        return f'error {_ex}'
    str_out += '<p>'
    if str_out == '<p>':
        str_out = 'на сегодняшний день новых резюме нет'
        return str_out
    return str_out



if __name__ == '__main__':

        url_dict = {
                    # 'маникюр': 'https://joblab.ru/search.php?r=res&srprofecy=%EC%E0%ED%E8%EA%FE%F0&kw_w2=1&srzpmax=&srregion=50&srcity=&srcategory=&submit=1&srexpir=&srgender=&pred=1',
                    # 'автослесарь':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%F1%EB%E5%F1%E0%F0%FC&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
                    'автомойщик':'https://joblab.ru/search.php?r=res&srprofecy=%E0%E2%F2%EE%EC%EE%E9%F9%E8%EA&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    'арматурщик':'https://joblab.ru/search.php?r=res&srprofecy=%E0%F0%EC%E0%F2%F3%F0%F9%E8%EA&kw_w1=1&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    'автомаляр':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E0%EB%FF%F0&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
                    'жестянщик':'https://joblab.ru/search.php?r=res&srprofecy=%E6%E5%F1%F2%FF%ED%F9%E8%EA&kw_w1=1&kw_w2=1&prof_bl=%E3%E8%E1%F9%E8%EA+%EA%F0%EE%E2%E5%EB%FC%F9%E8%EA+%E2%E5%ED%F2%E5%EB%FF%F6%E8%E8&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    # 'автомеханик':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E5%F5%E0%ED%E8%EA&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1'
                    }
        print(joblab_resume(url_dict))