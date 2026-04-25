
import feedparser
import requests

def fetch_all_articles(rss_url):
    articles = []
    page = 1  # Initialize page number, if pagination is supported

    while True:
        # Modify the URL for pagination if needed
        url = f"{rss_url}?page={page}"  # Adjust this for the specific RSS feed structure
        print(f"Fetching: {url}")

        response = requests.get(url)
        feed = feedparser.parse(response.content)

        # If there are no entries, break the loop
        if not feed.entries:
            break

        # Collect articles
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if 'published' in entry else 'No date provided'
            })

        page += 1  # Move to the next page

    return articles

# Example usage
rss_url = "https://example.com/rss"  # Replace with the actual RSS feed URL
all_articles = fetch_all_articles(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}, Link: {article['link']}, Published: {article['published']}")
