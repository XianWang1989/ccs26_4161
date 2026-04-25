
import feedparser
import requests

def fetch_all_articles(feed_url):
    all_articles = []
    page = 1

    while True:
        # Append page number to the feed URL if necessary (modify based on feed structure)
        response = requests.get(f"{feed_url}?page={page}")

        if response.status_code != 200:
            break  # Exit loop if no more pages

        feed = feedparser.parse(response.content)

        if not feed.entries:
            break  # Exit if there are no more entries

        for entry in feed.entries:
            all_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        page += 1  # Move to the next page

    return all_articles

# Usage
feed_url = 'https://example.com/rss'  # Replace with your RSS feed URL
articles = fetch_all_articles(feed_url)

for article in articles:
    print(f"{article['published']}: {article['title']} ({article['link']})")
