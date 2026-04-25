
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    parsed_feed = feedparser.parse(feed_url)
    articles.extend(parsed_feed.entries)

    # Check for pagination (this is just an example; the actual logic may vary)
    next_link = parsed_feed.feed.get('next')

    while next_link:
        parsed_feed = feedparser.parse(next_link)
        articles.extend(parsed_feed.entries)
        next_link = parsed_feed.feed.get('next')

    return articles

# Usage example
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print()
