
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = 1  # Assuming this is set based on user choice

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store elements

    # Loop to collect elements based on user input
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store the input in a list

    total_weight = 0  # Initialize total weight

    # Calculate total weight based on the elements entered
    for elem in elements:
        weight = float(elemen_data.get(elem, 0))  # Default to 0 if not found
        total_weight += weight

    print("Total mass =", total_weight)
