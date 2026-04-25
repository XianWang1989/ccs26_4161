
import feedparser
import requests

def fetch_all_articles(rss_url):
    articles = []
    page_number = 1
    while True:
        # Modify the URL to handle pagination if required
        paginated_url = f"{rss_url}?page={page_number}"  # Adjust according to feed's pagination
        feed = feedparser.parse(paginated_url)

        # Check if there are any entries
        if not feed.entries:
            break

        # Append articles to the list
        articles.extend(feed.entries)
        page_number += 1

    return articles

# Example usage
rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

# Print titles of all articles
for article in all_articles:
    print(article.title)
