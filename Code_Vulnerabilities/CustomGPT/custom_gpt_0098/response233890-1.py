
import random

# Simulated search function for demonstration purposes
class TwitterSearch:
    def __init__(self, query):
        self.query = query

    def get_query(self):
        return self.query

# Create your wrapped objects
p1 = TwitterSearch("#hash1")
p2 = TwitterSearch("#hash2")
p3 = TwitterSearch("#hash3")
p4 = TwitterSearch("#hash4")
p5 = TwitterSearch("#hash5")
p6 = TwitterSearch("#hash6")
p7 = TwitterSearch("#hash7")
p8 = TwitterSearch("#hash8")
p9 = TwitterSearch("#hash9")
p10 = TwitterSearch("#hash10")

# List of searches
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
p = random.choice(px)

# Print the query of the chosen object
print(p.get_query())
