
# Assume elemen_data is a predefined dictionary with element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# Get user input for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0.0

# Create a list to store the elements
elements = []

# Use a loop to gather the required number of elements from the user
for i in range(noelemen):
    element = raw_input("Enter element {}: ".format(i + 1))
    elements.append(element.lower())

# Calculate total weight
for elem in elements:
    weight = float(elemen_data.get(elem))

    if weight is not None:
        total_weight += weight

# Output the total weight
print("Total mass =", total_weight)
