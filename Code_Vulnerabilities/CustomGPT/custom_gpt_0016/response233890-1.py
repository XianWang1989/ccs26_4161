
import random

# Simulated tx.search.tweets function for demonstration
class TwitterAPI:
    def search(self, q):
        return {"query": q}

# Create an instance of your TwitterAPI (assuming tx in your case)
tx = TwitterAPI()

# Defining the search objects
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

# List of search results
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose a search result
p = random.choice(px)

# Print the 'q' value of the chosen result
print(f'Selected query: {p["query"]}')
