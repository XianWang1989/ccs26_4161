
import feedparser

def fetch_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    # Loop through the entries (articles)
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example usage
feed_url = 'https://example.com/rss'
all_articles = fetch_articles(feed_url)

for article in all_articles:
    print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
