
import random

# Simulating the wrapped object with a custom class
class WrappedTweet:
    def __init__(self, query):
        self.query = query
        # Simulated response from the Twitter API
        self.tweets = f"Tweets for {query}"

    def get_query(self):
        return self.query

# Creating wrapped objects for each hashtag
p1 = WrappedTweet("#hash1")
p2 = WrappedTweet("#hash2")
p3 = WrappedTweet("#hash3")
p4 = WrappedTweet("#hash4")
p5 = WrappedTweet("#hash5")
p6 = WrappedTweet("#hash6")
p7 = WrappedTweet("#hash7")
p8 = WrappedTweet("#hash8")
p9 = WrappedTweet("#hash9")
p10 = WrappedTweet("#hash10")

# List of wrapped objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one wrapped object
p = random.choice(px)

# Print the query from the chosen object
print(p.get_query())
