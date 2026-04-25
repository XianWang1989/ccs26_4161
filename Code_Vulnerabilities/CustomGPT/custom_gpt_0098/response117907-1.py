
# Simulated element data (for example purposes)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store inputs in a list

    total_weight = 0.0

    for elem in elements:
        weight = elemen_data.get(elem)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element {elem} not found")

    print("Total mass =", total_weight)
