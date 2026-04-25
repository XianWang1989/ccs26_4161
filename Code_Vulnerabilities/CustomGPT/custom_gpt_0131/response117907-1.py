
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # ... add other elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to hold the user inputs

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store the input in lowercase for consistency

    total_weight = 0  # Initialize total weight

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Warning: Element '{element}' not found in data.")

    print("Total mass =", total_weight)
