
import feedparser
import requests

def fetch_articles(feed_url):
    articles = []
    page = 1

    while True:
        # Modify the URL if the feed supports pagination (example: adding "?page={page}")
        response = requests.get(f"{feed_url}?page={page}")
        feed = feedparser.parse(response.content)

        # Break if there are no entries in the feed
        if not feed.entries:
            break

        # Collect articles
        articles.extend(feed.entries)
        page += 1  # Go to the next page

    return articles

# Example usage
feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_articles(feed_url)

for article in articles:
    print(f"Title: {article.title}")
    print(f"Link: {article.link}")
    print(f"Published: {article.published}\n")
