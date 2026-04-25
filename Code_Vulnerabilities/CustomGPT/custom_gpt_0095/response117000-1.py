
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published
        print(f'Title: {title}\nLink: {link}\nPublished: {published}\n')

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
read_rss_feed(rss_url)
