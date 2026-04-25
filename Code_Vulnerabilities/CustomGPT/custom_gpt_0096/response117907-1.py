
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # List to store the elements
    total_weight = 0

    for i in range(noelemen):
        element = raw_input("Enter element {}: ".format(i + 1))
        elements.append(element)

        # Look for the weight of the entered element
        weight = elemen_data.get(element.lower())

        if weight is not None:
            total_weight += float(weight)
        else:
            print("Element {} not found in data.".format(element))

    print("Total mass =", total_weight)
