
import random

# Define your hashtags
hashtags = ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5", "#hash6", "#hash7", "#hash8", "#hash9", "#hash10"]

# Perform searches and store search results in a list
search_results = [tx.search.tweets(q=hashtag) for hashtag in hashtags]

# Randomly select a search result
index = random.choice(range(len(search_results)))  # Get a random index
p = search_results[index]  # Select the corresponding search result
chosen_query = hashtags[index]  # Get the corresponding query

# Print the chosen query
print(chosen_query)  # This will print the hashtag associated with the chosen search result
