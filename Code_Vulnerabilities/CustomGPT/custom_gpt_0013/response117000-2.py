
import requests
from bs4 import BeautifulSoup

def fetch_full_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    articles = []

    for item in soup.find_all('item'):
        articles.append({
            'title': item.title.text,
            'link': item.link.text,
            'description': item.description.text,
        })

    return articles

if __name__ == "__main__":
    rss_url = 'YOUR_RSS_FEED_URL'
    articles = fetch_full_articles(rss_url)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Description: {article['description']}\n")
