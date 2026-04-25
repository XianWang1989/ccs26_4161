
import feedparser

# URL of the RSS feed
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Loop through each article in the feed
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published

    print(f'Title: {title}')
    print(f'Link: {link}')
    print(f'Published: {published}\n')
