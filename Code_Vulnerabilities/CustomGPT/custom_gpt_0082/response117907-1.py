
# Sample element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as necessary
}

# Get user input for the number of elements
noelemen = int(input("Enter total amount of elements: "))

# List to store user inputs
elements = []

# Loop to collect unique elements based on user input
for i in range(noelemen):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element.lower())  # Store lowercase for consistency

# Calculate total weight
total_weight = 0

for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Warning: {element} not found in element data.")

print("Total mass =", total_weight)
