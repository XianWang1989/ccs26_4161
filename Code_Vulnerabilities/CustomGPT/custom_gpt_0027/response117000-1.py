
import feedparser

def fetch_articles(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if 'published' in entry else 'No date provided',
            'summary': entry.summary
        })

    return articles

if __name__ == "__main__":
    rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    articles = fetch_articles(rss_url)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}")
        print(f"Summary: {article['summary']}\n")
