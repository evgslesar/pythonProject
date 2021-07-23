import requests
from bs4 import BeautifulSoup

ITEMS = 100


headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive'
}

def extract_max_page(url):
  hh_requests = requests.get(url, headers=headers)
  hh_soup = BeautifulSoup(hh_requests.text, 'html.parser')
  pages = []
  paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})
  for page in paginator:
    pages.append(int(page.find('a').text))
  return pages[-1]

def extract_job(html):
  title = html.find('a').text
  link = html.find('a')['href']
  company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text
  company = company.strip()
  location = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
  location = location.partition(',')[0]
  return {'title': title, 'company': company, 'location': location, 'link': link}


def extract_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    result = requests.get(f'{url}&page={page}', headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': 'vacancy-serp-item'})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(keyword):
  url = f'https://hh.ru/search/vacancy?st=searchVacancy&text={keyword}&items_on_page={ITEMS}'
  max_page = extract_max_page(url)
  jobs = extract_jobs(max_page, url)
  return jobs
