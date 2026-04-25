
import feedparser
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('rss_articles.db')
c = conn.cursor()

# Create a table for articles
c.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        title TEXT,
        link TEXT,
        description TEXT
    )
''')

# URL of the RSS feed
rss_url = 'https://example.com/rss'  # Replace with your RSS feed URL
feed = feedparser.parse(rss_url)

# Store articles in the database
for entry in feed.entries:
    c.execute('''
        INSERT INTO articles (title, link, description)
        VALUES (?, ?, ?)
    ''', (entry.title, entry.link, entry.description))

# Commit changes and close the connection
conn.commit()
conn.close()
