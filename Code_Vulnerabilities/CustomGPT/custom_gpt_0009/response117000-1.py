
import feedparser

# Replace with your RSS feed URL
rss_feed_url = 'https://example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

# Loop through and print all articles' titles and links
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print('-' * 40)
