
# Example dictionary to mimic data lookup
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0.0

# List to hold the entered element names
elements = []

# Loop based on user input
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate the total weight
for elem in elements:
    weight = float(elemen_data.get(elem))
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
