import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250/'

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_page(web_page):
    current_web = BeautifulSoup(web_page, "lxml")
    movie_list = current_web.find('ol', attrs={'class': 'grid_view'})

    movie_name_list = []

    for i in movie_list.find_all('li'):
        name = i.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(name)
        print(name)

    has_next_page = current_web.find('span', attrs={'class': 'next'}).find('a')
    if has_next_page:
        return movie_name_list, DOWNLOAD_URL + has_next_page['href']
    return movie_name_list, None


url = DOWNLOAD_URL
while url:
    web_page = download_page(url)
    movie_name_list, url = parse_page(web_page)
