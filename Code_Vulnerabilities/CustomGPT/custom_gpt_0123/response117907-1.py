
# Assume this is your element data dictionary
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # add more elements as needed
}

choice = int(raw_input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0.0
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
