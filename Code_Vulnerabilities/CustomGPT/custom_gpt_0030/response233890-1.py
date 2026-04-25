
import random

# Define the queries
queries = [
    "#hash1", "#hash2", "#hash3",
    "#hash4", "#hash5", "#hash6",
    "#hash7", "#hash8", "#hash9",
    "#hash10"
]

# Simulate the search tweets wrapped objects (replace with actual calls)
px = [tx.search.tweets(q=query) for query in queries]

# Randomly select one
p = random.choice(px)

# Get the index of the selected object to fetch the query
selected_index = px.index(p)  # Get the index of the randomly chosen search result

# Print the corresponding query
print(f'"{queries[selected_index]}"')
