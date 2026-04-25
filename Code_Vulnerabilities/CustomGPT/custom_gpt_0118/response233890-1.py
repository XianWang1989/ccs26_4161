
from random import choice

# Assuming tx is your Twitter API object and has been initialized
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

# Choose a random search
p = choice(px)

# To print the query parameter used
# Assuming each pX has a 'query' attribute or similar
# If not directly accessible, you may need to check the API documentation or inspect the object
query_value = p.query  # Or whichever attribute holds the query string
print(query_value)
