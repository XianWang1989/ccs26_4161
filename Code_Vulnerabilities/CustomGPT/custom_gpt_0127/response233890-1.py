
import random

# List of hashtags for searches
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list to hold the wrapped objects
px = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly choose one of the search results
p = random.choice(px)

# Find the corresponding hashtag
index = px.index(p)  # Get the index of the chosen object
chosen_hashtag = hashtags[index]  # Retrieve the corresponding hashtag

# Print the chosen hashtag
print(chosen_hashtag)
