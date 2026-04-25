
import random

# Define your queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Simulate the wrapped objects (replace with actual Twitter API calls)
search_results = {q: tx.search.tweets(q=q) for q in queries}

# Randomly choose a hash and get its corresponding result
chosen_query = random.choice(queries)
p = search_results[chosen_query]

# Print the chosen query
print(f"Selected query: '{chosen_query}'")
