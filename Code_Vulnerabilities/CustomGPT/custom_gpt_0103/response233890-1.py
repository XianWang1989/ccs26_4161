
import random  # Ensure you import random for choice

# Define your queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Perform the searches (assuming tx is defined and authenticated)
results = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one search result
selected_index = random.choice(range(len(results)))
selected_result = results[selected_index]
selected_query = queries[selected_index]

# Print the selected query
print(selected_query)
