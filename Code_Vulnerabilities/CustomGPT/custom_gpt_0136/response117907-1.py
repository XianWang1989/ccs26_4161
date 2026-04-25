
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []
    total_weight = 0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)

        # Look for the weight of the entered element
        weight = float(elemen_data.get(element.lower()))

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
