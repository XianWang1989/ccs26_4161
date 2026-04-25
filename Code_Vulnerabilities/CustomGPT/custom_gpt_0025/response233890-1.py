
import random

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulating the search function returning wrapped objects
class TwitterAPI:
    def search(self, q):
        # Simulate the search result as an object with a property for the query
        return {'query': q}

# Initialize Twitter API
tx = TwitterAPI()

# Wrap searches in objects
wrapped_searches = [tx.search(q) for q in queries]

# Randomly choose one wrapped object
chosen_search = random.choice(wrapped_searches)

# Print the query of the chosen search
print(chosen_search['query'])
