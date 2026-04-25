
from random import choice

# List of hashtags
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of search objects
px = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly select a search object
selected_search = choice(px)

# Find the index of the selected object
index = px.index(selected_search)

# Print the corresponding query
print(hashtags[index])
