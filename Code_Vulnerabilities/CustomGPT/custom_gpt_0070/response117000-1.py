
import feedparser

def fetch_all_articles(feed_url):
    all_articles = []
    page = 1

    while True:
        # Construct the URL for pagination if supported
        paged_url = f"{feed_url}?page={page}"
        feed = feedparser.parse(paged_url)

        # Check if any entries exist, if not, break the loop
        if not feed.entries:
            break

        # Add articles to the list
        all_articles.extend(feed.entries)
        page += 1

    return all_articles

if __name__ == "__main__":
    feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
    articles = fetch_all_articles(feed_url)

    # Print out titles of all articles
    for article in articles:
        print(article.title)
