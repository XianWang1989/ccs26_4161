
import random

# Define a wrapper for the search that stores the query
class WrappedSearch:
    def __init__(self, query):
        self.query = query
        self.results = tx.search.tweets(q=query)  # Assuming tx.search.tweets returns the results

# Create wrapped search instances
p1 = WrappedSearch("#hash1")
p2 = WrappedSearch("#hash2")
p3 = WrappedSearch("#hash3")
p4 = WrappedSearch("#hash4")
p5 = WrappedSearch("#hash5")
p6 = WrappedSearch("#hash6")
p7 = WrappedSearch("#hash7")
p8 = WrappedSearch("#hash8")
p9 = WrappedSearch("#hash9")
p10 = WrappedSearch("#hash10")

# List of wrapped searches
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
chosen_search = random.choice(px)

# Print the query of the chosen search
print(f'The selected query: "{chosen_search.query}"')
