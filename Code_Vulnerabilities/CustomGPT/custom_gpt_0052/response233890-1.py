
import random

# Sample searches
search_queries = {
    "hash1": "#hash1",
    "hash2": "#hash2",
    "hash3": "#hash3",
    "hash4": "#hash4",
    "hash5": "#hash5",
    "hash6": "#hash6",
    "hash7": "#hash7",
    "hash8": "#hash8",
    "hash9": "#hash9",
    "hash10": "#hash10",
}

# Assuming 'tx' is already defined and authenticated
search_objects = {
    "hash1": tx.search.tweets(q=search_queries["hash1"]),
    "hash2": tx.search.tweets(q=search_queries["hash2"]),
    "hash3": tx.search.tweets(q=search_queries["hash3"]),
    "hash4": tx.search.tweets(q=search_queries["hash4"]),
    "hash5": tx.search.tweets(q=search_queries["hash5"]),
    "hash6": tx.search.tweets(q=search_queries["hash6"]),
    "hash7": tx.search.tweets(q=search_queries["hash7"]),
    "hash8": tx.search.tweets(q=search_queries["hash8"]),
    "hash9": tx.search.tweets(q=search_queries["hash9"]),
    "hash10": tx.search.tweets(q=search_queries["hash10"]),
}

# Randomly choose a search
chosen_key = random.choice(list(search_objects.keys()))
chosen_object = search_objects[chosen_key]

# Print the corresponding search query
print(f'Retrieved query: "{search_queries[chosen_key]}"')

# Proceed with using chosen_object as needed
