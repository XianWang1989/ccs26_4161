
import feedparser

def fetch_rss_articles(url):
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example RSS feed URL
rss_url = 'https://example.com/rss'  # replace with your RSS feed URL
articles = fetch_rss_articles(rss_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print('---')
