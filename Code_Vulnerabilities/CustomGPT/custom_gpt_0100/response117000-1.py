
import feedparser

def fetch_articles(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Display feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Iterate through feed entries
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}\n")

# Example RSS feed URL
rss_url = 'http://example.com/rss'  # Replace with actual RSS feed URL
fetch_articles(rss_url)
