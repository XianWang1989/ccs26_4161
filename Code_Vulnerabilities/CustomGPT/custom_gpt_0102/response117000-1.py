
import feedparser

def fetch_all_articles(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Collect articles from the first page
    articles.extend(feed.entries)

    # If the feed supports pagination, you can get the next page's URL
    while 'next' in feed:
        feed = feedparser.parse(feed.feed.links[0].href)  # Adjust to find the pagination link
        articles.extend(feed.entries)

    return articles

# Example usage
rss_feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
all_articles = fetch_all_articles(rss_feed_url)

for article in all_articles:
    print(f'Title: {article.title}, Link: {article.link}')
