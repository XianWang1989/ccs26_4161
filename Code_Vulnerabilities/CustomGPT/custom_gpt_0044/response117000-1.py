
import feedparser

def fetch_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Append articles from the first page
    articles.extend(feed.entries)

    # Check if there's a link to more articles
    while 'next' in feed:
        feed = feedparser.parse(feed['next'])
        articles.extend(feed.entries)

    return articles

# Example usage
if __name__ == "__main__":
    rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
    all_articles = fetch_articles(rss_feed_url)

    for article in all_articles:
        print(article.title, article.link)
