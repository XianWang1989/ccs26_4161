
import feedparser

def fetch_all_articles(rss_url):
    articles = []
    feed = feedparser.parse(rss_url)

    while True:
        # Add fetched entries to the articles list
        articles.extend(feed.entries)

        # Check if there's a next page link
        if 'next' in feed:
            # Update the feedparser to the next page URL
            feed = feedparser.parse(feed['next'])
        else:
            break

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_url)

# Print titles of all articles
for article in all_articles:
    print(article.title)
