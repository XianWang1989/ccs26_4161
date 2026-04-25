
import feedparser

def get_all_articles(feed_url):
    all_articles = []
    feed = feedparser.parse(feed_url)

    # Loop to go through all entries in the feed
    while True:
        # Add the current page entries to the list
        for entry in feed.entries:
            all_articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published
            })

        # Check if there is a next page link in the feed
        if 'next' in feed:
            feed_url = feed['next']  # Update the feed URL for the next page
            feed = feedparser.parse(feed_url)
        else:
            break  # No more pages, exit the loop

    return all_articles

# Example usage:
if __name__ == "__main__":
    rss_feed_url = 'http://example.com/rss'
    articles = get_all_articles(rss_feed_url)
    for article in articles:
        print(f"Title: {article['title']}\nLink: {article['link']}\nPublished: {article['published']}\n")
