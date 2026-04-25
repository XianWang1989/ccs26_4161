
import feedparser

def fetch_all_articles(feed_url):
    parsed_feed = feedparser.parse(feed_url)

    # Initialize a list to store all articles
    articles = []

    # Loop through entries in the parsed feed
    for entry in parsed_feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}\n")
