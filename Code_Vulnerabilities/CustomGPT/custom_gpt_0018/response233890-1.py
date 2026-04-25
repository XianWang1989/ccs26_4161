
from random import choice

# Create a list of tuples where each tuple contains the query and the search result
px = [
    ("#hash1", tx.search.tweets(q="#hash1")),
    ("#hash2", tx.search.tweets(q="#hash2")),
    ("#hash3", tx.search.tweets(q="#hash3")),
    ("#hash4", tx.search.tweets(q="#hash4")),
    ("#hash5", tx.search.tweets(q="#hash5")),
    ("#hash6", tx.search.tweets(q="#hash6")),
    ("#hash7", tx.search.tweets(q="#hash7")),
    ("#hash8", tx.search.tweets(q="#hash8")),
    ("#hash9", tx.search.tweets(q="#hash9")),
    ("#hash10", tx.search.tweets(q="#hash10")),
]

# Randomly select one of the (query, result) tuples
selected_query, p = choice(px)

# Print the selected query
print(f"The selected query is: '{selected_query}'")
