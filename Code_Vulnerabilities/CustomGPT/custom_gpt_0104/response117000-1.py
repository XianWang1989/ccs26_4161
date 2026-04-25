
import feedparser

def read_all_articles(feed_url):
    all_articles = []
    current_url = feed_url

    while current_url:
        feed = feedparser.parse(current_url)
        all_articles.extend(feed.entries)

        # Assuming there's a 'next' link in the feed, which is common in paginated feeds
        current_url = None
        for link in feed.links:
            if link.rel == 'next':  # Check if there's a 'next' link
                current_url = link.href
                break

    return all_articles

if __name__ == "__main__":
    rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
    articles = read_all_articles(rss_feed_url)

    for article in articles:
        print(f"Title: {article.title}")
        print(f"Link: {article.link}\n")
