
# Sample element data for lookup
elemen_data = {
    'hydrogen': 1.00794,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add more elements as needed
}

choice = int(raw_input("Enter your choice (1 for mass calculation): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    elements = []
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element {element} not found.")

    print("Total mass =", total_weight)
