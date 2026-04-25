
import feedparser

def read_all_articles(feed_url):
    articles = []
    while feed_url:
        print(f"Fetching articles from: {feed_url}")
        feed = feedparser.parse(feed_url)

        # Append articles to the list
        articles.extend(feed.entries)

        # Check for a next link if available, this is not standard for RSS
        feed_url = next((link.href for link in feed.links if link.rel == 'next'), None)

    return articles

# Example RSS feed URL
rss_feed_url = 'http://example.com/feed'  # Replace with your RSS feed URL
all_articles = read_all_articles(rss_feed_url)

# Print titles of all articles
for article in all_articles:
    print(article.title)
