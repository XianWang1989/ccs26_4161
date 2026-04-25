
import feedparser

# URL of the RSS feed
feed_url = "https://example.com/rss"

# Parse the feed
feed = feedparser.parse(feed_url)

# Iterate over entries
for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}")
    print(f"Summary: {entry.summary}\n")

# Check if there's a way to paginate (e.g., using next page link)
if 'links' in feed:
    for link in feed.links:
        if link.rel == 'next':
            next_page_url = link.href
            # You can call feedparser again on next_page_url
