
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    if 'entries' in feed:
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published: {entry.published}")
            print()

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
read_rss_feed(rss_url)
