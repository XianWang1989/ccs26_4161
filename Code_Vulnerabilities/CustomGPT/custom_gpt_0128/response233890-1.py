
import random

# Simulating the Twitter API search (mock examples)
class MockTwitterAPI:
    def search(self, q):
        return f"Results for {q}"  # Simulating the response

tx = MockTwitterAPI()

# Define searches
searches = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
            "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped objects
wrapped_objects = [(search, tx.search(search)) for search in searches]

# Randomly choose one
selected_search, results = random.choice(wrapped_objects)

# Print the selected query
print(f'Selected query: "{selected_search}"')
print(results)
