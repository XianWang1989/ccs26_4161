
# Sample data for elements. This can be replaced with actual data.
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Assuming user chooses option 1
choice = 1
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_weight = 0  # Initialize total weight
    elements = []  # List to hold the input elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i+1}: ")  # Collect each element
        elements.append(element)  # Store in the list

        # Lookup for the weight of the entered element
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight  # Add weight if element is found
        else:
            print(f"Element '{element}' not found.")

    print(f"Total mass = {total_weight}")
