
# Assume elemen_data is a predefined dictionary containing element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add other elements as needed
}

choice = int(raw_input("Enter 1 to calculate total weight: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0.0
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store each element

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
