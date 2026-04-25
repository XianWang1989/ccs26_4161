
import feedparser
import requests

def fetch_all_articles(feed_url):
    all_articles = []
    while feed_url:
        print(f"Fetching articles from: {feed_url}")
        feed = feedparser.parse(feed_url)  # Parse the feed
        all_articles.extend(feed.entries)  # Add entries to the list

        # Check if there is a next page or more articles to fetch
        # (This step is highly dependent on the structure of the specific RSS feed)
        feed_url = None  # Set to None if no pagination is supported
        for link in feed.links:
            if link.rel == 'next':
                feed_url = link.href  # Get the URL for the next page
                break

    return all_articles

# Example usage
rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
articles = fetch_all_articles(rss_feed_url)

# Print titles of all articles
for article in articles:
    print(article.title)
