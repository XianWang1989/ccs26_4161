
# Example data for element weights (you'll need to replace this with your actual data)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

# Asking for user input
noelemen = int(raw_input("Enter total amount of elements: "))

# Initialize a list to store the weights
total_weight = 0

# Generate raw_inputs dynamically
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    weight = elemen_data.get(element.lower())

    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' is not recognized.")

# Output the total weight
print("Total mass =", total_weight)
