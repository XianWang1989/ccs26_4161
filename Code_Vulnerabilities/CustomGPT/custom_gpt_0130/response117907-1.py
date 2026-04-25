
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")

        # Look for the weight of the entered element
        weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if not found

        if weight:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
