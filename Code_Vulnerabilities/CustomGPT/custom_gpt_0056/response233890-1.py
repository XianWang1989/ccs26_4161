
import random

# Simulating the search object creation with a function
class TwitterAPI:
    def search(self, q):
        # Simulated response of a search query
        return {"query": q, "results": []}

# Instantiate the API
tx = TwitterAPI()

# Define the search terms
search_terms = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Create wrapped search objects
wrapped_searches = [tx.search(q=term) for term in search_terms]

# Randomly choose one
chosen_search = random.choice(wrapped_searches)

# Print the query parameter
print(chosen_search['query'])
