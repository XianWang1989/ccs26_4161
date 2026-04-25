
import random

# List of hashtags
hashtags = [
    "#hash1", "#hash2", "#hash3",
    "#hash4", "#hash5", "#hash6",
    "#hash7", "#hash8", "#hash9", "#hash10"
]

# Simulate search function calls with the hashtags
tweets = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly choose one search
chosen_tweets = random.choice(tweets)

# Get the index of the chosen search to retrieve the corresponding hashtag
index = tweets.index(chosen_tweets)
chosen_hashtag = hashtags[index]

# Print the chosen hashtag
print(chosen_hashtag)
