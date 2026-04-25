
import inspect
from random import choice
import tx  # Assuming this is your Twitter API wrapper

# Search hashtags and get tweets
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

# Choose one randomly
p = choice(px)

# Print the 'q' argument of the chosen tweet
print(inspect.signature(tx.search.tweets).parameters['q'])
