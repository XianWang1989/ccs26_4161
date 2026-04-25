
# Sample element weight data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

choice = int(raw_input("Enter your choice (1 for weight calculation): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0.0
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

        # Look for the weight of the entered element
        weight = float(elemen_data.get(element.lower(), 0))
        if weight > 0:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
