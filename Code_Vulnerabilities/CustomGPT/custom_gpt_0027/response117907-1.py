
# Assume this is a dictionary with element weights for lookup
elemen_data = {
    'hydrogen': 1.0,
    'helium': 4.0,
    'lithium': 6.9,
    # Add more elements as needed
}

if __name__ == "__main__":
    # Asking for the number of elements
    noelemen = int(raw_input("Enter total amount of elements: "))

    # Initialize a list to store the inputs
    elements = []

    # Loop to collect the user inputs
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Calculate total weight
    total_weight = 0.0

    for el in elements:
        weight = elemen_data.get(el)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{el}' not found.")

    print("Total mass =", total_weight)
