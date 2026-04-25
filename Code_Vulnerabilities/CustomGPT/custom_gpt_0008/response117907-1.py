
# Assume elemen_data is a dictionary with elements and their weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add additional elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0
    elements = []

    # Collecting user inputs in a loop
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in list

    for element in elements:
        weight = float(elemen_data.get(element))
        if weight is not None:
            total_weight += weight
        else:
            print(f"Warning: {element} not found in data.")

    print("Total mass =", total_weight)
