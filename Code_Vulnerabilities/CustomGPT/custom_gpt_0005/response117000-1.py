
import feedparser

def read_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)
    all_articles.extend(feed.entries)

    # Check for pagination
    next_url = feed.get('link')
    while next_url:
        next_feed = feedparser.parse(next_url)
        all_articles.extend(next_feed.entries)

        # Update next_url if pagination is available (depends on RSS structure)
        next_url = next_feed.get('next', None)

    return all_articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
articles = read_all_articles(feed_url)

for article in articles:
    print(article.title, article.link)
