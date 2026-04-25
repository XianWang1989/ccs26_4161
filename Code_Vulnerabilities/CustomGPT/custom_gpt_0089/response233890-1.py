
from random import choice

# Simulating the Twitter API search calls with a simple class
class MockTwitterAPI:
    def search(self, q):
        return {"query": q}  # This simulates the response with the query

tx = MockTwitterAPI()

# Create a list of searches
p1 = tx.search(q="#hash1")
p2 = tx.search(q="#hash2")
p3 = tx.search(q="#hash3")
p4 = tx.search(q="#hash4")
p5 = tx.search(q="#hash5")
p6 = tx.search(q="#hash6")
p7 = tx.search(q="#hash7")
p8 = tx.search(q="#hash8")
p9 = tx.search(q="#hash9")
p10 = tx.search(q="#hash10")

px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p = choice(px)

# Print the query from the chosen object
print(p["query"])  # This will output the value of 'q'
