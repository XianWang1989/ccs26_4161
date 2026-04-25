
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []

    # Loop through feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Optionally handle pagination or further entries if applicable
    # This depends on the specific RSS feed structure

    return articles

# Example usage
rss_url = 'https://rss.yourfeedurl.com'
articles = read_rss_feed(rss_url)

for article in articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
