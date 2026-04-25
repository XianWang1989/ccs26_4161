
import random

# Assume tx is your Twitter API object
# Create a list of search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Create a list of tweet search results
search_results = [tx.search.tweets(q=query) for query in queries]

# Randomly select one search result
selected_result_index = random.choice(range(len(search_results)))
selected_result = search_results[selected_result_index]

# Print the corresponding query
print(queries[selected_result_index])
