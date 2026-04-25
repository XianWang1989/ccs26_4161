
import feedparser

def fetch_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    while True:
        all_articles.extend(feed.entries)

        # Check if there's a link to the next page
        if 'next' in feed:
            feed_url = feed['next']
            feed = feedparser.parse(feed_url)
        else:
            break

    return all_articles

# Example feed URL (replace with your RSS feed URL)
rss_feed_url = "https://example.com/rss"
articles = fetch_all_articles(rss_feed_url)

for article in articles:
    print(article.title, article.link)
