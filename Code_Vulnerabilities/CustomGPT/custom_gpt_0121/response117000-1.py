
import feedparser

def fetch_rss_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Add articles from the current feed
    articles.extend(feed.entries)

    # Check for a next page (this largely depends on the RSS feed specifications)
    while 'next' in feed:
        # Update the feed URL to the next page
        feed_url = feed['next']
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)

    return articles

# Usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_rss_articles(feed_url)

# Printing title and link of each article
for article in all_articles:
    print(f"Title: {article.title}")
    print(f"Link: {article.link}")
    print('-' * 80)
