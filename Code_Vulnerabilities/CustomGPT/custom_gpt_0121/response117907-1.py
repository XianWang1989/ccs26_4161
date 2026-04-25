
# Assuming elemen_data is a dictionary that contains element weights
elemen_data = {
    'h': 1.008,
    'he': 4.0026,
    # Add other elements as needed
}

# Get user input for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))

# List to store user inputs
elements = []
total_weight = 0

# Collect the specified number of elements from user
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate total weight
for element in elements:
    weight = float(elemen_data.get(element))
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
