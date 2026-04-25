
import random

# Define the queries as a list
queries = [
    "#hash1",
    "#hash2",
    "#hash3",
    "#hash4",
    "#hash5",
    "#hash6",
    "#hash7",
    "#hash8",
    "#hash9",
    "#hash10"
]

# Randomly choose a query
chosen_query = random.choice(queries)

# Now you can perform the search using the chosen query
# For the sake of this example, I'll just simulate the search call
# Assuming `tx.search.tweets(q=chosen_query)` returns a wrapped object
p = tx.search.tweets(q=chosen_query)

# Print the chosen query
print(chosen_query)
