
# Example element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'oxygen': 16.00,
    'carbon': 12.01
}

choice = int(input("Enter 1 to input elements: "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ").lower()
        weight = elemen_data.get(element)

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)
