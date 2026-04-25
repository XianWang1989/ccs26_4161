
import random

# Presumably these are your wrapped objects
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Creating a list of tuples (query, tweets)
px = [(q, tx.search.tweets(q=q)) for q in queries]

# Randomly choosing one
p = random.choice(px)

# Printing the associated query (the 'q' value)
print(f'Selected query: "{p[0]}"')
