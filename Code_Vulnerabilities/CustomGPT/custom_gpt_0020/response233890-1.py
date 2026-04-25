
import random

# Simulating the tx object and the search.tweets method for demonstration.
class MockTwitterAPI:
    def search(self, query):
        # Simulate some search results
        return {"query": query, "results": [f"Result {i} for {query}" for i in range(3)]}

tx = MockTwitterAPI()

# Create wrapped objects that hold both the query and results
class WrappedSearch:
    def __init__(self, query):
        self.query = query
        self.results = tx.search(query)

# List of search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Create wrapped objects and store them in a list
wrapped_objects = [WrappedSearch(query) for query in queries]

# Randomly choose one wrapped search
chosen_search = random.choice(wrapped_objects)

# Print the query of the chosen search
print(f'The chosen query is: "{chosen_search.query}"')
