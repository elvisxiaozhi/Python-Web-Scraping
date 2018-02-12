import requests
from bs4 import BeautifulSoup
import urllib.request

DOWNLOAD_URL = 'http://www.msj1.com/archives/2121.html'

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_page(web_page):
    current_web = BeautifulSoup(web_page, "lxml")
    link_list = current_web.find('div', attrs={'id': 'content'})
    for i in link_list.find_all('li'):
        link = i.find('a')
        print("link: " , link)
        print("href: ", link['href'])

url = DOWNLOAD_URL
web_page = download_page(url)
url = parse_page(web_page)
