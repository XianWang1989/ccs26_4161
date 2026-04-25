
import random

# Example search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulating Twitter API searches
results = [(query, tx.search.tweets(q=query)) for query in queries]

# Randomly choosing one result
chosen_result = random.choice(results)

# Extracting the query from the chosen result
chosen_query = chosen_result[0]

# Print the selected query
print(f'Selected query: "{chosen_query}"')
