
import feedparser

def fetch_articles(feed_url):
    # Parse the feed
    feed = feedparser.parse(feed_url)

    # List to store all articles
    articles = []

    # Loop through entries in the feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if hasattr(entry, 'published') else None,
            'summary': entry.summary if hasattr(entry, 'summary') else None
        })

    return articles

# Example RSS feed URL
rss_feed_url = 'https://example.com/rss'
all_articles = fetch_articles(rss_feed_url)

# Print fetched articles
for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
