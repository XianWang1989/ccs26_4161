
import random

# Simulated search function (replace this with your actual Twitter API calls)
class TwitterAPI:
    def search_tweets(self, q):
        return f"Searching for: {q}"  # Simulated response

# Initialize the API
tx = TwitterAPI()

# List of query strings
queries = [
    "#hash1", "#hash2", "#hash3", 
    "#hash4", "#hash5", "#hash6", 
    "#hash7", "#hash8", "#hash9", 
    "#hash10"
]

# Create wrapped objects as tuples of (query, result)
px = [(q, tx.search_tweets(q)) for q in queries]

# Randomly select one
selected = random.choice(px)

# Print the query
print(selected[0])  # This will print the selected query, e.g., "#hash7"
