
from random import choice

# Define your searches
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
search_objects = [tx.search.tweets(q=q) for q in queries]

# Randomly choose one
selected_object = choice(search_objects)

# Print the query (brute-force method)
query_value = queries[search_objects.index(selected_object)]
print(query_value)
