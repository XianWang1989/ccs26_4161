
from random import choice

# Define your search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Perform the searches and store them in a list
px = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one of the searches
p = choice(px)

# Get the index of the chosen search
index = px.index(p)

# Print the corresponding query
print(f'Selected query: "{queries[index]}"')
