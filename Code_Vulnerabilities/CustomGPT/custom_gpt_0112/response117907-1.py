
# Assume elemen_data is a dictionary containing element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.941,
    # Add more elements as needed
}

choice = int(input("Enter your choice (1): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []  # List to store the elements

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element lowercase for consistency

    total_weight = 0  # Initialize total weight

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
