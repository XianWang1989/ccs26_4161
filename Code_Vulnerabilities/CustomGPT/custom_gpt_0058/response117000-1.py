
import feedparser

# Replace this URL with the RSS feed URL you want to read from
rss_feed_url = 'https://example.com/rss'

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

# Loop through each entry in the feed
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published if 'published' in entry else 'No publish date available'

    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Published: {published}\n')
