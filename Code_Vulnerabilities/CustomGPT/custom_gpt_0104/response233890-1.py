
import random

class WrappedSearch:
    def __init__(self, query, tweets):
        self.query = query
        self.tweets = tweets

# Assuming tx is your Twitter API object
p1 = WrappedSearch("#hash1", tx.search.tweets(q="#hash1"))
p2 = WrappedSearch("#hash2", tx.search.tweets(q="#hash2"))
p3 = WrappedSearch("#hash3", tx.search.tweets(q="#hash3"))
p4 = WrappedSearch("#hash4", tx.search.tweets(q="#hash4"))
p5 = WrappedSearch("#hash5", tx.search.tweets(q="#hash5"))
p6 = WrappedSearch("#hash6", tx.search.tweets(q="#hash6"))
p7 = WrappedSearch("#hash7", tx.search.tweets(q="#hash7"))
p8 = WrappedSearch("#hash8", tx.search.tweets(q="#hash8"))
p9 = WrappedSearch("#hash9", tx.search.tweets(q="#hash9"))
p10 = WrappedSearch("#hash10", tx.search.tweets(q="#hash10"))

px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p = random.choice(px)

# Print the query of the chosen search object
print(f'Chosen query: "{p.query}"')
