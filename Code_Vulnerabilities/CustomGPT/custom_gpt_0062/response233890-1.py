
import random

# Define the search queries
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

# Simulate the search object retrieval
px = [tx.search.tweets(q=query) for query in queries]

# Randomly choose one
p = random.choice(px)

# Assuming 'p' can access the original query somehow,
# you will need to find its index in the list
index = px.index(p)  # This gives you the index of the chosen item

# Print the corresponding query
selected_query = queries[index]
print(selected_query)  # Output will be one of the hashtags
