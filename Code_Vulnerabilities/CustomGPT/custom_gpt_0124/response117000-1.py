
import feedparser

def read_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example Usage
if __name__ == "__main__":
    rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    articles = read_rss_feed(rss_url)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}\n")
