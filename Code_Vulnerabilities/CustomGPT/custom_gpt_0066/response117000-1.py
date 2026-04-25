
import feedparser
import requests

def fetch_rss_articles(feed_url):
    articles = []

    # Fetch the RSS feed
    response = requests.get(feed_url)
    if response.status_code == 200:
        feed = feedparser.parse(response.content)

        # Extract articles from the feed
        articles.extend(feed.entries)

        # Check for pagination (if supported)
        if 'next' in feed:
            next_page_url = feed['next']  # Adjust this according to the feed's structure
            while next_page_url:
                response = requests.get(next_page_url)
                if response.status_code == 200:
                    feed = feedparser.parse(response.content)
                    articles.extend(feed.entries)
                    next_page_url = feed.get('next')  # Update to find the next page
                else:
                    break

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_rss_articles(feed_url)

for article in articles:
    print(article.title)
