
import feedparser

def fetch_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Assuming feed has 'entries'
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        })

    return articles

if __name__ == "__main__":
    rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    all_articles = fetch_articles(rss_url)

    for article in all_articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}")
        print(f"Summary: {article['summary']}\n")
