
# Assume `elemen_data` is a predefined dictionary containing element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

# Get the number of elements user wants to input
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0

# Use a list to store user inputs
elements = []

# Collecting user inputs
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate total weight
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
