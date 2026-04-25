
import random

# Simulating wrapped search objects
class SearchWrapper:
    def __init__(self, query):
        self.query = query

    def get_query(self):
        return self.query

# Creating search objects
p1 = SearchWrapper("#hash1")
p2 = SearchWrapper("#hash2")
p3 = SearchWrapper("#hash3")
p4 = SearchWrapper("#hash4")
p5 = SearchWrapper("#hash5")
p6 = SearchWrapper("#hash6")
p7 = SearchWrapper("#hash7")
p8 = SearchWrapper("#hash8")
p9 = SearchWrapper("#hash9")
p10 = SearchWrapper("#hash10")

# List of search objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly select one
p = random.choice(px)

# Print the query associated with the selected search object
print(p.get_query())
