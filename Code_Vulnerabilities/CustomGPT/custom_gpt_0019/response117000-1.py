
import feedparser

def read_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print("\n")

# Example RSS feed URL
feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
read_rss_feed(feed_url)
