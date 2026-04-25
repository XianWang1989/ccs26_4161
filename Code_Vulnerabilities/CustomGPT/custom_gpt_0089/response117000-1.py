
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    # Print feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Loop through the entries in the feed
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Published: {entry.published}")
        print(f"Link: {entry.link}\n")

# Example RSS feed URL
rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
read_rss_feed(rss_feed_url)
