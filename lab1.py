from bs4 import BeautifulSoup
import requests

def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }

    f = open('news.txt', 'w')
    url = 'https://www.omgtu.ru'
    page = requests.get(url, proxies=proxies)

    print(page.status_code)

    filterednews: list = []
    allnews: list = []
    soup = BeautifulSoup(page.text, "html.parser")
    allnews = soup.findAll('a', class_='news-card__link')

    for data in allnews:
        h3 = data.find('h3', class_='news-card__title')
        if h3:
            filterednews.append(h3.text)

    for data in filterednews:
        f.write(data)



parse()
