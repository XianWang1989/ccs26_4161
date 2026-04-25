
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(input("Choose an option (1): "))  # Use input() for Python 3

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))  # Python 3 uses input()

    elements = []
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")  # Prompt for each element
        elements.append(element.lower())  # Store the element in a list

    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
