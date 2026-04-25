
import random

# Example wrapped objects with associated queries
search_objects = [
    {"query": "#hash1", "result": tx.search.tweets(q="#hash1")},
    {"query": "#hash2", "result": tx.search.tweets(q="#hash2")},
    {"query": "#hash3", "result": tx.search.tweets(q="#hash3")},
    {"query": "#hash4", "result": tx.search.tweets(q="#hash4")},
    {"query": "#hash5", "result": tx.search.tweets(q="#hash5")},
    {"query": "#hash6", "result": tx.search.tweets(q="#hash6")},
    {"query": "#hash7", "result": tx.search.tweets(q="#hash7")},
    {"query": "#hash8", "result": tx.search.tweets(q="#hash8")},
    {"query": "#hash9", "result": tx.search.tweets(q="#hash9")},
    {"query": "#hash10", "result": tx.search.tweets(q="#hash10")},
]

# Randomly choose a search object
chosen = random.choice(search_objects)

# Print the query value
print(chosen["query"])
