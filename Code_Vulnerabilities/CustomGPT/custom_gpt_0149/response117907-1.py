
# Assuming elemen_data is a dictionary with element names as keys and their weights as values
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(input("Enter 1 to calculate total weight: "))
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ").lower()
        elements.append(element)

    total_weight = 0
    for element in elements:
        weight = float(elemen_data.get(element))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in the data.")

    print(f"Total mass = {total_weight}")
