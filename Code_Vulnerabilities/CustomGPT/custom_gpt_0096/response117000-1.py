
import feedparser

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Loop through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example usage
feed_url = 'https://example.com/rss'
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
