
import feedparser

def read_rss_feed(feed_url):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        })

    return articles

rss_url = 'https://your-rss-feed-url-here.com/feed'  # Replace with your RSS feed URL
articles = read_rss_feed(rss_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
