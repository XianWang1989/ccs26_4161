
import feedparser

def fetch_all_articles(feed_url):
    all_entries = []
    feed = feedparser.parse(feed_url)

    # Add initial entries
    all_entries.extend(feed.entries)

    # Check for next page (this depends on how the feed is structured)
    while hasattr(feed, 'next_page') and feed.next_page:
        feed = feedparser.parse(feed.next_page)
        all_entries.extend(feed.entries)

    return all_entries

# Usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_all_articles(feed_url)

# Print titles of all articles
for article in articles:
    print(article.title)
