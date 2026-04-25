
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Get the number of elements from user
choice = int(raw_input("Enter 1 to calculate total mass: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0  # Initialize total weight
    elements = []  # List to store input element names

    for i in range(noelemen):
        element = raw_input(f"Enter element #{i + 1}: ")
        elements.append(element.lower())  # Store the input in the list

    # Calculate total weight based on input elements
    for elem in elements:
        weight = elemen_data.get(elem)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{elem}' not found in data.")

    print("Total mass =", total_weight)
