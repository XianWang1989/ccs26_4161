
import random

# Define your search queries and their corresponding wrapped objects
search_queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
                  "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulate the tx.search.tweets function
class FakeTwitterAPI:
    def search(self, query):
        return f"Results for {query}"

tx = FakeTwitterAPI()

# Create the list of wrapped objects
px = [tx.search(query) for query in search_queries]

# Randomly choose one wrapped object
p = random.choice(px)

# Find the corresponding query
chosen_index = px.index(p)
chosen_query = search_queries[chosen_index]

# Print the chosen query
print(f'Randomly chosen query: "{chosen_query}"')
