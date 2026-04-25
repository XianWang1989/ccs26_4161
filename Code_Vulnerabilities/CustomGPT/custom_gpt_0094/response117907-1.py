
# Assuming elemen_data is a dictionary containing element names and their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter 1 to calculate total mass: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []
    total_weight = 0.0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)  # Store the element in the list

    for element in elements:
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in the data.")

    print("Total mass =", total_weight)
