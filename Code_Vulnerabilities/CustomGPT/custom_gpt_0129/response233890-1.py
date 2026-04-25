
from random import choice

# Assuming tx is your Twitter API object
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", 
           "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Create a list of tuples where each tuple contains the query and the corresponding search result
px = [(q, tx.search.tweets(q=q)) for q in queries]

# Randomly choose one of the tuples
chosen_query, p = choice(px)

# Print the chosen query
print(chosen_query)
