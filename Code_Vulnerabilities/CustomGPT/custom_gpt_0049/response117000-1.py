
import feedparser

def fetch_all_articles(feed_url):
    parsed_feed = feedparser.parse(feed_url)
    articles = []

    # Loop through all entries in the RSS feed
    for entry in parsed_feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check for pagination or older articles
    # This part depends on the specific RSS feed structure.
    # Example: If the feed supports pagination, you would fetch other pages.

    return articles

# Example usage
feed_url = 'https://example.com/rss_feed_url'
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
