
import feedparser

def fetch_all_articles(feed_url):
    all_articles = []
    page_number = 1  # Initialize page number

    while True:
        # Construct the feed URL with pagination if supported (this is hypothetical)
        paginated_url = f"{feed_url}?page={page_number}"
        feed = feedparser.parse(paginated_url)

        # Check if the feed has entries
        if not feed.entries:
            break  # Exit loop if no more entries

        all_articles.extend(feed.entries)  # Add new articles to the list
        page_number += 1  # Increment page number for the next iteration

    return all_articles

# Example usage
feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
articles = fetch_all_articles(feed_url)

for article in articles:
    print(f"Title: {article.title}, Link: {article.link}")
