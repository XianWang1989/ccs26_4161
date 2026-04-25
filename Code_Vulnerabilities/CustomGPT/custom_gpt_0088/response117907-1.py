
# Sample data dictionary for demonstration
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.94
}

# Get the number of elements from the user
noelemen = int(input("Enter total amount of elements: "))
elements = []
total_weight = 0

# Loop to gather user input for the specified number of elements
for i in range(noelemen):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate the total weight
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
