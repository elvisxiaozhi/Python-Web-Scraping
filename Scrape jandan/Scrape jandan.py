import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://jandan.net/ooxx/page-1#comments'

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_page(web_page):
    current_web = BeautifulSoup(web_page, "lxml")
    movie_list = current_web.find('ol', attrs={'class': 'commentlist'})
    for movie in movie_list.find_all('p'):
        print(movie)

web_content = download_page(DOWNLOAD_URL)
parse_page(web_content)
