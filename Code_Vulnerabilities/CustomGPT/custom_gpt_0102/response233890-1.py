
import random

# Define the search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Simulate the wrapped objects
def simulated_search_tweets(q):
    return {"query": q}  # Simulating a wrapped object with the query

# Create a list of wrapped objects
search_results = [simulated_search_tweets(q) for q in queries]

# Randomly choose one wrapped object
selected_result = random.choice(search_results)

# Extract and print the query from the selected wrapped object
print(selected_result["query"])
