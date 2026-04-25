
import feedparser

def read_rss_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary
        }
        articles.append(article)

    return articles

if __name__ == "__main__":
    rss_url = "http://example.com/rss"  # Replace with your RSS feed URL
    all_articles = read_rss_articles(rss_url)

    for article in all_articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}")
        print(f"Summary: {article['summary']}\n")
