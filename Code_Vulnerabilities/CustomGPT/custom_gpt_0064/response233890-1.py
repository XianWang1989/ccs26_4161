
from random import choice

# Simulating the Twitter API calls with a mock function
class MockTwitterAPI:
    def search_tweets(self, q):
        return {"query": q, "results": []}  # Replace with actual API call in production

tx = MockTwitterAPI()

# Your search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Creating a list of wrapped objects
search_results = {q: tx.search_tweets(q) for q in queries}

# Choose one query randomly
selected_query = choice(queries)
p = search_results[selected_query]

# Print the selected query
print(p['query'])  # This will output the selected hashtag
