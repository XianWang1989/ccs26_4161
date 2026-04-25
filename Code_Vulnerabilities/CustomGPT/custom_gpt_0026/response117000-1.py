
import feedparser

def read_rss_feed(feed_url):
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

# URL of the RSS feed
feed_url = 'http://example.com/rss'
articles = read_rss_feed(feed_url)

# Print all articles
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
