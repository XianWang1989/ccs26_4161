
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = 1  # Sample choice, you can replace this with actual input logic

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to hold element inputs

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store inputs in the list

    total_weight = 0  # Initialize total weight

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
