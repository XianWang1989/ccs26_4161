
# Sample element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

choice = 1  # Simulating user choice
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0
    for elem in elements:
        weight = elemen_data.get(elem)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{elem}' not found in data.")

    print("Total mass =", total_weight)
