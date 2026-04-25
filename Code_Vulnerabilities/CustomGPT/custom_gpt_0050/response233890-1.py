
from random import choice

# Create a dictionary to hold the search queries and their results
searches = {
    "#hash1": tx.search.tweets(q="#hash1"),
    "#hash2": tx.search.tweets(q="#hash2"),
    "#hash3": tx.search.tweets(q="#hash3"),
    "#hash4": tx.search.tweets(q="#hash4"),
    "#hash5": tx.search.tweets(q="#hash5"),
    "#hash6": tx.search.tweets(q="#hash6"),
    "#hash7": tx.search.tweets(q="#hash7"),
    "#hash8": tx.search.tweets(q="#hash8"),
    "#hash9": tx.search.tweets(q="#hash9"),
    "#hash10": tx.search.tweets(q="#hash10"),
}

# Randomly choose a query
chosen_query = choice(list(searches.keys()))
# Get the corresponding result
p = searches[chosen_query]

# Print the chosen query
print(f'Query: "{chosen_query}"')
