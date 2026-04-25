
import feedparser
import requests

def fetch_all_articles(feed_url):
    # Store articles in a list
    all_articles = []

    while True:
        # Parse the feed
        feed = feedparser.parse(feed_url)

        # Add new articles to the list
        all_articles.extend(feed.entries)

        # Check if there's a 'next' link in the feed for pagination
        if 'next' in feed:
            feed_url = feed['next']
        else:
            break  # Exit loop if no more pages

    return all_articles

# Example usage
if __name__ == "__main__":
    rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    articles = fetch_all_articles(rss_feed_url)

    # Print the titles of all articles
    for article in articles:
        print(article.title, article.link)
