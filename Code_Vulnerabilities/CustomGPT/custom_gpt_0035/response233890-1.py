
import random

# Define the queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Create a dictionary to associate queries with the tweet calls
searches = {query: tx.search.tweets(q=query) for query in queries}

# Randomly choose a query
chosen_query = random.choice(queries)
p = searches[chosen_query]

# Print the selected query
print(f'Selected query: "{chosen_query}"')
