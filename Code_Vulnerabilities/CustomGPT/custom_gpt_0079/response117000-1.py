
import feedparser
import requests

def fetch_rss_feed(url):
    response = requests.get(url)
    feed = feedparser.parse(response.content)
    return feed

def print_articles(feed):
    for entry in feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print(f'Date: {entry.published}\n')

if __name__ == "__main__":
    rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    feed = fetch_rss_feed(rss_url)
    print_articles(feed)
