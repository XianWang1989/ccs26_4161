
import random

# Simulate the Twitter API search
class TwitterAPI:
    @staticmethod
    def search_tweets(q):
        return f"Results for {q}"

tx = TwitterAPI()

# Your search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create wrapped objects
wrapped_objects = [tx.search_tweets(q) for q in queries]

# Randomly choose one
p = random.choice(wrapped_objects)

# Print the corresponding query
chosen_index = wrapped_objects.index(p)  # Find the index of the chosen search
print(queries[chosen_index])  # Print the corresponding query
