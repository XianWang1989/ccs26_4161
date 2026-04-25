
# Sample element weight data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    # Create a list to store the elements
    elements = []

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in lowercase for consistency

    total_weight = 0.0

    for elem in elements:
        weight = elemen_data.get(elem)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{elem}' not found in the data.")

    print("Total mass =", total_weight)
