
# Sample element data for lookup
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # add more elements as needed
}

# Get number of elements from user
noelemen = int(raw_input("Enter total amount of elements: "))

elements = []
total_weight = 0

# Gather user input
for i in range(noelemen):
    element = raw_input(f"Enter element {i + 1}: ")
    elements.append(element)

# Calculate total weight
for element in elements:
    weight = elemen_data.get(element.lower())
    if weight is not None:
        total_weight += weight

print("Total mass =", total_weight)
