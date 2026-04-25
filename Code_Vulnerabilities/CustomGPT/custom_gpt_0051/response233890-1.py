
import random

# List of hashtags.
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped objects.
px = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Choose a random search object.
p = random.choice(px)

# Find the index of the chosen object to get the corresponding hashtag.
index = px.index(p)

# Print the selected query.
print(hashtags[index])
