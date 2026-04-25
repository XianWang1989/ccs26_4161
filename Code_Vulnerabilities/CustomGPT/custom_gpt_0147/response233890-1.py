
from random import choice
import tweepy  # Assuming Tweepy is the library you're using for Twitter API

# Your Twitter API setup
tx = tweepy.API(your_auth)  # replace 'your_auth' with your authentication details

# List of search queries with their results
search_queries = [
    ("#hash1", tx.search.tweets(q="#hash1")),
    ("#hash2", tx.search.tweets(q="#hash2")),
    ("#hash3", tx.search.tweets(q="#hash3")),
    ("#hash4", tx.search.tweets(q="#hash4")),
    ("#hash5", tx.search.tweets(q="#hash5")),
    ("#hash6", tx.search.tweets(q="#hash6")),
    ("#hash7", tx.search.tweets(q="#hash7")),
    ("#hash8", tx.search.tweets(q="#hash8")),
    ("#hash9", tx.search.tweets(q="#hash9")),
    ("#hash10", tx.search.tweets(q="#hash10"))
]

# Randomly select one of the search results
selected_query, results = choice(search_queries)

# Print out the query string
print(f'The selected query is: "{selected_query}"')
