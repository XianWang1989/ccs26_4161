
import feedparser

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Store current pagination page
    while True:
        for entry in feed.entries:
            articles.append(entry)

        # Check if there is a link to the next page
        if 'next' in feed.links:
            next_link = feed.links['next'].href
            feed = feedparser.parse(next_link)
        else:
            break

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_url)

for article in all_articles:
    print(article.title)
