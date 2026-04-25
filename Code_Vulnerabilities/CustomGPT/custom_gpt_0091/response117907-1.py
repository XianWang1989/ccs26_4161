
# Example element data dictionary
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# Get number of elements from user
noelemen = int(raw_input("Enter total amount of elements: "))
elements = []  # List to store the elements entered by the user

# Collect inputs based on the number of elements
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Store in lowercase for consistency

# Calculate total weight
total_weight = 0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
