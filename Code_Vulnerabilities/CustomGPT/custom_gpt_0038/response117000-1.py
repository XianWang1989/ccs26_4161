
import feedparser
import requests

def get_all_articles(feed_url):
    all_articles = []
    response = requests.get(feed_url)

    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        all_articles.extend(feed.entries)

        # Check for pagination (optional logic based on feed structure)
        # Example placeholder: check a link for the next page/entries
        next_page = feed.get('links', [{}])[0].get('href', None)

        while next_page:
            response = requests.get(next_page)
            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                all_articles.extend(feed.entries)
                next_page = feed.get('links', [{}])[0].get('href', None)
            else:
                break
    else:
        print(f"Failed to fetch the feed: {response.status_code}")

    return all_articles

# Example usage
rss_feed_url = "http://example.com/rss"  # Replace with your RSS feed URL
articles = get_all_articles(rss_feed_url)

for article in articles:
    print(f"Title: {article.title}, Link: {article.link}")
