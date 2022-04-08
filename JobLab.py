# pip install requests
from bs4 import BeautifulSoup
import requests

def joblab_resume(url):
    global vacansy, list_rezume
    dict_rezyme = {}
    try:
        for val, (vacansy, url) in enumerate(url_dict.items()):
            list_rezume = []
            response = requests.get(url)
            if response.status_code != 200:
                list_rezume.append(f'Ошибка запроса по резюме {vacansy}, сервер не отвечает')
                dict_rezyme[vacansy] = list_rezume
            soup = BeautifulSoup(response.text, 'lxml')
            q = soup.find_all('td', class_="border hhide")
            for e in q:
                er = e.parent
                title = er.find('p', class_='prof').text
                link = 'https://joblab.ru/' + er.find('a').get('href')
                money = er.find('td', class_="hhide680").text
                geo = er.find_all('p', class_="font18")[1].text
                rezyme_str = f' {title}, ЗП {money}, город {geo}.'
                rezyme_str = f'<a href="{link}">{rezyme_str}</a>'
                list_rezume.append(rezyme_str)
            dict_rezyme[vacansy] = list_rezume
    except Exception as _ex:
        list_rezume.append(f'error {_ex}')
        dict_rezyme[vacansy] = list_rezume
        return
    return dict_rezyme



if __name__ == '__main__':

        url_dict = {
                    'test': 'https://joblab.ru/searc',
                    'маникюр': 'https://joblab.ru/search.php?r=res&srprofecy=%EC%E0%ED%E8%EA%FE%F0&kw_w2=1&srzpmax=&srregion=50&srcity=&srcategory=&submit=1&srexpir=&srgender=&pred=1',
                    'автослесарь':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%F1%EB%E5%F1%E0%F0%FC&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
                    'автомойщик':'https://joblab.ru/search.php?r=res&srprofecy=%E0%E2%F2%EE%EC%EE%E9%F9%E8%EA&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    'арматурщик':'https://joblab.ru/search.php?r=res&srprofecy=%E0%F0%EC%E0%F2%F3%F0%F9%E8%EA&kw_w1=1&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    'автомаляр':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E0%EB%FF%F0&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
                    'жестянщик':'https://joblab.ru/search.php?r=res&srprofecy=%E6%E5%F1%F2%FF%ED%F9%E8%EA&kw_w1=1&kw_w2=1&prof_bl=%E3%E8%E1%F9%E8%EA+%EA%F0%EE%E2%E5%EB%FC%F9%E8%EA+%E2%E5%ED%F2%E5%EB%FF%F6%E8%E8&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
                    'автомеханик':'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E5%F5%E0%ED%E8%EA&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1'
                    }
        print(joblab_resume(url_dict))