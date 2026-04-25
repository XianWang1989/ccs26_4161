
import feedparser
import requests

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = feed.entries

    while 'next' in feed:
        next_url = feed['next']
        feed = feedparser.parse(next_url)
        articles.extend(feed.entries)

    return articles

# Example usage
if __name__ == "__main__":
    rss_url = "https://example.com/rss"  # Replace with your RSS feed URL
    all_articles = fetch_all_articles(rss_url)

    for article in all_articles:
        print(f'Title: {article.title}')
        print(f'Link: {article.link}')
        print('---')
