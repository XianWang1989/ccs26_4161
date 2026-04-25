
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        feed = feedparser.parse(feed_url)

        # Collect articles from the current page
        for entry in feed.entries:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published
            })

        # Check for the next link in the feed
        feed_url = None
        for link in feed.links:
            if link.rel == 'next':  # This may vary based on the feed
                feed_url = link.href
                break

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
