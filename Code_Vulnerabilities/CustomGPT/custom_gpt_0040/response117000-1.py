
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        }
        articles.append(article)

    return articles

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = read_rss_feed(rss_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print('---')
