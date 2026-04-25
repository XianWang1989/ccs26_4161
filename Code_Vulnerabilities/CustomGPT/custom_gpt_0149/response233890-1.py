
import random

# Mocking the search object for demonstration
class MockSearch:
    def __init__(self, query):
        self.query = query

    def __repr__(self):
        return f"Search(query='{self.query}')"

# Creating instances of the search objects
p1 = MockSearch("#hash1")
p2 = MockSearch("#hash2")
p3 = MockSearch("#hash3")
p4 = MockSearch("#hash4")
p5 = MockSearch("#hash5")
p6 = MockSearch("#hash6")
p7 = MockSearch("#hash7")
p8 = MockSearch("#hash8")
p9 = MockSearch("#hash9")
p10 = MockSearch("#hash10")

# Storing them in a list
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choosing one
p = random.choice(px)

# Printing the query associated with the chosen search object
print(f"Chosen query: {p.query}")
