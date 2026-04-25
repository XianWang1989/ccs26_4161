
# Assuming elemen_data is a dictionary containing element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter choice (1 to input elements): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect elements based on user input
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in lower case for consistency

    # Calculate total weight
    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Weight not found for element: {element}")

    print("Total mass =", total_weight)
