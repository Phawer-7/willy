import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    r.encoding = "utf8"
    return r.text


def get_horoscope(html):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find('div', class_='horoBlock').find("p").string
    return text


def get_today(sign):
    link = f"https://orakul.com/horoscope/astrologic/more/{sign}/today.html"
    return get_horoscope(get_html(link))
