
from random import choice
import tweepy  # Assuming this is the library you're using for the Twitter API

# Example setup (make sure to authenticate with your credentials)
# tx = tweepy.API(auth)

queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Create a list of tuples containing the search result and its query
px = [(tx.search.tweets(q=query), query) for query in queries]

# Randomly choose one of the tuples
p, selected_query = choice(px)

# Print the selected query
print(f'"{selected_query}"')
