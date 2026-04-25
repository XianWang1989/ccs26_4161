
import feedparser
import requests

def fetch_articles(feed_url):
    articles = []
    page = 1

    while True:
        # Make sure to replace with the actual pagination parameter if supported by the feed
        paginated_url = f"{feed_url}?page={page}"
        feed = feedparser.parse(paginated_url)

        # Check if there are any entries
        if not feed.entries:
            break

        articles.extend(feed.entries)
        page += 1

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your actual RSS feed URL
articles = fetch_articles(feed_url)

for article in articles:
    print(f"Title: {article.title}, Link: {article.link}")
