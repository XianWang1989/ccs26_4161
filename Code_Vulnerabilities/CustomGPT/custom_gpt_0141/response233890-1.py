
from random import choice

# Assuming tx is your Twitter API client
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

# Randomly choose one
p = choice(px)

# Assuming that the original query `q` is stored in a way you can access
# This might require knowledge of the underlying object type
# Here's the simplest approach that specifically prints the query.

# This example assumes that you have the query stored somewhere; if not, modify accordingly
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
selected_index = px.index(p)  # Get the index of the selected object
selected_query = queries[selected_index]  # Fetch the corresponding query

# Print the selected query
print(selected_query)
