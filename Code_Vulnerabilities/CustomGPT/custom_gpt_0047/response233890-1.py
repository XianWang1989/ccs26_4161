
from random import choice

# Simulated Twitter API call for demonstration
class TwitterAPI:
    def search(self, q):
        return f"Results for {q}"

# Create a simulated API instance
tx = TwitterAPI()

# Define search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Create a list of wrapped search objects
px = [tx.search(q) for q in queries]

# Randomly choose one search result
p = choice(px)

# Retrieve and print the corresponding query
# Find the index of the chosen result
index = px.index(p)

# Print the query
print(f"Selected query: '{queries[index]}'")
