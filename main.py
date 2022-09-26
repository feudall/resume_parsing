from AvitoPars import avito_resumes
from JobLab import joblab_resumes
# from SuperJob import superjob_resumes
import smtplib
from email.mime.text import MIMEText
import time


def send_email(recipient, message):
    sender = 'evdatogly@gmail.com'
    password = 'rwvtdbdcvlhjzoue'                               #'asdLk32@)'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message, 'html')
        msg['Subject'] = 'Резюме за последнии сутки'
        server.sendmail(sender, recipient, msg.as_string())

        return "отравленно"
    except Exception as _ex:
        return f'error {_ex}'


def loop(start, joblab_url, avito_url, superjob_url):
    time_pars = start  # пример '07:00'
    print('script run', time.asctime())
    print('run time', start)

    while True:
        timee = time.asctime()[11:-8]
        if timee == time_pars:
            print('start pars', time.asctime())
            resumes_joblab = joblab_resumes(joblab_url)
            print('end pars joblab', time.asctime())
            resumes_avito = avito_resumes(avito_url)
            print('end pars avito', time.asctime())
            # resumes_superjob = superjob_resumes(superjob_url)
            print('end pars superjob', time.asctime())
            allmessage = resumes_joblab + '<p><p>' + resumes_avito # + '<p><p>' + resumes_superjob
            print('end pars', time.asctime())
            send_email('joker13joker@mail.ru', allmessage)
            send_email('d.lobanov@delfinrus.com', allmessage)
            send_email('a.dediakin@delfinrus.com', allmessage)
            print('message send')
            time.sleep(60)
            # continue

        time.sleep(30)


if __name__ == '__main__':
    url_avito = {
        # 'test': 'https://joblab.ru/searc',
        'автослесарь': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%B0%D1%80%D1%8C&radius=25&s=104',
        'автомойщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B9%D1%89%D0%B8%D0%BA&radius=25&s=104',
        'арматурщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D1%80%D0%BC%D0%B0%D1%82%D1%83%D1%80%D1%89%D0%B8%D0%BA&radius=25&s=104',
        'автомаляр': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D0%BB%D1%8F%D1%80&radius=25&s=104',
        'жестянщик': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B6%D0%B5%D1%81%D1%82%D1%8F%D0%BD%D1%89%D0%B8%D0%BA&radius=25&s=104',
        'диагност': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%B4%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE%D1%81%D1%82&radius=25&s=104',
        # 'маникюр': 'https://www.avito.ru/pushkino/rezume?bt=1&geoCoords=56.043787%2C37.887171&q=%D0%BC%D0%B0%D0%BD%D0%B8%D0%BA%D1%8E%D1%80&radius=25&s=104'
    }
    url_joblab = {
        # 'test': 'https://joblab.ru/searc',
        # 'маникюр': 'https://joblab.ru/search.php?r=res&srprofecy=%EC%E0%ED%E8%EA%FE%F0&kw_w2=1&srzpmax=&srregion=50&srcity=&srcategory=&submit=1&srexpir=&srgender=&pred=1',
        'автослесарь': 'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%F1%EB%E5%F1%E0%F0%FC&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
        'автомойщик': 'https://joblab.ru/search.php?r=res&srprofecy=%E0%E2%F2%EE%EC%EE%E9%F9%E8%EA&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
        'арматурщик': 'https://joblab.ru/search.php?r=res&srprofecy=%E0%F0%EC%E0%F2%F3%F0%F9%E8%EA&kw_w1=1&kw_w2=1&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
        'автомаляр': 'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E0%EB%FF%F0&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1',
        'жестянщик': 'https://joblab.ru/search.php?r=res&srprofecy=%E6%E5%F1%F2%FF%ED%F9%E8%EA&kw_w1=1&kw_w2=1&prof_bl=%E3%E8%E1%F9%E8%EA+%EA%F0%EE%E2%E5%EB%FC%F9%E8%EA+%E2%E5%ED%F2%E5%EB%FF%F6%E8%E8&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&pred=1&submit=1',
        'автомеханик': 'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E5%F5%E0%ED%E8%EA&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1'
    }
    url_superjob = {
        # 'test': 'https://joblab.ru/searc',
        'автослесарь': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%9C%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%20%2F%20%D0%90%D0%B2%D1%82%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%B0%D1%80%D1%8C%20%2F%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%BA%20%2F%20%D0%BC%D0%BE%D1%82%D0%BE%D1%80%D0%B8%D1%81%D1%82%20&keywords%5B0%5D%5Bskwc%5D=or&keywords%5B0%5D%5Bsrws%5D=7&period=1&catalogues%5B0%5D=363&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
        'автомойщик': 'https://www.superjob.ru/resume/avtomojschik.html?t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=3554&t%5B9%5D=1580&t%5B10%5D=1694&t%5B11%5D=880',
        'арматурщик': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%90%D1%80%D0%BC%D0%B0%D1%82%D1%83%D1%80%D1%89%D0%B8%D0%BA&keywords%5B0%5D%5Bskwc%5D=or&keywords%5B0%5D%5Bsrws%5D=60&keywords%5B1%5D%5Bkeys%5D=%D0%B1%D0%B5%D1%82%D0%BE%D0%BD%D1%89%D0%B8%D0%BA&keywords%5B1%5D%5Bskwc%5D=nein&keywords%5B1%5D%5Bsrws%5D=7&period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
        'автомаляр': 'https://www.superjob.ru/resume/search_resume.html?keywords%5B0%5D%5Bkeys%5D=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D0%BB%D1%8F%D1%80&keywords%5B0%5D%5Bskwc%5D=and&keywords%5B0%5D%5Bsrws%5D=60&keywords%5B1%5D%5Bkeys%5D=%D0%9C%D0%B0%D0%BB%D1%8F%D1%80%20%D0%BF%D0%BE%20%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83&keywords%5B1%5D%5Bskwc%5D=nein&keywords%5B1%5D%5Bsrws%5D=7&period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
        'жестянщик': 'https://www.superjob.ru/resume/avtozhestyanschik.html?period=1&t%5B0%5D=1430&t%5B1%5D=1394&t%5B2%5D=1507&t%5B3%5D=3011&t%5B4%5D=1396&t%5B5%5D=2899&t%5B6%5D=881&t%5B7%5D=849&t%5B8%5D=1580&t%5B9%5D=1694&t%5B10%5D=880&t%5B11%5D=3554',
        'автомеханик': 'https://joblab.ru/search.php?srprofecy=%E0%E2%F2%EE%EC%E5%F5%E0%ED%E8%EA&kw_w1=1&kw_w2=1&prof_bl=&srregion=50&srcity%5B%5D=23&srcity%5B%5D=32&srcity%5B%5D=115&srcity%5B%5D=103&srcity%5B%5D=71&srcity%5B%5D=24&srcity%5B%5D=102&srcity%5B%5D=104&srcity%5B%5D=42&srcity%5B%5D=87&srcity%5B%5D=127&srcity%5B%5D=83&srcity%5B%5D=88&srcity%5B%5D=47&srcity%5B%5D=58&srcity%5B%5D=219&srcity%5B%5D=84&srcity%5B%5D=56&srcity%5B%5D=90&srcity%5B%5D=62&srzpmin=&srzpmax=&srexpir=&srgender=&sragemin=&sragemax=&citizen=&lng=&pred=1&r=res&submit=1'
    }
    loop('07:00', url_joblab, url_avito, url_superjob)
