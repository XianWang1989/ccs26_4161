
from random import choice

# Store queries and associated objects together
query_object_map = {
    "#hash1": tx.search.tweets(q="#hash1"),
    "#hash2": tx.search.tweets(q="#hash2"),
    "#hash3": tx.search.tweets(q="#hash3"),
    "#hash4": tx.search.tweets(q="#hash4"),
    "#hash5": tx.search.tweets(q="#hash5"),
    "#hash6": tx.search.tweets(q="#hash6"),
    "#hash7": tx.search.tweets(q="#hash7"),
    "#hash8": tx.search.tweets(q="#hash8"),
    "#hash9": tx.search.tweets(q="#hash9"),
    "#hash10": tx.search.tweets(q="#hash10"),
}

# Randomly select a query
selected_query = choice(list(query_object_map.keys()))
selected_object = query_object_map[selected_query]

# Print the selected query
print(selected_query)
