
import feedparser

def fetch_rss_articles(feed_url):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    # List to store articles
    articles = []

    # Iterate over feed entries
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        }
        articles.append(article)

    return articles

def print_articles(articles):
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}")
        print('-' * 40)

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_rss_articles(feed_url)
print_articles(articles)
