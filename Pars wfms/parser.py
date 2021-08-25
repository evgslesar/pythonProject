import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jaguar/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
           'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')

    cars = []
    for item in items:
        uah_price = item.find('span', class_='size16')
        if uah_price:
            uah_price = uah_price.get_text().strip()
        else:
            uah_price = 'Нет данных'
        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text().strip(),
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'usd_price': item.find('span', class_='size22').get_text().strip(),
            'uah_price': uah_price,
            'city': item.find('span', class_='item region').get_text().strip(),
        })

    return cars

def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(['Марка', 'Ссылка', 'Цена в usd', 'Цена в uah', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'],
                             item['uah_price'], item['city'], ])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
        print(f'Получено {len(cars)} автомобилей')
    else:
        print('Error')

parse()
