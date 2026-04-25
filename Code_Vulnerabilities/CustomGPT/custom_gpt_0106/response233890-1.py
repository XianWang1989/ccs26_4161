
from random import choice
import tweepy  # Make sure you have tweepy installed

# Assuming `tx` is your Twitter API object
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

# Function to retrieve the query
def get_query(tweets_obj):
    for param in tweets_obj._query:  # '_query' is a hypothetical attribute
        return param  # Modify according to the actual attribute storing the query

# Print the query
query_value = get_query(p)
print(query_value)
