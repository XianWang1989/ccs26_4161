
import feedparser

def fetch_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    # Check if there are articles in the feed
    if 'entries' in feed:
        all_articles.extend(feed.entries)

    # While there are more articles, fetch next page if available
    while hasattr(feed, 'links'):
        next_link = next((link for link in feed.links if link.rel == "next"), None)
        if next_link:
            feed = feedparser.parse(next_link.href)
            all_articles.extend(feed.entries)
        else:
            break

    return all_articles

# Example usage
feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
articles = fetch_all_articles(feed_url)

for article in articles:
    print(article.title)
