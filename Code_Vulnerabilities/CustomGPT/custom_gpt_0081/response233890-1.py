
from random import choice

# Sample search function to simulate the Twitter API call
def search_tweets(q):
    # Ideally, this would call the Twitter API, but here
    # we just return a mock object that contains the query
    return {'query': q, 'tweets': []}

# List of searches with their queries
hashtags = [
    "#hash1", "#hash2", "#hash3", 
    "#hash4", "#hash5", "#hash6", 
    "#hash7", "#hash8", "#hash9", 
    "#hash10"
]

# Create a list of wrapped objects
px = [search_tweets(hashtag) for hashtag in hashtags]

# Randomly choose one of the wrapped objects
p = choice(px)

# Print the 'q' value
print(p['query'])  # This will output the associated query, e.g., "#hash7"
