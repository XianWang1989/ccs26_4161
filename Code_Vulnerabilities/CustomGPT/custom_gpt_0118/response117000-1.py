
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    next_url = feed_url

    while next_url:
        feed = feedparser.parse(next_url)
        articles.extend(feed.entries)

        # Check for the presence of a "next" page URL in the feed.
        # Adjust this logic based on the specific feed structure.
        next_url = get_next_url(feed)

    return articles

def get_next_url(feed):
    # Example logic to get the next URL (this may vary by feed)
    for link in feed.links:
        if link.rel == 'next':
            return link.href
    return None

# Example usage
feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(article.title, article.link)
