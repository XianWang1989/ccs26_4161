
import feedparser

def read_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)

    articles = []

    # Iterate through articles in the feed
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        }
        articles.append(article)

    return articles

# Usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = read_rss_feed(feed_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}")
    print('-' * 40)
