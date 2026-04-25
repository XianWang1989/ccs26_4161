
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    page = 1

    while True:
        # Constructing the URL for the paginated feed
        paginated_url = f"{feed_url}?page={page}"
        feed = feedparser.parse(paginated_url)

        # If there are no more entries, break the loop
        if not feed.entries:
            break

        # Collect articles from the current page
        articles.extend(feed.entries)
        page += 1

    return articles

# Example usage:
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(article.title, article.link)
