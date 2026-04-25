
import random

# Define the queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Perform searches
search_results = {query: tx.search.tweets(q=query) for query in queries}

# Randomly choose a search result
selected_query = random.choice(queries)
result = search_results[selected_query]

# Print the selected query
print(f'Selected query: "{selected_query}"')
