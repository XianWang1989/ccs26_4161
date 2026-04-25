
import random

# List of queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Function to simulate the search
def search_tweets(q):
    print(f"Searching tweets for: {q}")  # Simulating search
    return q  # Return the query for demonstration

# Create a list of wrapped search objects
wrapped_searches = [search_tweets(q) for q in queries]

# Randomly choose one of the wrapped search results
chosen_query = random.choice(wrapped_searches)

# Print the value of q used for the chosen search
print(f'Selected query: "{chosen_query}"')
