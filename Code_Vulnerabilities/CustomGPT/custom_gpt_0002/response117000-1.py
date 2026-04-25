
import feedparser
import requests

def fetch_all_articles(rss_url):
    articles = []
    # Assuming the feed has paginated links in the `link` or `next` element
    while rss_url:
        feed = feedparser.parse(rss_url)
        articles.extend(feed.entries)
        # Find the link for the next page
        rss_url = feed.get('feed', {}).get('link', None)  # Adjust this line as necessary
    return articles

# Example usage:
rss_feed_url = 'https://example.com/rss'
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(article.title, article.link)
