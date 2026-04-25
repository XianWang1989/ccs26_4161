
from random import choice

# Your list of search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Your search calls, simulating the results
p = [tx.search.tweets(q=query) for query in queries]

# Randomly select one of the search results
selected_search_result = choice(p)

# Find the index of the selected search result
index = p.index(selected_search_result)

# Print the corresponding query
print(queries[index])
