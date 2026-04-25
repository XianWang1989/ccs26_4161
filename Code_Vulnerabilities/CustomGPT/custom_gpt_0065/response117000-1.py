
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    for entry in feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print(f'Summary: {entry.summary}')
        print()  # Print an empty line for better readability

# Example usage
rss_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
read_rss_feed(rss_url)
