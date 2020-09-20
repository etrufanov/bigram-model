import requests
from bs4 import BeautifulSoup
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
for i in range(1,10):
    url = 'https://www.kinopoisk.ru/film/447301/reviews/ord/date/status/all/perpage/200/page/' + str(i)

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('span', class_='_reachbanner_')

    for item in items:
        with open("text.txt", "a") as myfile:
            myfile.write(item.get_text())