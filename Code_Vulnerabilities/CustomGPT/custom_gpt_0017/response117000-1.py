
import feedparser
import requests

def fetch_articles(feed_url):
    articles = []
    while feed_url:
        # Parse the feed
        feed = feedparser.parse(feed_url)

        # Extract articles
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        # Get the URL for the next page of articles
        feed_url = get_next_page(feed)

    return articles

def get_next_page(feed):
    # Check for a 'next' link in the feed (if available)
    if 'links' in feed:
        for link in feed.links:
            if link.rel == 'next':
                return link.href
    return None

# Example usage
feed_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
articles = fetch_articles(feed_url)

# Print the results
for article in articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
