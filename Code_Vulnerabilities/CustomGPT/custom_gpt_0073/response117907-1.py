
# Assuming elemen_data is defined
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

choice = 1  # Replace with your actual condition

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
