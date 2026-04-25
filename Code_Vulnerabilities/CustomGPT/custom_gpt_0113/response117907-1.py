
# Sample data for elements and their weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'carbon': 12.011,
    # Add more elements as needed
}

# Get user choice
choice = int(input("Enter your choice (1 to continue): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        weight = elemen_data.get(element.lower())

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
