
# Example dictionary to hold element data.
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))

# List to store weights
weights = []

# Loop to get user inputs
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    weight = elemen_data.get(element.lower())

    if weight is not None:
        weights.append(weight)
    else:
        print(f"Element '{element}' not found.")
        weights.append(0)  # Append 0 if element not found

# Calculate total mass
total_weight = sum(weights)
print("Total mass =", total_weight)
