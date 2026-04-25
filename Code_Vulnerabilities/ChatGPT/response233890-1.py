
from random import choice

# List of hashtags with their corresponding search objects
hashtags = [
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

# Create a list of tuples: (query, search_object)
px = [(hashtag, tx.search.tweets(q=hashtag)) for hashtag in hashtags]

# Randomly choose one of the search objects
chosen_query, chosen_object = choice(px)

# Printing the chosen query
print(f'Chosen query: "{chosen_query}"')
