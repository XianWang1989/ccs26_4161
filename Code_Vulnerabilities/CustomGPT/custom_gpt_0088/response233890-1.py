
from random import choice

# Assuming tx is your Twitter API object
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of tuples (query, search result)
px = [(query, tx.search.tweets(q=query)) for query in queries]

# Randomly choose one of the tuples
p = choice(px)

# Print the query from the selected tuple
print(f'"{p[0]}"')
