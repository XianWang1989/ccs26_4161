
from random import choice
import tweepy

# Assuming you have authenticated with Twitter API and stored it in 'tx'

# Creating searches
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

# Storing the queries and their corresponding wrapped objects
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choosing one search object
p = choice(px)

# Find the index of the chosen search object
index = px.index(p)

# Print the corresponding query
print(queries[index])
