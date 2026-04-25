
# Dictionary to hold element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as required
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0

# Loop to collect inputs based on the number of elements
elements = []
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate total weight
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
