
import random

# Define the hashtag queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Assuming tx is your Twitter API object
p_objects = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one wrapped object
p = random.choice(p_objects)

# Get the index of the chosen object
index = p_objects.index(p)

# Print the corresponding query
print(queries[index])
