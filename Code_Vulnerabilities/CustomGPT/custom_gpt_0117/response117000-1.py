
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        # Parse the RSS feed
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)  # Add the articles from current feed

        # Find the next link (if available)
        feed_url = None
        for link in feed.links:
            if link.rel == 'next':
                feed_url = link.href
                break
    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f'Title: {article.title}, Link: {article.link}')
