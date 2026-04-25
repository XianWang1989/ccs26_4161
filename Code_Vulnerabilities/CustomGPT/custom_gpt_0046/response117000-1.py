
import feedparser
import requests

def fetch_articles(feed_url):
    all_articles = []
    page = 1

    while True:
        # Construct the URL (modify according to the feed's pagination structure)
        current_url = f"{feed_url}?page={page}"
        response = requests.get(current_url)

        if response.status_code != 200:
            break  # Exit the loop if there's an issue with the request

        feed = feedparser.parse(response.content)

        if not feed.entries:
            break  # No more entries, exit the loop

        for entry in feed.entries:
            all_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
            })

        page += 1  # Move to the next page

    return all_articles

# Example usage
rss_feed_url = "http://example.com/rss"  # Replace with your RSS feed URL
articles = fetch_articles(rss_feed_url)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print('-' * 40)
