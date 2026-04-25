
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        response = requests.get(feed_url)
        feed = feedparser.parse(response.content)

        # Add articles from the current feed
        articles.extend(feed.entries)

        # Check for pagination (this depends on the feed's structure)
        feed_url = getattr(feed, 'next_page', None)  # or any other attribute that points to next page.

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for i, article in enumerate(all_articles, start=1):
    print(f"{i}. {article.title} - {article.link}")
