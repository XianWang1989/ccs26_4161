
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    parsed_feed = feedparser.parse(feed_url)

    # Add the initial entries
    articles.extend(parsed_feed.entries)

    # Check for pagination, if provided by the feed
    while hasattr(parsed_feed, 'feed') and 'next' in parsed_feed.feed:
        next_url = parsed_feed.feed.next
        response = requests.get(next_url)
        if response.status_code == 200:
            parsed_feed = feedparser.parse(next_url)
            articles.extend(parsed_feed.entries)
        else:
            break  # No more pages or a problem occurred

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(feed_url)

for article in all_articles:
    print(f'Title: {article.title}, Link: {article.link}')
