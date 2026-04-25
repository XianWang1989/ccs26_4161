
def fetch_all_articles(base_url):
    all_articles = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"  # Modify as per your RSS feed pagination
        articles = fetch_rss_feed(url)

        if not articles:
            break  # Stop if no more articles are found

        all_articles.extend(articles)
        page += 1

    return all_articles

# Fetch all articles from paginated RSS feed
all_articles = fetch_all_articles(rss_url)

for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print(f"Summary: {article['summary']}\n")
