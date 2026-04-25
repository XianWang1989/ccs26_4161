
from random import choice

# Assuming 'tx' is your Twitter API object

# Create a list of tuples (search_object, query)
px = [
    (tx.search.tweets(q="#hash1"), "#hash1"),
    (tx.search.tweets(q="#hash2"), "#hash2"),
    (tx.search.tweets(q="#hash3"), "#hash3"),
    (tx.search.tweets(q="#hash4"), "#hash4"),
    (tx.search.tweets(q="#hash5"), "#hash5"),
    (tx.search.tweets(q="#hash6"), "#hash6"),
    (tx.search.tweets(q="#hash7"), "#hash7"),
    (tx.search.tweets(q="#hash8"), "#hash8"),
    (tx.search.tweets(q="#hash9"), "#hash9"),
    (tx.search.tweets(q="#hash10"), "#hash10")
]

# Randomly choose an object and its associated query
p, query = choice(px)

# Print the query value
print(query)
