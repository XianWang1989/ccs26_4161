
from random import choice

# Define your hashtags
hashtags = [
    "#hash1", "#hash2", "#hash3", "#hash4", 
    "#hash5", "#hash6", "#hash7", "#hash8", 
    "#hash9", "#hash10"
]

# Create a dictionary to store the search results with queries as keys
search_results = {hashtag: tx.search.tweets(q=hashtag) for hashtag in hashtags}

# Randomly select one of the hashtags
selected_hashtag = choice(hashtags)

# Get the corresponding search result
selected_result = search_results[selected_hashtag]

# Print the selected query
print(f'Selected query: "{selected_hashtag}"')
