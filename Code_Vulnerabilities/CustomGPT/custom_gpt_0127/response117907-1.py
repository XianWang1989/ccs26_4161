
# Create a dictionary to map element names to their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# User choice
choice = int(input("Enter choice (1 for elements): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []  # List to hold the elements entered by the user

    # Gather elements
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in list as lowercase

    total_weight = 0.0  # Initialize total weight

    # Calculate total mass based on entered elements
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Weight not found for element: {element}")

    print("Total mass =", total_weight)
