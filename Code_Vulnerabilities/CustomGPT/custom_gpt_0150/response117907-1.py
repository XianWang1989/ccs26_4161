
# Assuming elemen_data is a dictionary that maps element names to their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from user
noelemen = int(input("Enter total amount of elements: "))

# Initialize a list to store the names of elements
elements = []
total_weight = 0.0

# Loop to get the element names
for i in range(noelemen):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate total weight
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
