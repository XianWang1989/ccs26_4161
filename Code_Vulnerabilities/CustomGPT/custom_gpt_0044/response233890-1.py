
import random

# Assume tx.search.tweets is defined and returns wrapped objects
search_queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Create a list of tuples (query, result)
wrapped_objects = [(query, tx.search.tweets(q=query)) for query in search_queries]

# Choose a random wrapped object
chosen_query, chosen_result = random.choice(wrapped_objects)

# Print the chosen query
print(f'Chosen query: "{chosen_query}"')
