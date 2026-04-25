
from random import choice

# Define your queries
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

# Create a list of wrapped objects with the associated query
search_results = [tx.search.tweets(q=query) for query in queries]

# Randomly select one of the search results
selected_result = choice(search_results)

# Find the index of the selected result
index = search_results.index(selected_result)

# Print the corresponding query
print(queries[index])  # This will print the chosen query like "#hash7"
