
# Dictionary to store element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))
total_weight = 0.0

# Iterate to get inputs for the specified number of elements
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if element not found

    if weight > 0:
        total_weight += weight
    else:
        print(f"Element '{element}' not found.")

print("Total mass =", total_weight)
