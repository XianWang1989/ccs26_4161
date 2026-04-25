
from random import choice
import tweepy  # Make sure you have the Twitter API library installed

# Create a sample Twitter API client (you should set this up with your credentials)
# tx = tweepy.API(auth)

# Prepare the search queries
queries = {
    'p1': "#hash1",
    'p2': "#hash2",
    'p3': "#hash3",
    'p4': "#hash4",
    'p5': "#hash5",
    'p6': "#hash6",
    'p7': "#hash7",
    'p8': "#hash8",
    'p9': "#hash9",
    'p10': "#hash10",
}

# Perform the searches and store the results in the dictionary
results = {key: tx.search.tweets(q=query) for key, query in queries.items()}

# Choose one randomly
chosen_key = choice(list(results.keys()))
chosen_result = results[chosen_key]

# Print the corresponding query
chosen_query = queries[chosen_key]
print(f'You searched for: "{chosen_query}"')
