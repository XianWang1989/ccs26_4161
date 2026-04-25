
import feedparser

def read_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Iterate through entries
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Published: {entry.published}")
        print(f"Link: {entry.link}\n")

# Example RSS Feed URL
url = "https://example.com/rss"  # Replace with your RSS feed URL
read_rss_feed(url)
