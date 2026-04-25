
import random

# Simulating the Twitter API search function
class TwitterAPI:
    def search(self, q):
        return f"Results for {q}"  # Simulated response

tx = TwitterAPI()

# List of search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Perform searches and store results along with their queries
px = [tx.search(q) for q in queries]

# Randomly choose one search result
chosen_index = random.choice(range(len(px)))
p = px[chosen_index]
chosen_query = queries[chosen_index]

# Print the chosen query
print(chosen_query)
