import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
}

def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a', newline='', encoding='utf-8') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts

def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except :
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)

def main():
    while True:
        page = 1
        url = f'\https://catertrax.com/why-catertrax/traxers/page/{str(page)}/'
        articles = get_articles(get_html(url))

        if articles:
            get_page_data(articles)
            page = page + 1
        else:
            break

if __name__ == '__main__':
    main()






