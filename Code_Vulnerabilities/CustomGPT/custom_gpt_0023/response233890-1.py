
import random

# Simulating the search object creation for demonstration
class TwitterSearch:
    def __init__(self, query):
        self.query = query  # Store the query

    def get_query(self):
        return self.query  # Method to return the query


# Create Twitter search objects
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

# List of search objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
p = random.choice(px)

# Print the query of the chosen search object
print(p.get_query())  # This will output e.g. "#hash7" if p7 was chosen
