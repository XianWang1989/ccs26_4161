
import random

# Simulating the search objects with a dictionary that includes the query
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

# Randomly choose one search object
selected_search = random.choice(search_objects)

# Print the query used for the selected search object
print(selected_search["query"])
