
import feedparser
import requests

def read_all_articles(feed_url):
    articles = []
    while feed_url:
        response = requests.get(feed_url)
        feed = feedparser.parse(response.content)

        # Append articles from the current feed
        articles.extend(feed.entries)

        # Check for pagination and update feed_url if next page exists
        feed_url = None  # Default to None
        if 'next' in feed:
            feed_url = feed['next']  # Update to the next page URL if available

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
all_articles = read_all_articles(rss_feed_url)

for article in all_articles:
    print(article.title, article.link)
