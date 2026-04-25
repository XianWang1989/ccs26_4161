
# Suppose this dictionary contains element data for lookup
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))
elements = []  # List to store the input elements

# Loop to collect the required number of elements
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Store the element in lowercase

# Calculate total weight
total_weight = 0
for elem in elements:
    weight = elemen_data.get(elem)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Warning: Weight data for '{elem}' not found.")

print("Total mass =", total_weight)
