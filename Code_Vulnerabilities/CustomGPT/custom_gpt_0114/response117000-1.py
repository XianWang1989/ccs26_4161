
import feedparser

# URL of the RSS feed
rss_url = 'https://example.com/rss'

# Parse the feed
feed = feedparser.parse(rss_url)

# Loop through the entries and print titles and links
for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}")
    print("---")
