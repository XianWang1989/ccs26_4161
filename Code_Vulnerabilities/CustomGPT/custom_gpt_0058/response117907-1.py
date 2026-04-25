
# Example element data (replace with your actual data source)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Prompt user for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))

# Initialize an empty list to store user inputs
elements = []

# Loop to get user inputs
for i in range(noelemen):
    element = raw_input(f"Enter element {i+1}: ")
    elements.append(element.lower())  # Store in the list as lowercase

# Calculate total weight
total_weight = 0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight
    else:
        print(f"Element '{element}' not found!")

print("Total mass =", total_weight)
