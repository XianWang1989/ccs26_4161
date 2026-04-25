
import random

# Define the search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Create wrapped objects
px = [tx.search.tweets(q=query) for query in queries]

# Randomly select one wrapped object
p = random.choice(px)

# Print the corresponding query
selected_query = queries[px.index(p)]
print(selected_query)
