
import feedparser

def fetch_rss_feed(url):
    # Parsing the feed
    feed = feedparser.parse(url)

    # Print the feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Get and print each article's title and link
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}\n")

# Example RSS feed URL
rss_url = "http://example.com/rss"  # Replace with the actual RSS feed URL

fetch_rss_feed(rss_url)
