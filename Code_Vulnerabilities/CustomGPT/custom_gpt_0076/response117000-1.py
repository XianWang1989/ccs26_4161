
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    # Check for entries in the feed
    if feed.entries:
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published: {entry.published}")
            print()  # Add a blank line between articles
    else:
        print("No articles found in the feed.")

# Replace with your RSS feed URL
rss_url = 'https://example.com/rss'
read_rss_feed(rss_url)
