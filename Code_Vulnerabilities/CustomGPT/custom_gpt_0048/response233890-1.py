
import random

# Define the list of hashtags
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of search objects
px = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly choose one
p = random.choice(px)

# Find the index of the chosen search object
index = px.index(p)

# Print the corresponding hashtag
print(hashtags[index])
