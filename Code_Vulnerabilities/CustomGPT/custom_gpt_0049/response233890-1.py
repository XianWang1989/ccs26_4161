
import tx
from random import choice

# Define all the searches with their respective hashtags
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

# Collect all searches in a list
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly select one wrapped object
p = choice(px)

# Method to extract the query 'q' from the wrapped object
def get_query(obj):
    return obj.request.args['q']

# Print the chosen query
print(get_query(p))
