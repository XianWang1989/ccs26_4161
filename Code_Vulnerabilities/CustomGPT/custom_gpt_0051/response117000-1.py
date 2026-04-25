
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    page = 1

    while True:
        # Construct the full URL for pagination
        paged_url = f"{feed_url}?page={page}"

        # Fetch and parse the feed
        response = requests.get(paged_url)
        feed = feedparser.parse(response.content)

        # Check if there are articles
        if not feed.entries:
            break  # No more articles to fetch

        articles.extend(feed.entries)
        page += 1  # Move to the next page

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for entry in all_articles:
    print(f"Title: {entry.title}\nLink: {entry.link}\n")
