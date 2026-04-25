
# Assume elemen_data is a dictionary that maps element names to their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

choice = int(raw_input("Enter your choice (1 for weight calculation): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        weight = float(elemen_data.get(element.lower(), 0))

        if weight > 0:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
