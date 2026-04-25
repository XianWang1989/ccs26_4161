
from random import choice

# Simulated search function (replace with actual Twitter API calls)
def search_tweets(q):
    return {"query": q}  # Simulates a wrapped object containing the query

# List of searches
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
search_objects = [search_tweets(q) for q in queries]

# Randomly choose one search object
p = choice(search_objects)

# Print the query
print(p["query"])
