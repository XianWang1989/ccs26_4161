
import feedparser

# URL of the RSS feed
rss_url = 'https://example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Iterate through the entries
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Published: {entry.published}')
    print(f'Link: {entry.link}\n')
