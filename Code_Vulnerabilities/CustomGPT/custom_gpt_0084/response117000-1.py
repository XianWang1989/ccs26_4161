
import feedparser

def fetch_all_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Loop through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        })

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
