
# Sample element data for testing
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    "beryllium": 9.0122
}

choice = int(raw_input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    # List to hold user inputs
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Sum the weights of the entered elements
    for elem in elements:
        weight = float(elemen_data.get(elem))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Warning: Element '{elem}' not found.")

    print("Total mass =", total_weight)
