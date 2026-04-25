
from random import choice

# Define your search queries
queries = [
    "#hash1", "#hash2", "#hash3", "#hash4",
    "#hash5", "#hash6", "#hash7", "#hash8",
    "#hash9", "#hash10"
]

# Perform the searches and create a list of wrapped objects
px = [tx.search.tweets(q=query) for query in queries]

# Randomly select one of the tweets
p = choice(px)

# To get the query corresponding to the chosen object
index_of_p = px.index(p)
chosen_query = queries[index_of_p]

# Print the chosen query
print(chosen_query)
