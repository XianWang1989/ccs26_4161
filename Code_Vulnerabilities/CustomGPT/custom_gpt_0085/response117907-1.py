
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

choice = 1  # For demonstration; you can replace this with user input.

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store user inputs

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store elements in a list

    total_weight = 0.0  # Initialize total weight

    for elem in elements:
        weight = float(elemen_data.get(elem))
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
