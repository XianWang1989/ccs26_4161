
import feedparser

def read_all_articles(feed_url):
    all_articles = []
    while feed_url:
        feed = feedparser.parse(feed_url)
        all_articles.extend(feed.entries)

        # Check for next page link (assuming it's in the feed)
        feed_url = None
        for link in feed.links:
            if link.rel == 'next':
                feed_url = link.href
                break

    return all_articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = read_all_articles(feed_url)

for article in articles:
    print(f'Title: {article.title}\nLink: {article.link}\n')
