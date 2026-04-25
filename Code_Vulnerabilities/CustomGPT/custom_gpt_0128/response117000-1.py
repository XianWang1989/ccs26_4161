
import feedparser

def fetch_articles(feed_url):
    articles = []
    page_url = feed_url
    while page_url:
        feed = feedparser.parse(page_url)
        articles.extend(feed.entries)

        # Check if there's a next page link in the feed
        if 'next' in feed:
            page_url = feed['next']
        else:
            page_url = None

    return articles

# Example RSS feed URL
rss_feed_url = 'https://example.com/rss'
articles = fetch_articles(rss_feed_url)

for article in articles:
    print(f'Title: {article.title}')
    print(f'Link: {article.link}')
    print('---')
