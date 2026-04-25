
from random import choice

# Sample Twitter API response wrapper
class TwitterSearch:
    def __init__(self, query):
        self.query = query
        self.results = tx.search.tweets(q=query)  # Assume this fetches the tweets based on the query

    def get_query(self):
        return self.query

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped objects
px = [TwitterSearch(query) for query in queries]

# Randomly choose one
p = choice(px)

# Print the query used for the chosen wrapped object
print(p.get_query())
