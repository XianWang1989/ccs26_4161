
import random

# Simulate the search API wrapper
class TwitterAPI:
    def search_tweets(self, q):
        # This would normally call the Twitter API
        return {"query": q, "results": []}  # Simulated response

# Initialize Twitter API instance
tx = TwitterAPI()

# List of queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped tweet objects
px = [tx.search_tweets(q) for q in queries]

# Randomly select one of the tweet objects
p = random.choice(px)

# Print the query from the selected object
print(p["query"])
