
import feedparser

# Replace with your RSS feed URL
rss_url = 'https://example.com/rss'

def read_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

if __name__ == "__main__":
    articles = read_rss_feed(rss_url)
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}\n")
