
import random

# Simulating the search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Assuming 'tx.search.tweets' returns objects that we can access
class MockSearch:
    def __init__(self, query):
        self.query = query

    def tweets(self):
        return self  # Simulating the return of a 'wrapped object'

# Create a list of 'wrapped objects'
px = [MockSearch(q).tweets() for q in queries]

# Randomly select one
p = random.choice(px)

# Find the index of the selected object to print the corresponding query
selected_query = queries[px.index(p)]
print(selected_query)
