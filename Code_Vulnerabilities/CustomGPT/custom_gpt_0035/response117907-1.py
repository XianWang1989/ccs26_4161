
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect elements using a loop
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0

    # Calculate total weight
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in the database.")

    print("Total mass =", total_weight)
