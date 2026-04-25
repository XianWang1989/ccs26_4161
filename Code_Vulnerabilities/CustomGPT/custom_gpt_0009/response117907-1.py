
# Example of element data
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter 1 to input elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to hold the elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in list

    total_weight = 0.0  # Initialize total weight
    for elem in elements:
        weight = float(elemen_data.get(elem))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{elem}' not found in data.")

    print("Total mass =", total_weight)
