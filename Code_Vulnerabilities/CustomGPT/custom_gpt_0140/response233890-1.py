
import random

# Define your searches
queries = [
    "#hash1",
    "#hash2",
    "#hash3",
    "#hash4",
    "#hash5",
    "#hash6",
    "#hash7",
    "#hash8",
    "#hash9",
    "#hash10"
]

# Perform searches
search_results = [tx.search.tweets(q=query) for query in queries]

# Choose a random search result
selected_index = random.randint(0, len(search_results) - 1)
selected_search = search_results[selected_index]
selected_query = queries[selected_index]

# Print the chosen query
print(selected_query)
