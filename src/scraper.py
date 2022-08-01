from bs4 import BeautifulSoup
import requests
import json

html = requests.get('https://unsplash.com/s/photos/vaporwave').text
soup = BeautifulSoup(html, 'lxml')
images = soup.find_all('img', class_ = 'YVj9w')

img_src_list = []
for image in images:
    img_src_list.append('{ image: \'' + image['src'] + '\'},')

