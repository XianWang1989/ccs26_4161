
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    # Iterate through the entries in the feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
        })

    return articles

if __name__ == "__main__":
    rss_url = 'YOUR_RSS_FEED_URL'
    articles = read_rss_feed(rss_url)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary']}\n")
