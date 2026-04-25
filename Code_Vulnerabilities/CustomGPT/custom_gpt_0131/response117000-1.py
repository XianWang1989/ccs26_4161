
import feedparser

# Function to fetch and parse the RSS feed
def read_rss_feed(feed_url):
    # Parse feed
    feed = feedparser.parse(feed_url)

    articles = []

    # Iterate through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example usage
feed_url = "https://example.com/rss"  # Update with the actual feed URL
all_articles = read_rss_feed(feed_url)

# Print all articles
for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
