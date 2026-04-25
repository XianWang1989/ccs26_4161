
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)

    # Now, look for the weights of the entered elements
    total_weight = 0.0
    for element in elements:
        weight = float(elemen_data.get(element.lower()))
        if weight is not None:
            total_weight += weight

    print "Total mass =", total_weight
