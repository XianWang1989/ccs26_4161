
from random import choice

# Define your search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Perform searches
p_list = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one search result
p = choice(p_list)

# Find the index of the chosen search result
index = p_list.index(p)

# Print the corresponding query
print(queries[index])
