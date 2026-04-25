
import feedparser
import requests

def fetch_articles(rss_url):
    articles = []
    feed = feedparser.parse(rss_url)

    # Process the first page
    articles.extend(feed.entries)

    # Check for pagination (assuming it uses a 'next' link)
    while 'next' in feed:
        next_url = feed['next']
        feed = feedparser.parse(next_url)
        articles.extend(feed.entries)

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
all_articles = fetch_articles(rss_url)

for article in all_articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print(f'Date: {article.published}')
    print('---')
