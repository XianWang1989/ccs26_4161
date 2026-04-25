
import random

# Mocking the search class to simulate behavior
class MockTwitterAPI:
    def search(self, q):
        return f"Results for {q}"

# Your Twitter API instance
tx = MockTwitterAPI()

# Define the search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Using a list comprehension to create search objects with queries
search_results = [tx.search(q) for q in queries]

# Randomly choose one search result
chosen_result = random.choice(search_results)

# Find the corresponding query for the chosen result
chosen_query = queries[search_results.index(chosen_result)]

# Print the chosen query
print(chosen_query)
