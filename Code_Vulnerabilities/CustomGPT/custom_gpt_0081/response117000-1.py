
import feedparser
import requests

rss_url = 'http://example.com/rss'  # Replace with your RSS feed URL

def fetch_all_articles(rss_url):
    articles = []
    while rss_url:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary
            })

        # Assuming the feed provides a 'next' link for pagination
        rss_url = next((link.href for link in feed.links if link.rel == 'next'), None)

    return articles

all_articles = fetch_all_articles(rss_url)
for article in all_articles:
    print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\nSummary: {article['summary']}\n")
