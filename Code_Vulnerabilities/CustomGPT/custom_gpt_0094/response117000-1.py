
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Add initial articles
    articles.extend(feed.entries)

    # Check for additional pages if supported (may vary by feed)
    if 'next' in feed:
        next_url = feed.next
        while next_url:
            response = requests.get(next_url)
            feed = feedparser.parse(response.content)
            articles.extend(feed.entries)
            next_url = feed.get('next')

    return articles

# Example usage
if __name__ == "__main__":
    rss_feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
    all_articles = fetch_all_articles(rss_feed_url)

    for article in all_articles:
        print(f'Title: {article.title}')
        print(f'Link: {article.link}\n')
