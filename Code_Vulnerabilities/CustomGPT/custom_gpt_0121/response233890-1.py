
from random import choice

# Define a list of hashtags
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list to store search results along with their queries
px = []

# Simulate the search object creation
for tag in hashtags:
    search_result = tx.search.tweets(q=tag)  # This represents your wrapped object
    px.append((search_result, tag))  # Store the result and its query

# Randomly choose one search result
p = choice(px)

# Print the query
print(f'Chosen query: "{p[1]}"')  # p[1] contains the query (hashtag)
