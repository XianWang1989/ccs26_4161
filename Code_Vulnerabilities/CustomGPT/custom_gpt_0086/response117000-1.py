
import feedparser
import time

# Function to fetch articles from an RSS feed
def fetch_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example RSS feed URL
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL

# Store seen articles to avoid duplicates
seen_articles = set()

while True:
    articles = fetch_articles(feed_url)

    for article in articles:
        if article['link'] not in seen_articles:
            print(f"New Article: {article['title']}")
            print(f"Link: {article['link']}")
            seen_articles.add(article['link'])

    # Wait for a while before fetching new articles
    time.sleep(3600)  # Fetch after every hour
