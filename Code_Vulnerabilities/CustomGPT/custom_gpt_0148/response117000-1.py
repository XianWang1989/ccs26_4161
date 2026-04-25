
import feedparser

def read_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Loop through all entries in the feed
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published if 'published' in entry else 'No date available'

        print(f'Title: {title}')
        print(f'Link: {link}')
        print(f'Published: {published}')
        print('-' * 40)

# Example RSS feed URL
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
read_rss_feed(rss_url)
