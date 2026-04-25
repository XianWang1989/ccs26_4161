
import requests
from bs4 import BeautifulSoup

def read_all_articles(rss_url):
    while rss_url:
        response = requests.get(rss_url)
        soup = BeautifulSoup(response.content, 'xml')

        for item in soup.find_all('item'):
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            print(f"Title: {title}")
            print(f"Link: {link}")
            print(f"Published: {pub_date}")
            print()  # Add a blank line between articles

        # Logic for pagination: find 'next' link
        next_page = soup.find('link', rel='next')
        if next_page:
            rss_url = next_page['href']
        else:
            rss_url = None

# Replace with your RSS feed URL
rss_url = 'https://example.com/rss'
read_all_articles(rss_url)
