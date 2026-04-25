
from random import choice

# Assuming tx is your Twitter API client
searches = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Wrap the search results in a dictionary to keep track of the queries
px = {q: tx.search.tweets(q=q) for q in searches}

# Randomly choose one
chosen_query = choice(searches)
chosen_result = px[chosen_query]

# Print the chosen query
print(f'Chosen query: "{chosen_query}"')
