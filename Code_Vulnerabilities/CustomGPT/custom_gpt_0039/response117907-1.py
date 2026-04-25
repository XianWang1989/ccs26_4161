
# Sample data for elements and their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# User choice
choice = 1  # Assume user selected option 1

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    total_weight = 0

    # List to store user inputs
    elements = []

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store the input in the list

    # Calculate total weight
    for el in elements:
        weight = elemen_data.get(el)
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
else:
    print("Invalid choice.")
