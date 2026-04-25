
import random

# Simulating the Twitter API calls for demonstration
class TwitterAPI:
    @staticmethod
    def search_tweets(q):
        return f"Results for {q}"

# Create the list of queries and corresponding search results
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Store the search results in a list
results = [TwitterAPI.search_tweets(q) for q in queries]

# Choose a random search result
selected_index = random.choice(range(len(results)))
selected_result = results[selected_index]
selected_query = queries[selected_index]

# Print the chosen query
print(selected_query)
