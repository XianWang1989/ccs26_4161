
import random

# Define queries
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

# Simulate Twitter API calls (replace with actual calls)
results = {query: tx.search.tweets(q=query) for query in queries}

# Randomly choose a query and its result
selected_query = random.choice(queries)
selected_result = results[selected_query]

# Print the selected query
print(selected_query)  # Output will be the chosen query, e.g., "#hash7"
