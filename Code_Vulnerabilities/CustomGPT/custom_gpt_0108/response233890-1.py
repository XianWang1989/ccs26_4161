
from random import choice

# Example queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Simulating the search using a dictionary to map queries to results
search_results = {query: tx.search.tweets(q=query) for query in queries}

# Randomly choosing one query's result
chosen_query = choice(queries)
chosen_result = search_results[chosen_query]

# Print the chosen query
print(f'"{chosen_query}"')
