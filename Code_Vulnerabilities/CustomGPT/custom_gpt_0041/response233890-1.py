
import random

class WrappedTweetSearch:
    def __init__(self, query):
        self.query = query
        # Simulate the actual API call
        self.tweets = tx.search.tweets(q=query)

# Create wrapped search objects
p1 = WrappedTweetSearch("#hash1")
p2 = WrappedTweetSearch("#hash2")
p3 = WrappedTweetSearch("#hash3")
p4 = WrappedTweetSearch("#hash4")
p5 = WrappedTweetSearch("#hash5")
p6 = WrappedTweetSearch("#hash6")
p7 = WrappedTweetSearch("#hash7")
p8 = WrappedTweetSearch("#hash8")
p9 = WrappedTweetSearch("#hash9")
p10 = WrappedTweetSearch("#hash10")

# List of wrapped search objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one search
p = random.choice(px)

# Print the query of the chosen search
print(f'Chosen query: "{p.query}"')
