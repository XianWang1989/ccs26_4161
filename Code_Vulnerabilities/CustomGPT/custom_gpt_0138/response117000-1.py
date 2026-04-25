
import feedparser

def fetch_articles(url):
    feed = feedparser.parse(url)
    articles = []

    # Loop through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        })

    return articles

# Example usage
rss_url = 'http://example.com/rss'  # Replace with the actual RSS feed URL
all_articles = fetch_articles(rss_url)

# Print all articles
for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
