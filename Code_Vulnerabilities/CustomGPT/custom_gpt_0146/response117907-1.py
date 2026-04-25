
# Sample data for elements and their weights
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add more elements as needed
}

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0
    elements = []  # List to store the elements entered by the user

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")  # Get the element
        elements.append(element.lower())  # Store the element in a list

    # Calculate the total weight based on the elements entered
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
