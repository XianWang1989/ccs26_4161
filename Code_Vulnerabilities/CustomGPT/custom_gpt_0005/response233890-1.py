
import random

# Sample search function to simulate the Twitter API response
class SearchTweet:
    def __init__(self, query):
        self.query = query

    def search(self):
        return f"Searching for {self.query}"

# Create wrapped objects for each search
p1 = SearchTweet("#hash1")
p2 = SearchTweet("#hash2")
p3 = SearchTweet("#hash3")
p4 = SearchTweet("#hash4")
p5 = SearchTweet("#hash5")
p6 = SearchTweet("#hash6")
p7 = SearchTweet("#hash7")
p8 = SearchTweet("#hash8")
p9 = SearchTweet("#hash9")
p10 = SearchTweet("#hash10")

px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p = random.choice(px)

# Print the query of the selected search object
print(p.query)
