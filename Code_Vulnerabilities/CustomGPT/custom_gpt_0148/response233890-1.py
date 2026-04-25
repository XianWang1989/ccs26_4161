
from random import choice

# Mock search function to simulate Twitter API behavior
class MockTwitterAPI:
    def search_tweets(self, q):
        return f"Results for {q}"

# Instantiate the mock API
tx = MockTwitterAPI()

# List of queries and associated search results
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Create wrapped search objects
px = [tx.search_tweets(q) for q in queries]

# Randomly choose one search result
p = choice(px)

# Find the query associated with the chosen result
chosen_query = queries[px.index(p)]

# Print the chosen query
print(chosen_query)
