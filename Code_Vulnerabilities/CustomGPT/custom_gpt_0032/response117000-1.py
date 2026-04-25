
import feedparser

def read_rss_feed(feed_url):
    # Parsing the RSS feed
    feed = feedparser.parse(feed_url)

    articles = []

    # Store articles from the current feed
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if 'published' in entry else 'No date available'
        })

    # Check if there's a next page (may vary per feed implementation)
    if hasattr(feed, 'feed') and 'next' in feed.feed:
        next_page_url = feed.feed.next
        articles.extend(read_rss_feed(next_page_url))  # Recursively fetch the next page

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = read_rss_feed(feed_url)

for article in all_articles:
    print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
