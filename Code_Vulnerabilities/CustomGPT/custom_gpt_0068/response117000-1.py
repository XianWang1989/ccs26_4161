
import feedparser

# URL of the RSS feed
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL

# Parse the feed
feed = feedparser.parse(rss_url)

# Print all articles in the feed
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print(f'Description: {entry.description}')
    print('---')
