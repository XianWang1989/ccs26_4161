
import random

# Define your queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of wrapped objects using the Twitter API
search_objects = [tx.search.tweets(q=query) for query in queries]

# Randomly choose a wrapped object
chosen_object = random.choice(search_objects)

# Get the index of the chosen object to find the corresponding query
index = search_objects.index(chosen_object)
chosen_query = queries[index]

# Print the chosen query
print(chosen_query)
