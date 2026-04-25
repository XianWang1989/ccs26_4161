
from random import choice

# Define your queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Simulate the Twitter API calls (replace these with actual API calls)
px = [tx.search.tweets(q=query) for query in queries]

# Randomly select one of the search results
p = choice(px)

# Find the index of the selected search result in the list
index = px.index(p)

# Print the corresponding query
print(queries[index])
