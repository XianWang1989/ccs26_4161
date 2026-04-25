
import feedparser

def get_all_articles(feed_url):
    # Parse the feed
    feed = feedparser.parse(feed_url)
    articles = []

    # Store all entries
    articles.extend(feed.entries)

    # Check if there are more articles (if pagination is supported)
    # Note: Not all feeds support pagination. This is just a generic example.
    if 'next' in feed:
        while 'next' in feed:
            feed = feedparser.parse(feed['next'])
            articles.extend(feed.entries)

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = get_all_articles(feed_url)

for article in articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}\n')
