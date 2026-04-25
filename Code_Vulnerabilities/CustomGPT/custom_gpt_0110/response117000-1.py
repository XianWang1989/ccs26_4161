
import feedparser

# URL of the RSS feed
rss_url = 'https://example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Print the titles and links of articles
for entry in feed.entries:
    print(f'Title: {entry.title}')
    print(f'Link: {entry.link}')
    print('---')

# Check for a link to older articles (common in some feeds)
if 'next' in feed:
    next_url = feed.next
    # Repeat parsing for the next page
    next_feed = feedparser.parse(next_url)
    for entry in next_feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print('---')
