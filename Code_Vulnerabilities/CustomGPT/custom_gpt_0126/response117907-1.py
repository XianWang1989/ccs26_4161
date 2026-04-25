
# Sample element data dictionary
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from the user
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0.0  # Initialize total weight
    elements = []  # List to store user inputs

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")  # Prompt for each element
        elements.append(element)  # Add element to the list

        # Look for the weight of the entered element
        weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if not found
        total_weight += weight  # Add weight to total

    print("Total mass =", total_weight)
