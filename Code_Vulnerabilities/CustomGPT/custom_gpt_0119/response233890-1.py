
from random import choice

# Sample function mocking the tweets search
class TweetSearch:
    def __init__(self, q):
        self.q = q

    def search(self):
        # Simulate a tweet search and return self
        return self

# Create wrapped objects with queries
p1 = TweetSearch(q="#hash1").search()
p2 = TweetSearch(q="#hash2").search()
p3 = TweetSearch(q="#hash3").search()
p4 = TweetSearch(q="#hash4").search()
p5 = TweetSearch(q="#hash5").search()
p6 = TweetSearch(q="#hash6").search()
p7 = TweetSearch(q="#hash7").search()
p8 = TweetSearch(q="#hash8").search()
p9 = TweetSearch(q="#hash9").search()
p10 = TweetSearch(q="#hash10").search()

# List of wrapped objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p = choice(px)

# Print the query of the selected object
print(p.q)
