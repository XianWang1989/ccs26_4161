
# Example element data dictionary for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
noelemen = int(raw_input("Enter the total amount of elements: "))

total_weight = 0

# Loop to get each element input
for i in range(noelemen):
    element = raw_input("Enter element #{}: ".format(i + 1))
    weight = float(elemen_data.get(element.lower()))

    if weight is not None:
        total_weight += weight
    else:
        print("Element not found in data.")

# Display the total mass
print("Total mass =", total_weight)
