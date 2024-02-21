import requests
from bs4 import BeautifulSoup

def scrape_itsecguru():
    url = 'https://www.itsecurityguru.org'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')

    result_list = []

    for item in articles:
        title_text = item.find('h3').text.strip()
        link = item.find('a')
        
        result_list.append({"Title": title_text, "Url": link['href']})

    return result_list

