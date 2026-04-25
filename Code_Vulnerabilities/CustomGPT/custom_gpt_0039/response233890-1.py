
import random

# Assuming tx is your Twitter API client
search_queries = {
    "#hash1": tx.search.tweets(q="#hash1"),
    "#hash2": tx.search.tweets(q="#hash2"),
    "#hash3": tx.search.tweets(q="#hash3"),
    "#hash4": tx.search.tweets(q="#hash4"),
    "#hash5": tx.search.tweets(q="#hash5"),
    "#hash6": tx.search.tweets(q="#hash6"),
    "#hash7": tx.search.tweets(q="#hash7"),
    "#hash8": tx.search.tweets(q="#hash8"),
    "#hash9": tx.search.tweets(q="#hash9"),
    "#hash10": tx.search.tweets(q="#hash10"),
}

# Choose a random query
chosen_query = random.choice(list(search_queries.keys()))
chosen_tweets = search_queries[chosen_query]

# Print the chosen query
print(f'"{chosen_query}"')
