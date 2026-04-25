
# Assuming you have a dictionary with element data
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0

# List to store entered elements
elements = []

# Loop to gather inputs
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Store in lowercase for consistency

# Calculate total weight
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"{element} not found in element data.")

print("Total mass =", total_weight)
