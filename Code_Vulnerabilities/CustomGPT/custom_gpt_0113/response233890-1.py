
import random

# Define your searches
hash_tags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Simulate the search objects
p_objects = [tx.search.tweets(q=tag) for tag in hash_tags]

# Choose a random search object
chosen_index = random.choice(range(len(p_objects)))
p = p_objects[chosen_index]

# Print the corresponding hash tag
print(f'"{hash_tags[chosen_index]}"')
