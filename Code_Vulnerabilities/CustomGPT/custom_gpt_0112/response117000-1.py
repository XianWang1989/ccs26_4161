
import feedparser
import requests

def fetch_articles(feed_url):
    articles = []
    while feed_url:
        # Parse the RSS feed
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)

        # Check for the next page (this depends on the feed structure)
        feed_url = feed.get('next_page', None)
    return articles

# Example usage
rss_feed_url = 'http://example.com/rss'
articles = fetch_articles(rss_feed_url)

for article in articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print('---')
