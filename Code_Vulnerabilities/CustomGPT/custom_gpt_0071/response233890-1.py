
import random

# Define your individual search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", "#hash5",
    "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"
]

# Perform the searches
p_objects = [tx.search.tweets(q=query) for query in queries]

# Choose a random search object
p = random.choice(p_objects)

# Find the index of the chosen object to get its query
index = p_objects.index(p)
chosen_query = queries[index]

# Print the chosen query
print(chosen_query)
