
import feedparser

def fetch_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print the titles and links of all articles
    for entry in feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print('---')

# Example usage
rss_url = 'http://example.com/rss'  # Replace with your RSS feed URL
fetch_rss_feed(rss_url)
