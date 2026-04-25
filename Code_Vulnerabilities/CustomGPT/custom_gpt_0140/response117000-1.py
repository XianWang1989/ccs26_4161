
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    page = 1
    while True:
        # Construct the URL for the current page
        url = f"{feed_url}?page={page}"
        response = requests.get(url)

        # Check if the response is valid
        if response.status_code != 200:
            break

        # Parse the feed
        feed = feedparser.parse(response.content)

        # Break if there are no entries
        if not feed.entries:
            break

        # Add entries to the articles list
        articles.extend(feed.entries)
        page += 1

    return articles

# Example usage
rss_feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print()
