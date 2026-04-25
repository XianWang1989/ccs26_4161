
import feedparser

def get_feed_articles(url):
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example RSS feed URL (Replace with your feed URL)
rss_url = 'http://example.com/rss'
all_articles = get_feed_articles(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
