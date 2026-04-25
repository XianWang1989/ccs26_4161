
import random

# Assuming tx is your Twitter API instance
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

# Store the queries in a list or dictionary for easy access
queries = {
    p1: "#hash1",
    p2: "#hash2",
    p3: "#hash3",
    p4: "#hash4",
    p5: "#hash5",
    p6: "#hash6",
    p7: "#hash7",
    p8: "#hash8",
    p9: "#hash9",
    p10: "#hash10"
}

# Choose one search
p = random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

# Print the corresponding query
print(queries[p])
