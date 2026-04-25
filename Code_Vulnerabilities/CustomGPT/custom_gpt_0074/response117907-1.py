
# Sample dictionary with element weights (for demonstration)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    'boron': 10.81,
    # Add more elements as needed
}

# Get number of elements from user
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0

# List to store the elements input by the user
elements = []

# Loop to get user input for the specified number of elements
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Add element to the list, in lowercase

# Calculate total weight
for element in elements:
    weight = float(elemen_data.get(element))
    if weight is not None:
        total_weight += weight

print "Total mass =", total_weight
