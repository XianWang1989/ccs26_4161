
# Assuming elemen_data is a dictionary containing element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed...
}

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))  # Use input() for Python 3

    total_weight = 0  # Initialize total weight
    elements = []  # List to store user inputs

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element)  # Add to the list

    for element in elements:
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
