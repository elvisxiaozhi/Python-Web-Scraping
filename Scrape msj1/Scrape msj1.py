import requests
from bs4 import BeautifulSoup
import urllib.request

downloaded_links = []

def input_link():
    DOWNLOAD_URL = input("Enter the link: ")
    return DOWNLOAD_URL

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_page(web_page):
    current_web = BeautifulSoup(web_page, "lxml")
    link_content = current_web.find('div', attrs={'id': 'content'})
    ul = link_content.find_all('ul', attrs={'class': ''})
    for ul_list in ul:
        li = ul_list.find_all('li')
        for li_list in li:
            link = li_list.find_all('a')
            for link_list in link:
                downloaded_links.append(link_list['href'])
                print(link_list['href']) 

    save_links()

def save_links(): 
    file = open('links.txt', 'w')
    for link in downloaded_links:
        file.write(link + '\n')
    file.close()

url = input_link()
web_page = download_page(url)
url = parse_page(web_page)
