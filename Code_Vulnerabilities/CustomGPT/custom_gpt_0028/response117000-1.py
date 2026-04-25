
import feedparser

def read_rss_feed(url):
    articles = []
    while url:
        feed = feedparser.parse(url)

        # Add the articles from the current feed
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        # Check for a next page or similar link (varies by feed)
        url = None  # Replace this with actual logic to find the next URL if available (e.g., feed.links)

    return articles

# Usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = read_rss_feed(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
