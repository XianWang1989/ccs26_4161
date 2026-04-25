
import random

# Define a function to wrap the tweet search
def create_search_wrapper(query):
    return {'query': query, 'result': tx.search.tweets(q=query)}

# Create wrapped objects
p1 = create_search_wrapper("#hash1")
p2 = create_search_wrapper("#hash2")
p3 = create_search_wrapper("#hash3")
p4 = create_search_wrapper("#hash4")
p5 = create_search_wrapper("#hash5")
p6 = create_search_wrapper("#hash6")
p7 = create_search_wrapper("#hash7")
p8 = create_search_wrapper("#hash8")
p9 = create_search_wrapper("#hash9")
p10 = create_search_wrapper("#hash10")

# List of wrapped search objects
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly select one
p = random.choice(px)

# Print the query for the selected wrapped object
print(p['query'])  # This will print the query (e.g., "#hash7")
