
import feedparser

def fetch_articles(feed_url):
    # Parse the initial feed
    feed = feedparser.parse(feed_url)

    articles = []

    # Get articles from the feed
    articles.extend(feed.entries)

    # Check if the feed has a pagination mechanism (e.g., next link)
    while hasattr(feed, 'feed') and 'next' in feed.feed:
        feed_url = feed.feed.next
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)

    return articles

# Example usage
feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_articles(feed_url)

for article in all_articles:
    print(f'Title: {article.title}\nLink: {article.link}\n')
