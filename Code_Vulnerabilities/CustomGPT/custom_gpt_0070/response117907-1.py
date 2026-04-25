
# Example element weight data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))

# Initialize an empty list to store weights
weights = []

for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    weight = elemen_data.get(element.lower())

    if weight is not None:
        weights.append(weight)
    else:
        print(f"Element '{element}' not found.")

# Calculate the total weight
total_weight = sum(weights)
print("Total mass =", total_weight)
