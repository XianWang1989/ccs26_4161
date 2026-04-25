
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to store the elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)  # Store each input in the list

    total_weight = 0  # Initialize total weight
    for elem in elements:
        weight = float(elemen_data.get(elem.lower()))
        if weight is not None:
            total_weight += weight  # Accumulate total weight

    print("Total mass =", total_weight)
