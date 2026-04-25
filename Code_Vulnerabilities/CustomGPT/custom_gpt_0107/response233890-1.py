
import random

# Simulated search function (replace with your actual Twitter API calls)
class TwitterSearch:
    def __init__(self, q):
        self.q = q  # This is where the query is stored

# Create wrapped objects for searches
p1 = TwitterSearch(q="#hash1")
p2 = TwitterSearch(q="#hash2")
p3 = TwitterSearch(q="#hash3")
p4 = TwitterSearch(q="#hash4")
p5 = TwitterSearch(q="#hash5")
p6 = TwitterSearch(q="#hash6")
p7 = TwitterSearch(q="#hash7")
p8 = TwitterSearch(q="#hash8")
p9 = TwitterSearch(q="#hash9")
p10 = TwitterSearch(q="#hash10")

# List of search results
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
p = random.choice(px)

# Print the query value
print(p.q)
