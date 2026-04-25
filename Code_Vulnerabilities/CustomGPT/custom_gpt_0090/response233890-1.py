
import random

# Assuming tx.search.tweets is defined elsewhere
# Create a list of searches with their query values
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

# Randomly choose one search
chosen_query, p = random.choice(searches)

# Print the chosen query value
print(f'Selected query: "{chosen_query}"')
