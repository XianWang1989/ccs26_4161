
import random

# Assuming tx.search.tweets returns an object where the query can be accessed
# Let's simulate search result objects
class SearchResult:
    def __init__(self, query):
        self.query = query

# Create your wrapped objects
p1 = SearchResult("#hash1")
p2 = SearchResult("#hash2")
p3 = SearchResult("#hash3")
p4 = SearchResult("#hash4")
p5 = SearchResult("#hash5")
p6 = SearchResult("#hash6")
p7 = SearchResult("#hash7")
p8 = SearchResult("#hash8")
p9 = SearchResult("#hash9")
p10 = SearchResult("#hash10")

# List of search results
px = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# Randomly choose one search result
p = random.choice(px)

# Print the query of the selected search result
print(p.query)
