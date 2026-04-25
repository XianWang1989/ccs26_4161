
import feedparser
import requests

def fetch_rss_articles(feed_url):
    articles = []

    # Initially, set the url to the original feed url
    current_url = feed_url

    while current_url:
        # Parse the RSS feed
        feed = feedparser.parse(current_url)

        # Collect articles from the current feed
        for entry in feed.entries:
            articles.append(entry)

        # Check if there's a link to the next page, 
        # Depending on the feed's pagination structure, you might need to modify this
        current_url = find_next_url(feed)

    return articles

def find_next_url(feed):
    # This function needs to be tailored based on the specific feed's structure
    # Here we just return None as an example; you would need to replace this
    if 'next' in feed:
        return feed['next']
    return None

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_rss_articles(feed_url)

for article in all_articles:
    print(f"Title: {article.title}")
    print(f"Link: {article.link}")
    print(f"Published: {article.published}")
    print('-' * 40)
