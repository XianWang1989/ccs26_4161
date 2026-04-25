
import feedparser
import sqlite3

# Set up SQLite database
conn = sqlite3.connect('rss_feed.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS articles (title TEXT, link TEXT, published TEXT)')

def read_and_store_rss_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published

        # Insert into the database
        c.execute('INSERT INTO articles (title, link, published) VALUES (?, ?, ?)', (title, link, published))
        conn.commit()

# Example usage
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
read_and_store_rss_feed(rss_url)

# To display stored articles later
def display_stored_articles():
    c.execute('SELECT * FROM articles')
    for row in c.fetchall():
        print(row)

# Uncomment to see stored articles
# display_stored_articles()

conn.close()
