
import random

# Define the hashtags and their corresponding wrapped objects
hashtags = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Simulate wrapped objects for each hashtag
px = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly choose one
p = random.choice(px)

# Find the query associated with the chosen object
chosen_index = px.index(p)
chosen_query = hashtags[chosen_index]

# Print the chosen query
print(chosen_query)
