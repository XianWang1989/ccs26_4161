
import random

# Your list of search objects
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

# List of queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Combine searches and queries
px = list(zip([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10], queries))

# Choose a random search object and its corresponding query
p, query = random.choice(px)

# Print the query
print(query)  # This will print the chosen query, e.g., "#hash7"
