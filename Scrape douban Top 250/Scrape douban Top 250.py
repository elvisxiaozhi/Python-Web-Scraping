import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

DOWNLOAD_URL = 'http://movie.douban.com/top250/'
movie_names_list = []
movie_stars_list = []
movie_years_list = []

def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parse_page(web_page):
    current_web = BeautifulSoup(web_page, "lxml")
    movie_list = current_web.find('ol', attrs={'class': 'grid_view'})

    for i in movie_list.find_all('li'):
        name = i.find('span', attrs={'class': 'title'}).getText()
        star = i.find('span', attrs={'class': 'rating_num'}).getText()
        year_country = i.find('div', attrs={'class': 'bd'}).getText()
        movie_names_list.append(name)
        movie_stars_list.append(star)
        print(name)
        print(star)
        for year in year_country.split():
        	if year.isdigit():
        		movie_years_list.append(year)
        		print(year)
        
    has_next_page = current_web.find('span', attrs={'class': 'next'}).find('a')
    if has_next_page:
        return DOWNLOAD_URL + has_next_page['href']
    return None

def write_xml():
	xml_root = ET.Element("MovieList")
	for movie_name, movie_star, movie_year in zip(movie_names_list, movie_stars_list, movie_years_list):
		xml_title = ET.SubElement(xml_root, "Title").text = movie_name
		xml_star = ET.SubElement(xml_root, "Star").text = movie_star
		xml_year = ET.SubElement(xml_root, "Year").text = movie_year
	print("Finished writing xml file")
	tree = ET.ElementTree(xml_root)
	tree.write("douban_top250.xml", encoding = "utf-8")


url = DOWNLOAD_URL
while url:
	web_page = download_page(url)
	url = parse_page(web_page)
print("Finished scraping")
write_xml()