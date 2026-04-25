
import random

# Assuming tx.search.tweets is defined elsewhere
class WrappedSearch:
    def __init__(self, query):
        self.query = query
        self.results = tx.search.tweets(q=query)  # Perform the search

# Wrap your queries
search_queries = [
    WrappedSearch("#hash1"),
    WrappedSearch("#hash2"),
    WrappedSearch("#hash3"),
    WrappedSearch("#hash4"),
    WrappedSearch("#hash5"),
    WrappedSearch("#hash6"),
    WrappedSearch("#hash7"),
    WrappedSearch("#hash8"),
    WrappedSearch("#hash9"),
    WrappedSearch("#hash10"),
]

# Randomly choose one wrapped search
chosen_search = random.choice(search_queries)

# Print the query of the chosen search
print(chosen_search.query)
