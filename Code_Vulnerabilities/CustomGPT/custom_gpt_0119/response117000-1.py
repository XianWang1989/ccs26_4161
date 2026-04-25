
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    while feed_url:
        response = requests.get(feed_url)
        feed = feedparser.parse(response.content)

        # Append articles from the current feed
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
            })

        # Try to find the next page URL (this depends on the feed's structure)
        feed_url = next((link.href for link in feed.links if link.rel == 'next'), None)

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

# Print out all articles
for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
