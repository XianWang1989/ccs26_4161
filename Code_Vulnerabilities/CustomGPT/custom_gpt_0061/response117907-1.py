
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Calculate total weight
    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
