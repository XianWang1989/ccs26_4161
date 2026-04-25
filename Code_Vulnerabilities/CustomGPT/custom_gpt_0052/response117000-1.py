
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print()

    return feed

# Example usage
url = 'https://example.com/rss'  # Replace with your RSS feed URL
feed = read_rss_feed(url)
