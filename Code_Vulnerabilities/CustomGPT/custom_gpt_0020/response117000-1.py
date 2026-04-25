
import feedparser

# Replace with your RSS feed URL
rss_feed_url = 'https://example.com/rss'

# Parse the feed
feed = feedparser.parse(rss_feed_url)

# Check if the feed was successfully parsed
if feed.bozo:
    print("Failed to parse the feed: ", feed.bozo_exception)
else:
    # Loop through the entries in the feed
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published if 'published' in entry else "No publish date"

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Published: {published}")
        print("-" * 40)
