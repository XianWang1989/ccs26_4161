
import random

# Simulating the search function
class TwitterAPI:
    def search(self, q):
        return {"query": q, "results": []}  # Mocked response

# Create an instance of the Twitter API
tx = TwitterAPI()

# List of hashtag searches
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped search objects
px = [tx.search(q=hashtag) for hashtag in hashtags]

# Randomly choose one search object
p = random.choice(px)

# Print the query value
print(p['query'])
