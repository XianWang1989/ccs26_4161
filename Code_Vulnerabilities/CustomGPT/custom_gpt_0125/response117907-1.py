
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Choose an option (1): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []
    total_weight = 0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if not found
        elements.append(element)
        total_weight += weight

    print("Total mass =", total_weight)
