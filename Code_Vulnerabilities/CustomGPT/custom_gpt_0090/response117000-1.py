
import feedparser
import requests

def read_rss_feed(url):
    feed = feedparser.parse(url)

    # Print all articles
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print()

# Example RSS feed URL
rss_url = 'https://example.com/rss'
read_rss_feed(rss_url)
