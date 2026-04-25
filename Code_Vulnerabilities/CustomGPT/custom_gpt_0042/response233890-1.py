
import random

# Simulate the search objects with their queries
search_queries = [
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

# Simulating the search function returns
def mock_search(tweets):
    return {"query": tweets}  # Simulated response

# Create the list of search objects
px = [mock_search(q) for q in search_queries]

# Randomly choose one search object
p = random.choice(px)

# Print the corresponding query
print(f'Chosen query: "{p["query"]}"')
