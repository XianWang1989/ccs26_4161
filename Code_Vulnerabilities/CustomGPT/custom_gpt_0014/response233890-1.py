
import random

# Assuming tx is your Twitter API client
p1 = tx.search.tweets(q="#hash1")
p2 = tx.search.tweets(q="#hash2")
p3 = tx.search.tweets(q="#hash3")
p4 = tx.search.tweets(q="#hash4")
p5 = tx.search.tweets(q="#hash5")
p6 = tx.search.tweets(q="#hash6")
p7 = tx.search.tweets(q="#hash7")
p8 = tx.search.tweets(q="#hash8")
p9 = tx.search.tweets(q="#hash9")
p10 = tx.search.tweets(q="#hash10")

# Create a list of tuples containing the queries and their results
px = [
    ("#hash1", p1),
    ("#hash2", p2),
    ("#hash3", p3),
    ("#hash4", p4),
    ("#hash5", p5),
    ("#hash6", p6),
    ("#hash7", p7),
    ("#hash8", p8),
    ("#hash9", p9),
    ("#hash10", p10),
]

# Randomly choose one of the queries
selected_query, p = random.choice(px)

# Print the selected query
print(selected_query)
