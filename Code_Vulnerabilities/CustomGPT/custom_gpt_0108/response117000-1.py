
import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    # Check if the feed has entries
    if feed.entries:
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary
            })
    return articles

# Replace with your RSS feed URL
rss_url = 'https://example.com/rss'
all_articles = fetch_rss_feed(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
