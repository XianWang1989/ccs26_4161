from random import choice

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Pair each query with its result
results = [(q, tx.search.tweets(q=q)) for q in queries]

# Choose one at random
selected_query, selected_result = choice(results)

# Print the query
print(selected_query)
