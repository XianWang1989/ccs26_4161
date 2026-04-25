
import feedparser

def fetch_articles(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []

    # Iterate through each entry in the feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_articles(rss_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
