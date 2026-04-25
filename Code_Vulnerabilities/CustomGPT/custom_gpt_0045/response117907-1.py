
# Example dictionary with sample element data
elemen_data = {
    'hydrogen': 1.0,
    'helium': 4.0,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

choice = int(raw_input("Enter your choice (1 for input): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store user inputs
    total_weight = 0  # Variable to accumulate total weight

    # Loop to collect elements
    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element)  # Add element to the list

    # Calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element.lower(), 0))  # Get weight with a default of 0
        total_weight += weight  # Sum weights

    print("Total mass =", total_weight)
