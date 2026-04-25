
# Assuming you have a dictionary (like `elemen_data`) to get the weights of elements.
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# User chooses to input elements
choice = int(input("Enter your choice (1 for weight calculation): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    # Initialize an empty list to store elements
    elements = []

    # Loop to get the required number of element inputs
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Append the element in lowercase to maintain consistency

    total_weight = 0

    # Calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element, 0))  # Default to 0 if not found
        total_weight += weight

    print("Total mass =", total_weight)
