
import random

# Define your search queries
queries = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]
# Map each query to its corresponding tweet-fetching action
tweets = [tx.search.tweets(q=query) for query in queries]

# Choose a random tweet
chosen_tweet = random.choice(tweets)
chosen_query = queries[tweets.index(chosen_tweet)]

# Print the chosen query
print(chosen_query)
