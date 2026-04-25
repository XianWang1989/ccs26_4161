
import feedparser
import requests

def read_all_articles(feed_url):
    # Make a request to the RSS feed
    response = requests.get(feed_url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the feed
    feed = feedparser.parse(response.content)

    # List to hold all articles
    all_articles = []

    # Loop through the feed entries
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        }
        all_articles.append(article)

    return all_articles

# Example usage
feed_url = "https://example.com/rss"  # Replace with a valid RSS feed URL
articles = read_all_articles(feed_url)

# Print all articles
for article in articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
