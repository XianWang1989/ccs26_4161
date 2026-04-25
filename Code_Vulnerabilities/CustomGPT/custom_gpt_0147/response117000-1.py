
import feedparser

def read_rss_feed(url):
    # Parse the RSS feed
    feed = feedparser.parse(url)
    articles = []

    # Loop through each entry in the feed
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        summary = entry.summary
        articles.append({
            'title': title,
            'link': link,
            'summary': summary
        })

    return articles

def print_articles(articles):
    for idx, article in enumerate(articles):
        print(f"{idx + 1}. {article['title']}")
        print(f"   Link: {article['link']}")
        print(f"   Summary: {article['summary']}\n")

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = read_rss_feed(rss_url)
print_articles(articles)
