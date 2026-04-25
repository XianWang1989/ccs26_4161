
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Extract articles from the first page
    articles.extend(feed.entries)

    # Check for additional pages in feed (if supported)
    # This depends on whether the feed supports pagination
    if 'next' in feed:
        while feed.get('next'):
            feed = feedparser.parse(feed.get('next'))
            articles.extend(feed.entries)

    return articles

# Example usage
feed_url = "https://example.com/rss"
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(article.title)
    print(article.link)
