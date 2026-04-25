
from random import choice

# Assuming tx is already defined as a Twitter API client
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

px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p = choice(px)

# Extracting the query from the chosen wrapped object
chosen_query = p['search_metadata']['query']  # Adjust based on actual structure

# Printing the chosen query
print(chosen_query)
