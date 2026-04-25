
import feedparser

# Function to fetch articles
def fetch_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = feed.entries

    for entry in articles:
        print(entry.title, entry.link)

    # Check for pagination
    # (This depends on how the specific RSS feed handles pagination)
    while hasattr(feed, 'next'):
        feed = feedparser.parse(feed.next)
        articles = feed.entries
        for entry in articles:
            print(entry.title, entry.link)

# Replace with your RSS feed URL
rss_feed_url = "https://example.com/rss"
fetch_articles(rss_feed_url)
