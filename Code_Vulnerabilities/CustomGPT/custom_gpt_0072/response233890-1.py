
import tx
from random import choice

# List of search queries and their corresponding results
queries = [
    ("#hash1", tx.search.tweets(q="#hash1")),
    ("#hash2", tx.search.tweets(q="#hash2")),
    ("#hash3", tx.search.tweets(q="#hash3")),
    ("#hash4", tx.search.tweets(q="#hash4")),
    ("#hash5", tx.search.tweets(q="#hash5")),
    ("#hash6", tx.search.tweets(q="#hash6")),
    ("#hash7", tx.search.tweets(q="#hash7")),
    ("#hash8", tx.search.tweets(q="#hash8")),
    ("#hash9", tx.search.tweets(q="#hash9")),
    ("#hash10", tx.search.tweets(q="#hash10"))
]

# Randomly choose one query-result pair
selected_query, result = choice(queries)

# Print the chosen query
print(selected_query)
