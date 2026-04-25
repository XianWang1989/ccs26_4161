
import random

# Assuming tx is your Twitter API object
search_queries = [
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

# Create a list of tuples containing (query, search object)
px = [(query, tx.search.tweets(q=query)) for query in search_queries]

# Randomly choose one search object
selected_query, selected_search = random.choice(px)

# Print the selected query
print(selected_query)
