
import random

# Assume tx is your Twitter API object
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

px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one of the search results
p = random.choice(px)

# Print the query used for the chosen search
query = p._get_kwargs()[0][1]  # Adjust based on actual object structure
print(f'The chosen query is: "{query}"')
