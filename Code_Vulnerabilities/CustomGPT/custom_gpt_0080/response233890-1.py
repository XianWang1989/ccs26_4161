
import random

# Example of mock function (you should replace this with your actual API calls)
class MockTwitterAPI:
    def search(self, q):
        return f"Results for {q}"

tx = MockTwitterAPI()

# Define the search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Create tuple pairs of (search query, result)
search_results = [(q, tx.search(q)) for q in queries]

# Randomly choose one result
chosen = random.choice(search_results)

# Print the query of the chosen result
print(chosen[0])  # This will print the query, e.g., "#hash7"
