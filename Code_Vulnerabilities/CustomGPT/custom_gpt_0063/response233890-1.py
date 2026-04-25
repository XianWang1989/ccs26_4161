
import random

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Perform searches and store results
results = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one result
p = random.choice(results)

# Get the index of the selected result
index = results.index(p)

# Print the corresponding query
print(queries[index])
