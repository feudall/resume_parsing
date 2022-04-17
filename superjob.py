# pip install requests
# pip install bs4
# pip install lxml

from bs4 import BeautifulSoup
import requests

def meseg_compil(dict_mes, name):
    messeg_superjob = f'______________________________________<p>Резюме с {name}<p>______________________________________<p>'
    for val, (vacansy, resumes) in enumerate(dict_mes.items()):
        if resumes:
            messeg_superjob = messeg_superjob + f'Резюме "{vacansy}" за последние сутки >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><p>'
            for resume in resumes:
                messeg_superjob = messeg_superjob + resume + '<p>'
        else:
            messeg_superjob = messeg_superjob + f'За последние сутки новых резюме "{vacansy}" нет <p>'
    return messeg_superjob


def superjob_resumes(url_dict):
    global vacansy, list_rezume
    dict_rezyme = {}
    headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    try:
        for val, (vacansy, url) in enumerate(url_dict.items()):
            list_rezume = []
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                list_rezume.append(f'Ошибка запроса по резюме "{vacansy}", сервер не отвечает')
                dict_rezyme[vacansy] = list_rezume
                continue
            soup = BeautifulSoup(response.text, 'lxml')
            blocs = soup.find_all('div', class_="Qh7ZP _2OUfT _15EZz")
          
            # blocs = soup.find_all('div', class_="_3igJl _3lK_W ljjt-")
            for bloc in blocs:               
                title = bloc.find('span', class_='_1Ijga').text
                link = 'https://www.superjob.ru' + bloc.find('a').get('href')
                money = bloc.find('span', class_="VqAHI _1CLYJ _1TcZY dAWx1").text
                geo = bloc.find('span', class_="_4uUzb _1TcZY mO3i1 Bbtm8").text
                rezyme_str = f' {title}, ЗП {money}, город {geo}.'
                rezyme_str = f'<a href="{link}">{rezyme_str}</a>'
                list_rezume.append(rezyme_str)
            dict_rezyme[vacansy] = list_rezume
        return meseg_compil(dict_rezyme, 'superjob.ru')
    except Exception as _ex:
        list_rezume.append(f'error {_ex}')
        dict_rezyme[vacansy] = list_rezume
        return meseg_compil(dict_rezyme, 'superjob.ru')





if __name__ == '__main__':

        url = {
                # 'test': 'https://joblab.ru/searc',
                # 'маникюр': 'https://www.superjob.ru/resume/manikyur.html?period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=3554&t%5B9%5D=1580&t%5B10%5D=1694&t%5B11%5D=880',
                'автослесарь': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%20%2F%20%D0%90%D0%B2%D1%82%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%B0%D1%80%D1%8C%20%2F%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%20%2F%20%D0%BC%D0%BE%D1%82%D0%BE%D1%80%D0%B8%D1%81%D1%82%20&keywords%5B0%5D%5Bskwc%5D=or&keywords%5B0%5D%5Bsrws%5D=7&period=1&catalogues%5B0%5D=363&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
                'автомойщик': 'https://www.superjob.ru/resume/avtomojschik.html?t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=3554&t%5B9%5D=1580&t%5B10%5D=1694&t%5B11%5D=880',
                'арматурщик': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%90%D1%80%D0%BC%D0%B0%D1%82%D1%83%D1%80%D1%89%D0%B8%D0%BA&keywords%5B0%5D%5Bskwc%5D=or&keywords%5B0%5D%5Bsrws%5D=60&keywords%5B1%5D%5Bkeys%5D=%D0%B1%D0%B5%D1%82%D0%BE%D0%BD%D1%89%D0%B8%D0%BA&keywords%5B1%5D%5Bskwc%5D=nein&keywords%5B1%5D%5Bsrws%5D=7&period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
                'автомаляр': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D0%BB%D1%8F%D1%80&keywords%5B0%5D%5Bskwc%5D=and&keywords%5B0%5D%5Bsrws%5D=60&keywords%5B1%5D%5Bkeys%5D=%D0%9C%D0%B0%D0%BB%D1%8F%D1%80%20%D0%BF%D0%BE%20%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83&keywords%5B1%5D%5Bskwc%5D=nein&keywords%5B1%5D%5Bsrws%5D=7&period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
                'жестянщик': 'https://www.superjob.ru/resume/avtozhestyanschik.html?period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
                'автомеханик': 'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E5%F5%E0%ED%E8%EA&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1'
                }
        print(superjob_resumes(url))