
import feedparser

def fetch_articles(feed_url):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)
    articles = []

    # Loop through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check for pagination
    if 'next' in feed:
        next_page_url = feed.next  # Depends on how the feed handles pagination
        articles += fetch_articles(next_page_url)

    return articles

# Example usage
feed_url = 'http://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_articles(feed_url)

# Print all articles
for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
