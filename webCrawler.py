import requests
import re
from bs4 import BeautifulSoup as bs

start_URL = 'https://www.vit.ac.in'
list_URL = []
soup_dict = {}
list_URL.append(start_URL)
while(len(list_URL) > 0 and len(list_URL)< 150):
    for URL in list_URL:
        r = requests.get(URL)
        #print(r.headers['Content-Type'])
        if not(re.match('text/html',r.headers['Content-Type'])):
            print('Skip')
            list_URL.pop(0)
            continue
        print('HTML')
        if URL in soup_dict:
            print('Skip-Present')
            list_URL.pop(0)
            continue
        #print('Not in present already')
        html_text = r.text
        soup = bs(html_text, 'html.parser')
        soup_dict[URL] = soup
        URL_tags = soup.find_all()
        #URLs_in_this_URL = [tag.find('a').get('href','') if tag.find('a') else '' for tag in URL_tags]
        URLs_in_this_URL = []
        for tag in URL_tags:
            if tag.find('a'):
                link = tag.find('a').get('href','')
                if(re.match('http',link)):
                    URLs_in_this_URL.append(link)
            #URLs_in_this_URL.append(link['href'])
        #print(URLs_in_this_URL)
        list_URL.pop(0)
        list_URL.extend(URLs_in_this_URL)
    break
    
print(soup_dict.keys())
