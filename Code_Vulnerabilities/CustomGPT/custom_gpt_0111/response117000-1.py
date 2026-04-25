
import feedparser

def fetch_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    while True:
        all_articles.extend(feed.entries)

        # Check for a 'next' link in the feed
        if 'next' in feed:
            feed_url = feed['next']
            feed = feedparser.parse(feed_url)
        else:
            break

    return all_articles

# Usage
rss_feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_all_articles(rss_feed_url)

for article in articles:
    print(article.title, article.link)
