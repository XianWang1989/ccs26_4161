
import feedparser

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

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_articles(rss_feed_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
