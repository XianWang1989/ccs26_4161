
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Append initial articles
    articles.extend(feed.entries)

    # Check for additional pages (depends on the feed structure)
    while hasattr(feed, 'next_page'):
        feed_url = feed.next_page
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)  # Append new articles

    return articles

# Example usage
feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(article.title)  # Print article titles
    print(article.link)   # Print article links
