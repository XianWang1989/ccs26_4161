
# Sample data: a dictionary to store element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter total amount of elements: "))

# Initialize an empty list to hold the user input elements
elements = []

# Collect the elements from the user
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element.lower())

# Calculate the total weight
total_weight = 0
for element in elements:
    weight = elemen_data.get(element)
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
