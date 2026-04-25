
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    while True:
        # Append articles from the current feed
        articles.extend(feed.entries)

        # Check for a 'next' link to paginate (if available)
        next_link = next((link.href for link in feed.links if link.rel == 'next'), None)
        if not next_link:
            break  # No more pages to fetch

        # Parse the next feed
        feed = feedparser.parse(next_link)

    return articles


# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for entry in all_articles:
    print(entry.title, entry.link)
