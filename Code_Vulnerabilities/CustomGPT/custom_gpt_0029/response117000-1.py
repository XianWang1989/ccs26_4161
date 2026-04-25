
import feedparser

# URL of the RSS feed
rss_url = 'http://example.com/rss'

# Parse the feed
feed = feedparser.parse(rss_url)

# Iterate through feed entries
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print(f'Summary: {entry.summary}\n')

# Checking if there is a pagination link
if 'next' in feed:
    next_url = feed.next.href
    next_feed = feedparser.parse(next_url)
    for entry in next_feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print(f'Summary: {entry.summary}\n')
