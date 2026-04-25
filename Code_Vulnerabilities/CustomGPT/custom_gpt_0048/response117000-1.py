
import feedparser

def fetch_rss_articles(feed_url):
    d = feedparser.parse(feed_url)

    articles = []

    # Add current feed articles
    for entry in d.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })

    # Check if there is a next page link
    while 'next' in d:
        next_url = d.feed.get('next')
        if not next_url:
            break
        d = feedparser.parse(next_url)
        for entry in d.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

    return articles

# Example usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_rss_articles(feed_url)
for article in articles:
    print(f"{article['title']} - {article['link']} - {article['published']}")
