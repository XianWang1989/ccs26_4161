
import feedparser

def fetch_articles(feed_url):
    # Parse the RSS feed
    parsed_feed = feedparser.parse(feed_url)
    articles = []

    # Loop through the entries in the feed
    for entry in parsed_feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check for pagination (this logic may vary based on specific feeds)
    if 'next' in parsed_feed:
        next_url = parsed_feed.next.href  # Adjust as needed based on your feed
        articles += fetch_articles(next_url)  # Recursive call to fetch next page

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_articles(feed_url)

# Print out the articles
for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
