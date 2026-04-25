
import feedparser

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Collect articles from the feed
    articles.extend(feed.entries)

    # Check if there is pagination in the feed (Note: This highly depends on the feed structure)
    while 'next' in feed:
        feed = feedparser.parse(feed.feed.link)
        articles.extend(feed.entries)

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_all_articles(rss_url)

for article in articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print('---')
