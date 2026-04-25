
import feedparser

def read_rss_feed(feed_url):
    # Parse the feed
    feed = feedparser.parse(feed_url)

    # Print the feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Iterate through the entries in the feed
    for entry in feed.entries:
        # Print the title and link of each article
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}\n")

    # Check if there is a next page link (this will depend on the feed structure)
    if 'next' in feed:
        next_feed_url = feed['next']
        print(f"Fetching next page of articles from: {next_feed_url}\n")
        read_rss_feed(next_feed_url)  # Recursively fetch articles from the next page

# Example usage
rss_feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
read_rss_feed(rss_feed_url)
