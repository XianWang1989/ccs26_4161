
import random

# List of queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulate the search queries using the Twitter API (tx)
results = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one of the results
chosen_result = random.choice(results)

# Find the index of the chosen result
index = results.index(chosen_result)

# Print the corresponding query
print(f"The chosen query is: '{queries[index]}'")
