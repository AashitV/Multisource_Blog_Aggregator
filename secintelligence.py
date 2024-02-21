# secintelligence.py

import requests
from bs4 import BeautifulSoup

def scrape_secintelligence():
    url = 'https://securityintelligence.com/all-articles/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all(class_="article__text_container")

    result_list = []

    for item in articles:
        title_text = item.find('h2',class_='article__title').text.strip()
        link = item.find('a',class_="article__content_link")
        
        result_list.append({"Title": title_text, "Url": link['href']})

    return result_list

