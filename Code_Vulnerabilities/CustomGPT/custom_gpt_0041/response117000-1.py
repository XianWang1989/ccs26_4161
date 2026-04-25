
import feedparser

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = feed.entries

    # Check if there's a next page or archive
    while hasattr(feed, 'feed') and hasattr(feed.feed, 'next'):
        feed_url = feed.feed.next
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_url)

for article in all_articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}\n')
