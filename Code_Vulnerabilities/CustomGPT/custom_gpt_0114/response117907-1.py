
# Assuming elemen_data is a dictionary that contains element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Choose an option (1 for input elements): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Gather user input for the specified number of elements
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0

    # Calculate total weight
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element {element} not found in data.")

    print("Total mass =", total_weight)
