
import random

# Example search queries
queries = [
    "#hash1",
    "#hash2",
    "#hash3",
    "#hash4",
    "#hash5",
    "#hash6",
    "#hash7",
    "#hash8",
    "#hash9",
    "#hash10"
]

# Simulating Twitter API search calls (replace with actual calls in practice)
p_results = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one search result
p = random.choice(p_results)

# Find the index of the chosen result to retrieve the corresponding query
index = p_results.index(p)
selected_query = queries[index]

# Print the chosen query
print(selected_query)
