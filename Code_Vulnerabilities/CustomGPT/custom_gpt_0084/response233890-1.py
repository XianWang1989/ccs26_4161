
import random

# Sample search objects with their respective queries
search_queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Assuming `tx.search.tweets` returns wrapped search objects
px = [tx.search.tweets(q=query) for query in search_queries]

# Randomly choose one search object
p = random.choice(px)

# Find the index of the chosen search object
index = px.index(p)

# Print the corresponding query
print(f'"{search_queries[index]}"')
