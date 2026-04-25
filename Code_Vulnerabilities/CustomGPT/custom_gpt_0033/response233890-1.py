
import random

# Assuming tx is your Twitter API instance and a `search` method
# Create a list of searches
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

# List of search results
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Choose one randomly
p = random.choice(px)

# Print the query used for the chosen search
# This assumes the object has an attribute/method to access the original query
query_value = p.query if hasattr(p, 'query') else None

if query_value:
    print(query_value)
else:
    print("No query found for the selected object.")
