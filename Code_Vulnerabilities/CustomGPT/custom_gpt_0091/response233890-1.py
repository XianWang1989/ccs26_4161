
import random

# Mocking the response from tx.search.tweets for demonstration purposes
class MockTweetSearch:
    def __init__(self, query):
        self.query = query

    def get_query(self):
        return self.query

# Assuming tx.search.tweets returns instances of MockTweetSearch for simplicity
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
results = [MockTweetSearch(q) for q in queries]

# Randomly choosing one
p = random.choice(results)

# Printing the query of the selected object
print(p.get_query())
