
import feedparser
import requests

def get_all_articles(feed_url):
    articles = []
    while feed_url:
        feed = feedparser.parse(feed_url)
        articles.extend(feed.entries)
        # Find the next page (if applicable, this depends on the feed structure)
        feed_url = get_next_page(feed)

    return articles

def get_next_page(feed):
    # Check if there's a 'next' link in the feed (this is feed-specific)
    for link in feed.links:
        if link.rel == 'next':
            return link.href
    return None

# Example usage
rss_url = 'http://example.com/rss'  # Replace with the actual RSS feed URL
all_articles = get_all_articles(rss_url)

for article in all_articles:
    print(f'Title: {article.title}')
    print(f'Published: {article.published}')
    print(f'Link: {article.link}')
    print('---')
