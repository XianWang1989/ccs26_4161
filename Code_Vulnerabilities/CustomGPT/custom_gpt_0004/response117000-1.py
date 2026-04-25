
import feedparser

def fetch_articles(rss_url, num_pages=1):
    articles = []
    for page in range(num_pages):
        # Adjust the URL to fetch different pages if applicable
        # This is an example; adjust 'page' according to the feed structure
        feed_url = f"{rss_url}?page={page + 1}"  # Check if the feed supports pagination
        feed = feedparser.parse(feed_url)

        # Collect articles
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

    return articles

# Example usage
rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
all_articles = fetch_articles(rss_feed_url, num_pages=5)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
