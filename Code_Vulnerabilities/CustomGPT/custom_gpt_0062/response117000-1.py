
import feedparser

def get_all_articles(feed_url):
    # Parse the feed
    feed = feedparser.parse(feed_url)
    articles = []

    # Extract articles from the feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Usage example
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = get_all_articles(feed_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
