
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # Create an empty list to store the elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)  # Add the input to the list

    total_weight = 0  # Initialize total weight

    # Look for the weights of the entered elements
    for element in elements:
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight  # Accumulate the weights

    print "Total mass =", total_weight
