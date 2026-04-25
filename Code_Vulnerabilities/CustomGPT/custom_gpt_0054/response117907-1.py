
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # List to store the element inputs
    total_weight = 0  # Variable to accumulate total weight

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")  # Prompting for each element
        elements.append(element.lower())  # Storing element in list (lowercase for consistency)

    # Look for the weight of each entered element and calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element))
        if weight is not None:
            total_weight += weight

    print "Total mass =", total_weight
