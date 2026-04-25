
import feedparser

def read_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    while True:
        all_articles.extend(feed.entries)

        # Check if there is a next page (this is feed-specific)
        if 'next' in feed:
            feed = feedparser.parse(feed.feed.link)  # Adjust according to the feed structure
        else:
            break

    return all_articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = read_all_articles(feed_url)

for article in articles:
    print(article.title)
