
import feedparser
import requests

def fetch_all_articles(feed_url):
    articles = []
    page = feed_url  # Start with the initial feed URL

    while page:
        print(f"Fetching articles from: {page}")
        feed = feedparser.parse(page)
        articles.extend(feed.entries)

        # Check if there's a next page link (this will depend on the feed structure)
        # For example, if the feed has a 'next' link in feed.feed.links
        next_link = None
        for link in feed.feed.links:
            if link.rel == 'next':  # Check for a link with rel='next'
                next_link = link.href
                break

        page = next_link  # Update the page URL for the next iteration

    return articles

# Example usage
if __name__ == "__main__":
    rss_feed_url = "https://example.com/rss"  # Replace with your RSS feed URL
    all_articles = fetch_all_articles(rss_feed_url)

    for article in all_articles:
        print(f"Title: {article.title}")
        print(f"Link: {article.link}")
        print(f"Published: {article.published}\n")
