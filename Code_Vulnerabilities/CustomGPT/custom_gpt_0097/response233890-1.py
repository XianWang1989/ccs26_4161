
from random import choice

# Define a function to create a wrapped object with the query
def wrap_query(query):
    return {'query': query}  # This simulates a wrapped object

# Create the search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
px = [wrap_query(q) for q in queries]  # List of wrapped objects

# Choose a random query
p = choice(px)

# Print the query
print(p['query'])
