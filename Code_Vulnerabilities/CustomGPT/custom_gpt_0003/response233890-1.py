
import random

# Assuming tx is your Twitter API instance
search_queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
search_results = {}

# Create a dictionary where the keys are queries and the values are the search results
for query in search_queries:
    search_results[query] = tx.search.tweets(q=query)

# Randomly choose a query and its corresponding search result
chosen_query = random.choice(search_queries)
chosen_result = search_results[chosen_query]

# Print the chosen query
print(f"The selected query is: {chosen_query}")
