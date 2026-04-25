
import feedparser
import requests

def fetch_all_articles(rss_url):
    articles = []
    feed = feedparser.parse(rss_url)

    # Loop through the feed entries
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary
        })

    # Check if there's a next page and fetch more
    next_page = getattr(feed, 'next_page', None)
    while next_page:
        response = requests.get(next_page)
        feed = feedparser.parse(response.content)

        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary
            })

        next_page = getattr(feed, 'next_page', None)

    return articles

# Example Usage
rss_url = 'http://example.com/rss'
all_articles = fetch_all_articles(rss_url)
for article in all_articles:
    print(article['title'], article['link'])
