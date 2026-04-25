
from random import choice

# Simulated search results using a dictionary
search_results = {
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

# Create a list of keys (hashtags)
queries = list(search_results.keys())

# Randomly choose one query
chosen_query = choice(queries)

# Print the chosen query
print(f'Chosen query: "{chosen_query}"')

# Retrieve the corresponding search result if needed
p = search_results[chosen_query]
