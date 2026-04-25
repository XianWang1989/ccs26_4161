
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        # Parse the feed
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)

        # Check for a next link if your feed supports it
        feed_url = feed.get('feed', {}).get('link', None)  # Modify based on feed structure

        # Some feeds might include a "next" link directly
        for link in feed.links:
            if link.rel == 'next':
                feed_url = link.href
                break
        else:
            feed_url = None  # Exit if no next page

    return articles

# Example usage
url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(url)

for article in all_articles:
    print(article.title)
