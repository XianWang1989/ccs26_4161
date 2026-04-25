
import random

# Assuming tx is your Twitter API instance

# Define search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Wrap the search calls in a list of tuples (query, results)
px = [(q, tx.search.tweets(q=q)) for q in queries]

# Choose a random search
selected_query, p = random.choice(px)

# Print the query
print(selected_query)
