
import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)
    articles = feed.entries

    print(f'Title: {feed.feed.title}\n')
    for article in articles:
        print(f'Title: {article.title}')
        print(f'Published: {article.published}')
        print(f'Link: {article.link}\n')

# Example usage
rss_url = 'http://example.com/rss'
read_rss_feed(rss_url)
