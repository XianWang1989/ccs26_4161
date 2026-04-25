
import feedparser
import requests

def fetch_rss_feed(feed_url, pages=5):
    articles = []

    for page in range(pages):
        # Construct the URL for the RSS feed, assuming it accepts pagination
        paginated_url = f"{feed_url}?page={page + 1}"  # Adjust based on actual pagination mechanism

        try:
            # Fetch the RSS feed
            response = requests.get(paginated_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the feed
            feed = feedparser.parse(response.content)

            # Collect articles
            articles.extend(feed.entries)

            # If the feed has no more articles, break the loop
            if len(feed.entries) == 0:
                break

        except requests.RequestException as e:
            print(f"Failed to fetch page {page + 1}: {e}")
            break

    return articles

# Example usage:
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_rss_feed(feed_url)

for article in all_articles:
    print(f"Title: {article.title}")
    print(f"Link: {article.link}")
    print(f"Published: {article.published}")
    print("-" * 80)
