
import feedparser
import requests

def fetch_all_articles(feed_url):
    all_articles = []
    next_page_url = feed_url

    while next_page_url:
        response = requests.get(next_page_url)
        if response.status_code != 200:
            print(f"Failed to fetch feed: {response.status_code}")
            break

        feed = feedparser.parse(response.content)
        all_articles.extend(feed.entries)

        if 'next' in feed:
            next_page_url = feed.feed.next  # Modify this based on feed specifications
        else:
            next_page_url = None

    return all_articles

def main():
    feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
    articles = fetch_all_articles(feed_url)

    for article in articles:
        print(f"Title: {article.title}")
        print(f"Link: {article.link}")
        print(f"Published: {article.published}")
        print("------")

if __name__ == "__main__":
    main()
