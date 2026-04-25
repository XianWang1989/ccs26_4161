
# Assuming elemen_data is a predefined dictionary with elements and their weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store the elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store it in lowercase to match keys in elemen_data

    total_weight = 0  # Initialize total weight variable

    for element in elements:
        weight = float(elemen_data.get(element))

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
