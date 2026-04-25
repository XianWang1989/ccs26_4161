
import random

# Define your search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Simulate the wrapped objects with their respective queries
px = [(query, tx.search.tweets(q=query)) for query in queries]

# Randomly select one of the wrapped objects
selected = random.choice(px)

# Print the query associated with the selected object
query_value, result = selected
print(f'Selected query: "{query_value}"')
