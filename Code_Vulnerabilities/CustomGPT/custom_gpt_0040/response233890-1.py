
import random

# Assuming tx is your Twitter API client instance
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

# Create a list of the search results
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly select one search result
p = random.choice(px)

# Extracting the query value
query_value = p.args[0]  # Access the first argument of the search call

# Print the query value
print(query_value)
