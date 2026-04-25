
from random import choice

# Initialize query list
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulated tweet search function (mocking the Twitter API call)
def tweet_search(query):
    # Assume some wrapper object is created here
    return {"query": query, "results": f"Results for {query}"}

# Create list of wrapped objects
px = [tweet_search(q) for q in queries]

# Randomly choose one of the wrapped objects
p = choice(px)

# Print the query from the chosen wrapped object
print(p['query'])
