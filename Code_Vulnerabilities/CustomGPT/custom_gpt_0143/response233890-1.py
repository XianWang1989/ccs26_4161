
from random import choice

# Mocking the tx.search.tweets to simulate the behavior
class TweetSearch:
    def __init__(self, query):
        self.query = query

    def get_query(self):
        return self.query

# Example search objects
p1 = TweetSearch("#hash1")
p2 = TweetSearch("#hash2")
p3 = TweetSearch("#hash3")
p4 = TweetSearch("#hash4")
p5 = TweetSearch("#hash5")
p6 = TweetSearch("#hash6")
p7 = TweetSearch("#hash7")
p8 = TweetSearch("#hash8")
p9 = TweetSearch("#hash9")
p10 = TweetSearch("#hash10")

# List of search objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly select one search object
p = choice(px)

# Print the query value
print(p.get_query())
