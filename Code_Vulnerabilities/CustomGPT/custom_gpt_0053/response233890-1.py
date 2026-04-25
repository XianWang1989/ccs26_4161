
import random

# Assuming tx is your Twitter API object
p1 = ("#hash1", tx.search.tweets(q="#hash1"))
p2 = ("#hash2", tx.search.tweets(q="#hash2"))
p3 = ("#hash3", tx.search.tweets(q="#hash3"))
p4 = ("#hash4", tx.search.tweets(q="#hash4"))
p5 = ("#hash5", tx.search.tweets(q="#hash5"))
p6 = ("#hash6", tx.search.tweets(q="#hash6"))
p7 = ("#hash7", tx.search.tweets(q="#hash7"))
p8 = ("#hash8", tx.search.tweets(q="#hash8"))
p9 = ("#hash9", tx.search.tweets(q="#hash9"))
p10 = ("#hash10", tx.search.tweets(q="#hash10"))

# List of (query, wrapped object) tuples
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one
p = random.choice(px)

# Print the query value
print(p[0])  # This will print the selected query, e.g., "#hash7"
