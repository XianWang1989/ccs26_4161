
import random

# Define the query list
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Simulating the Twitter API calls (wrapped objects)
def simulate_tweet_search(query):
    return f"Results for {query}"

# Create the wrapped objects
px = [simulate_tweet_search(query) for query in queries]

# Randomly choose one wrapped object
p = random.choice(px)

# Find the corresponding query
selected_query = queries[px.index(p)]

# Print the selected query
print(selected_query)
