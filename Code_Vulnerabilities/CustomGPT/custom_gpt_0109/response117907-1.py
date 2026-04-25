
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []  # List to hold the elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)  # Add the input to the list

    total_weight = 0.0  # Initialize total weight to 0

    for el in elements:
        weight = float(elemen_data.get(el.lower()))
        if weight is not None:
            total_weight += weight  # Accumulate the weight

    print("Total mass =", total_weight)
