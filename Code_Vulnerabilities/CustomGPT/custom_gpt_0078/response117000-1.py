
import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print(f'Title: {entry.title}')
        print(f'Link: {entry.link}')
        print(f'Published: {entry.published}')
        print('---')

    return feed

def fetch_all_articles(url):
    all_articles = []
    next_page_url = url  # Start with the initial URL

    while next_page_url:
        feed = fetch_rss_feed(next_page_url)
        all_articles.extend(feed.entries)

        # Check for a link to the next page
        next_page_url = None
        if 'next' in feed:
            next_page_url = feed['next']  # Modify according to the feed's pagination format
        else:
            break

    return all_articles

if __name__ == "__main__":
    RSS_URL = 'https://example.com/rss'  # Replace with your RSS feed URL
    all_articles = fetch_all_articles(RSS_URL)

    for article in all_articles:
        print(f'Title: {article.title}, Link: {article.link}')
