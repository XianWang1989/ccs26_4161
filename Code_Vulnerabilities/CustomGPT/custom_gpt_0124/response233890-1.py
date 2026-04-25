
import random

# Simulating your search objects
search_queries = [
    "#hash1",
    "#hash2",
    "#hash3",
    "#hash4",
    "#hash5",
    "#hash6",
    "#hash7",
    "#hash8",
    "#hash9",
    "#hash10"
]

# Example function to simulate the tweet search (replace with actual API call)
def mock_search(q):
    return f"Results for {q}"

# Creating a list of wrapped objects (search results)
px = [mock_search(query) for query in search_queries]

# Randomly choosing a search result
p = random.choice(px)

# Finding the original query based on the selected wrapped object
selected_index = px.index(p)
chosen_query = search_queries[selected_index]

# Print the selected query
print(f'Selected query: "{chosen_query}"')
