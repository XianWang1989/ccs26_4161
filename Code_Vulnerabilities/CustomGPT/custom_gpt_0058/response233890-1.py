
from random import choice

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulating the API calls with wrapped objects (just for example)
# Replace this with actual calls to your Twitter API
search_results = [tx.search.tweets(q=query) for query in queries]

# Choose a random search result
chosen_search = choice(search_results)
chosen_index = search_results.index(chosen_search)

# Print the query that corresponds to the chosen search result
chosen_query = queries[chosen_index]
print(chosen_query)
