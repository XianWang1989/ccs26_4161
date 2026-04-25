
import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    articles = soup.find_all('item')
    for article in articles:
        title = article.title.text
        link = article.link.text
        pub_date = article.pubDate.text
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Published: {pub_date}\n")

# Example URL
rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
fetch_articles(rss_feed_url)
