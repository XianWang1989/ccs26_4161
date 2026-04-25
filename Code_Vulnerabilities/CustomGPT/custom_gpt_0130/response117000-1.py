
import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    # Append articles from the first page
    for entry in feed.entries:
        articles.append((entry.title, entry.link))

    # Check for a next page link if available
    while hasattr(feed, 'next_feed') and feed.next_feed:
        feed = feedparser.parse(feed.next_feed)
        for entry in feed.entries:
            articles.append((entry.title, entry.link))

    return articles

url = "https://example.com/rss"  # Replace with your RSS feed URL
all_articles = fetch_rss_feed(url)

for title, link in all_articles:
    print(f"Title: {title}, Link: {link}")
