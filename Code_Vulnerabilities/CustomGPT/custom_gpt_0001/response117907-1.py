
# Sample element data dictionary (for demonstration purposes)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))

# Initialize a list to hold the input elements
elements = []

# Loop to gather user input for the specified number of elements
for i in range(noelemen):
    element = raw_input("Enter element {}: ".format(i + 1))
    elements.append(element.lower())

# Calculate total weight
total_weight = 0
for element in elements:
    weight = float(elemen_data.get(element))
    if weight is not None:
        total_weight += weight
    else:
        print("Element '{}' not found in data.".format(element))

print("Total mass =", total_weight)
