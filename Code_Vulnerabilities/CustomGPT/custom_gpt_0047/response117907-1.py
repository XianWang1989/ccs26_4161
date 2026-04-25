
# Example dictionary with element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    # Add more elements as needed
}

# Getting the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))

# List to store the elements
elements = []

# Loop to get each element input from user
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate total weight
total_weight = 0.0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
