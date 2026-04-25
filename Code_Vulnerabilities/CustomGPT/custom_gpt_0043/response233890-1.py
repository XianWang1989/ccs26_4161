
from random import choice

# Assuming 'tx' is your Twitter API object already initialized
search_queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
                  "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list to store the search results, along with their original query
results = []
for query in search_queries:
    result = tx.search.tweets(q=query)
    results.append((query, result))  # Store the query along with the result

# Randomly select one of the results
selected_query, selected_result = choice(results)

# Print the value of the randomly chosen query
print(f'The selected query is: "{selected_query}"')
