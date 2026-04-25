
import random
import tweepy  # Make sure you have the tweepy package installed

# Example Twitter API setup (you need to fill these in with your actual credentials)
# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# tx = tweepy.API(auth)

# List of hashtags as queries
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Dictionary to hold the search results
search_results = {}

# Perform the searches
for hashtag in hashtags:
    search_results[hashtag] = tx.search.tweets(q=hashtag)

# Randomly choose one search result
chosen_hashtag = random.choice(hashtags)
chosen_results = search_results[chosen_hashtag]

# Print the selected query
print(f'Randomly chosen query: "{chosen_hashtag}"')

# Further processing of the chosen results if needed
# For example, you could iterate over the results
for tweet in chosen_results:
    print(tweet.text)  # Prints the text of each tweet in the chosen results
