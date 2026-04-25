
import feedparser

def read_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Check if feed is successfully parsed
    if feed.bozo:
        print(f"Error while parsing the feed: {feed.bozo_exception}")
        return

    # Print feed title
    print(f"Feed Title: {feed.feed.title}\n")

    # Loop through feed entries 
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}\n")
        print(f"Summary: {entry.summary}\n")
        print("===================================")

# URL of the RSS feed
rss_url = 'https://example.com/rss-feed.xml'  # Replace with the actual RSS feed URL

# Call the function to read RSS feed
read_rss_feed(rss_url)
