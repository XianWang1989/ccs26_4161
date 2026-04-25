
import random

# Define your search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Simulate wrapped objects based on queries
wrapped_objects = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one wrapped object
selected_object = random.choice(wrapped_objects)

# Identify the corresponding query
index = wrapped_objects.index(selected_object)
chosen_query = queries[index]

# Print the chosen query
print(chosen_query)
