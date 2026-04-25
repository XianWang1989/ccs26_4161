
import feedparser
import requests
from bs4 import BeautifulSoup

# Function to fetch articles from the RSS feed
def fetch_articles(feed_url):
    articles = []

    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    # Add articles from the current feed
    for entry in feed.entries:
        articles.append(entry.title)

    # Example of checking for older articles if pagination links are present
    if 'next_page' in feed:
        # You may need to adapt this if the RSS feed uses a different method for pagination
        next_page_url = feed.next_page
        while next_page_url:
            # Get the next page feed
            feed = feedparser.parse(next_page_url)
            for entry in feed.entries:
                articles.append(entry.title)
            next_page_url = feed.get('next_page')  # Check for the URL of the next page

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
articles = fetch_articles(feed_url)
print("Articles:")
for article in articles:
    print(article)
