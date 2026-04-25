
import feedparser
import requests

def fetch_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    # Append the articles from the initial feed
    all_articles.extend(feed.entries)

    # Check for pagination support (if provided in the feed)
    next_page = feed.get('links', [])

    for link in next_page:
        if link.get('rel') == 'next':
            # Assuming 'href' points to the next feed page
            next_feed = feedparser.parse(link['href'])
            all_articles.extend(next_feed.entries)
            break  # Only handle one next page for this example

    return all_articles

# Usage
feed_url = 'http://example.com/rss-feed'
articles = fetch_all_articles(feed_url)

for article in articles:
    print(f'Title: {article.title}, Link: {article.link}')
