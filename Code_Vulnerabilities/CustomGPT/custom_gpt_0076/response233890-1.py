
import random

# Define the searches with their queries
queries = [
    "#hash1", "#hash2", "#hash3", 
    "#hash4", "#hash5", "#hash6", 
    "#hash7", "#hash8", "#hash9", 
    "#hash10"
]

# Create a list to hold the tweets and their corresponding queries
tweets_with_queries = []

for query in queries:
    # Assuming tx.search.tweets() returns a tweet object
    tweets = tx.search.tweets(q=query)
    tweets_with_queries.append((tweets, query))

# Randomly choose one of the tweet/query pairs
selected_tweet, selected_query = random.choice(tweets_with_queries)

# Print the selected query
print(selected_query)
