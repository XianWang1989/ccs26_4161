
import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)

    articles = []
    articles.extend(feed.entries)

    # Check if there are additional pages (depends on the specific feed)
    while hasattr(feed, 'link') and feed.link:
        next_feed = feed.link  # Example link; replace with actual pagination logic if available
        feed = feedparser.parse(next_feed)
        articles.extend(feed.entries)

    return articles

# Usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_rss_feed(rss_url)

for article in articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print(f'Summary: {article.summary}\n')
