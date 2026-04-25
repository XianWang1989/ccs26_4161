
import random

# Simulating the tweet search function
class MockTwitterAPI:
    def search(self, q):
        return {'query': q, 'tweets': []}  # Mock return

tx = MockTwitterAPI()

# Search queries
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

# List of wrapped objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
p = random.choice(px)

# Print the 'q' value of the chosen object
print(p['query'])  # Output will be the query associated with the chosen object
