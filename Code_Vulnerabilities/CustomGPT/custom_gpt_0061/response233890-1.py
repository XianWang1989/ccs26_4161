
import random

# Example tweet search objects (replace with actual Twitter API calls)
p1 = tx.search.tweets(q="#hash1")
p2 = tx.search.tweets(q="#hash2")
p3 = tx.search.tweets(q="#hash3")
p4 = tx.search.tweets(q="#hash4")
p5 = tx.search.tweets(q="#hash5")
p6 = tx.search.tweets(q="#hash6")
p7 = tx.search.tweets(q="#hash7")
p8 = tx.search.tweets(q="#hash8")
p9 = tx.search.tweets(q="#hash9")
p10 = tx.search.tweets(q="#hash10")

# List of wrapped objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one of the wrapped objects
p = random.choice(px)

# Accessing the query used for the chosen object
query = p['search_metadata']['query']  # or however your object lets you access the query

print(f'The chosen query is: "{query}"')
