
# Sample data for illustration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Ask the user for the number of elements
noelemen = int(raw_input("Enter total amount of elements: "))
elements = []  # List to hold the user inputs
total_weight = 0  # Initialize total weight

# Loop to gather elements based on user input
for i in range(noelemen):
    element = raw_input("Enter element {}: ".format(i + 1))
    elements.append(element.lower())  # Store the input in the list

# Calculate total weight by looking up values in elemen_data
for ele in elements:
    weight = elemen_data.get(ele)
    if weight is not None:
        total_weight += weight
    else:
        print("Element not found in data:", ele)

print("Total mass =", total_weight)
