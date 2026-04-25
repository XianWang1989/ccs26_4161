
# Sample element data for lookup
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Ask user for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))

# Create a list to store the user inputs
elements = []

# Gather inputs based on user-defined quantity
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Optionally convert to lowercase for consistency

# Calculate the total weight
total_weight = 0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in the data.")

print("Total mass =", total_weight)
