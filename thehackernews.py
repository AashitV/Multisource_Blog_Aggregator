import requests
from bs4 import BeautifulSoup

def scrape_thehackernews():
    url = 'https://www.thehackernews.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, features='lxml')
    articles = soup.find_all(class_='body-post clear')

    result_list = []

    for item in articles:
        title_text = item.find('h2', class_='home-title').text.strip()
        link = item.find('a', class_='story-link')
        
        result_list.append({"Title": title_text, "Url": link['href']})

    return result_list

#results = scrape_thehackernews()
#for result in results:
#    print(f"title: {result['Title']}, link: {result['Url']}")
  
