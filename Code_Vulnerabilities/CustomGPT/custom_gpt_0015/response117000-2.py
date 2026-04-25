
import requests
from bs4 import BeautifulSoup

def scrape_archived_articles(archive_url):
    response = requests.get(archive_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')  # Adjust this based on actual HTML structure
    for article in articles:
        title = article.find('h2').get_text()
        link = article.find('a')['href']
        print(f'Title: {title}')
        print(f'Link: {link}')
        print('---')

archive_url = 'https://example.com/archive'
scrape_archived_articles(archive_url)
