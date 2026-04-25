
from random import choice

# Assume tx is your Twitter API connection object
queries = {
    "hash1": "#hash1",
    "hash2": "#hash2",
    "hash3": "#hash3",
    "hash4": "#hash4",
    "hash5": "#hash5",
    "hash6": "#hash6",
    "hash7": "#hash7",
    "hash8": "#hash8",
    "hash9": "#hash9",
    "hash10": "#hash10"
}

# Generate wrapped objects with queries
p_objects = [tx.search.tweets(q=hashtag) for hashtag in queries.values()]

# Randomly select one of the wrapped objects
p = choice(p_objects)

# To find the corresponding query of the chosen wrapped object
chosen_query = [query for query, obj in zip(queries.values(), p_objects) if obj == p]

# Print the selected query if found
if chosen_query:
    print(chosen_query[0])  # This will print the corresponding q value
