
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []
    total_weight = 0.0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)
        weight = float(elemen_data.get(element.lower(), 0))
        total_weight += weight

    print("Total mass =", total_weight)
