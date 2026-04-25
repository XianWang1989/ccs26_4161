
import feedparser

# Replace with your RSS feed URL
rss_url = 'http://example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Iterate through all entries in the feed
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Published: {published}')
    print('---')
