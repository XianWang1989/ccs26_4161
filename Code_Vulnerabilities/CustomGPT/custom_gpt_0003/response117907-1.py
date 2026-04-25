
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
}

# Asking the user for the number of elements
noelemen = int(raw_input("Enter the total amount of elements: "))

# List to store the entered elements
elements = []

# Loop to get user input for each element
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate the total weight
total_weight = 0.0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
