
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = 1  # Assume user chooses option 1 for this example
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    elements = []  # List to hold user inputs
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)

    for element in elements:
        weight = float(elemen_data.get(element.lower()))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
