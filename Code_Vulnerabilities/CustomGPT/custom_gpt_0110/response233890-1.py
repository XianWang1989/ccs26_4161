
import random

# Assuming tx is your Twitter API instance
searches = [
    ("#hash1", tx.search.tweets(q="#hash1")),
    ("#hash2", tx.search.tweets(q="#hash2")),
    ("#hash3", tx.search.tweets(q="#hash3")),
    ("#hash4", tx.search.tweets(q="#hash4")),
    ("#hash5", tx.search.tweets(q="#hash5")),
    ("#hash6", tx.search.tweets(q="#hash6")),
    ("#hash7", tx.search.tweets(q="#hash7")),
    ("#hash8", tx.search.tweets(q="#hash8")),
    ("#hash9", tx.search.tweets(q="#hash9")),
    ("#hash10", tx.search.tweets(q="#hash10")),
]

# Choose a random search
chosen_search = random.choice(searches)

# Print the value of 'q'
print(f'Query: "{chosen_search[0]}"')
